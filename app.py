import streamlit as st
import sqlite3
import os
import time
import docx2txt
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import speech_recognition as sr
from pydub import AudioSegment

# Load environment variables
load_dotenv()

# Initialize Streamlit session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = None
if 'page' not in st.session_state:
    st.session_state['page'] = None
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'uploaded_documents' not in st.session_state:
    st.session_state['uploaded_documents'] = []


# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS documents
                 (document_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, document_name TEXT, document_path TEXT,
                 FOREIGN KEY(user_id) REFERENCES users(user_id))''')
    conn.commit()
    conn.close()


# Function to create a new user
def create_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()


# Function to authenticate a user
def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    return user


# Function to check if a user exists
def user_exists(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    conn.close()
    return user


# Function to store uploaded documents for a user
def store_uploaded_documents(username, uploaded_files):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Fetch user_id based on username
    c.execute('SELECT user_id FROM users WHERE username = ?', (username,))
    user_id = c.fetchone()[0]

    os.makedirs(f"uploaded_files/{username}", exist_ok=True)

    # Store each uploaded document in the documents table
    for uploaded_file in uploaded_files:
        file_path = os.path.join(f"uploaded_files/{username}", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Insert document information into the documents table
        c.execute('INSERT INTO documents (user_id, document_name, document_path) VALUES (?, ?, ?)',
                  (user_id, uploaded_file.name, file_path))

    conn.commit()
    conn.close()

# Function to get user documents
def get_user_documents(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Fetch user_id based on username
    c.execute('SELECT user_id FROM users WHERE username = ?', (username,))
    user_id = c.fetchone()[0]

    # Fetch documents associated with the user
    c.execute('SELECT document_id, document_name, document_path FROM documents WHERE user_id = ?', (user_id,))
    documents = c.fetchall()

    conn.close()
    return documents


# Function to clear chat history for the current user
def clear_chat_history():
    st.session_state['chat_history'] = []


# Function to display user-specific documents in the sidebar
def display_user_documents(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    # Fetch user_id based on username
    c.execute('SELECT user_id FROM users WHERE username = ?', (username,))
    user_id = c.fetchone()[0]

    # Fetch documents associated with the user
    c.execute('SELECT document_name FROM documents WHERE user_id = ?', (user_id,))
    documents = c.fetchall()

    conn.close()

    # Display documents in the sidebar
    if documents:
        st.sidebar.title("Uploaded Documents")
        displayed_documents = set()  # Use set to track displayed document names
        for doc in documents:
            doc_name = doc[0]
            if doc_name not in displayed_documents:
                st.sidebar.write(doc_name)
                displayed_documents.add(doc_name)


# Function to embed vectors for uploaded documents
def vector_embedding(uploaded_files, username):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    docs = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join(f"uploaded_files/{username}", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if uploaded_file.type == "application/pdf":
            loader = PyPDFLoader(file_path)
        elif uploaded_file.type == "text/plain":
            loader = TextLoader(file_path)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            loader = CustomDocxLoader(file_path)
        else:
            st.warning(f"Unsupported file type: {uploaded_file.type}")
            continue

        docs.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(docs)
    vectors = FAISS.from_documents(final_documents, embeddings)

    st.session_state['embeddings'] = embeddings
    st.session_state['docs'] = docs
    st.session_state['text_splitter'] = text_splitter
    st.session_state['final_documents'] = final_documents
    st.session_state['vectors'] = vectors

# Custom Document Class
class Document:
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata


# Custom Word Document Loader
class CustomDocxLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        text = docx2txt.process(self.file_path)
        return [Document(page_content=text, metadata={"source": self.file_path})]


# Initialize the LLM
groq_api_key = os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Define the prompt template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    <context>
    Questions: {input}
    """
)


# Registration Page
def registration_page():
    st.title("User Registration")

    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')

    if st.button("Register"):
        if new_password == confirm_password:
            if not user_exists(new_username):
                create_user(new_username, new_password)
                st.success("User registered successfully! You can now log in.")
                st.session_state['page'] = "login_page"
            else:
                st.error("Username already exists. Please choose a different username.")
        else:
            st.error("Passwords do not match. Please try again.")

    st.text("📝If you Already have an account? \n Please login Yourself...")


# Login Page
def login_page():
    st.title("User Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        user = authenticate_user(username, password)
        if user:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['page'] = "Document Q&A"  # Set the page to redirect
            clear_chat_history()  # Clear chat history for the current user
        else:
            st.error("Invalid username or password. Please try again.")

    st.text("📝If you Don't have an account? \n Please Register yourself...")

# Main Function
def main():
    st.sidebar.title("Navigation")

    # Check if user is logged in
    if st.session_state['logged_in']:
        current_page = st.session_state.get('page', 'Document Q&A')
        username = st.session_state['username']

        # Logout button
        if st.sidebar.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = None
            st.session_state['page'] = None
            st.session_state['chat_history'] = []
            st.session_state['uploaded_documents'] = []
            st.experimental_rerun()

        # Display user documents in sidebar
        display_user_documents(username)

        if current_page == "Document Q&A":
            st.title("DOCUMENT GENIE \n For Fast Document Analysis")

            # File upload in sidebar
            with st.sidebar:
                uploaded_files = st.file_uploader("Upload PDF, Text, or Word files", type=["pdf", "txt", "docx"], accept_multiple_files=True)

                if uploaded_files and st.sidebar.info(
                        "Documents uploaded successfully.\n Click 'Submit' button to process.") and st.sidebar.button(
                        "Submit"):
                    with st.spinner("Documents processing ..."):
                        try:
                            store_uploaded_documents(username, uploaded_files)
                            vector_embedding(uploaded_files, username)
                            st.success("Vector Store DB is ready.")
                            st.session_state['uploaded_documents'].extend([file.name for file in uploaded_files])
                            clear_chat_history()  # Clear chat history for the current user
                        except Exception as e:
                            st.error(f"An error occurred during embedding: {e}")

                #if st.session_state['uploaded_documents']:
                    #st.subheader("Uploaded Documents:")
                    #displayed_documents = set()  # Use set to track displayed document names
                    #for doc in st.session_state['uploaded_documents']:
                        #if doc not in displayed_documents:
                            #st.write(doc)
                            #displayed_documents.add(doc)

            # Chat interface
            prompt1 = st.text_input("Enter Your Question From Documents")

            # Voice search
            if st.button("🎙️ Voice Input"):
                recognizer = sr.Recognizer()
                with sr.Microphone() as source:
                    st.write("Listening...")
                    audio = recognizer.listen(source)
                    try:
                        query = recognizer.recognize_google(audio)
                        st.session_state.chat_history.append({"role": "user", "content": query})
                        st.success(f"You said: {query}")
                        prompt1 = query
                    except sr.UnknownValueError:
                        st.error("Google Speech Recognition could not understand audio")
                    except sr.RequestError as e:
                        st.error(f"Could not request results from Google Speech Recognition service; {e}")

            if prompt1:
                if st.session_state.chat_history and st.session_state.chat_history[-1]["content"] != prompt1:
                    st.session_state.chat_history.append({"role": "user", "content": prompt1})
                if "vectors" in st.session_state:
                    try:
                        document_chain = create_stuff_documents_chain(llm, prompt)
                        retriever = st.session_state.vectors.as_retriever()
                        retrieval_chain = create_retrieval_chain(retriever, document_chain)

                        with st.spinner("Fetching response..."):
                            start = time.process_time()
                            response = retrieval_chain.invoke({'input': prompt1})
                            response_time = time.process_time() - start

                        # Clear chat history button
                        if st.button("Clear Chat History"):
                            clear_chat_history()

                        st.session_state.chat_history.append({"role": "assistant", "content": response['answer']})
                        st.session_state.chat_history.append(
                            {"role": "metadata", "content": f"Response time: {response_time:.2f} seconds"})
                    except Exception as e:
                        st.error(f"An error occurred during querying: {e}")
                else:
                    st.error("Please upload and embed documents first.")

            # Display chat history with emojis for user and assistant
            for chat in reversed(st.session_state.chat_history):
                if chat["role"] == "user":
                    st.markdown(
                        f'<div style="text-align: right; padding-left: 10px;">{chat["content"]}: <span style="font-size: 40px;">👤</span></div>',
                        unsafe_allow_html=True)
                elif chat["role"] == "assistant":
                    st.markdown(
                        f'<div style="text-align: left; padding-right: 10px;"><span style="font-size: 40px;">🤖</span>: {chat["content"]}</div>',
                        unsafe_allow_html=True)
                elif chat["role"] == "metadata":
                    st.markdown(f'<div style="text-align: center;">{chat["content"]}</div>', unsafe_allow_html=True)

    else:
        # Display login or registration page
        current_page = st.sidebar.radio("Go to", ["Login", "Register"])

        if current_page == "Register":
            registration_page()
        elif current_page == "Login":
            login_page()


if __name__ == '__main__':
    init_db()
    main()


