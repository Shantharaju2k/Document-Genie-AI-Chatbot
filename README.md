# Document Genie

## Overview

**Document Genie** is a Streamlit application designed for efficient document analysis and information retrieval. It utilizes advanced Natural Language Processing (NLP) capabilities to answer questions based on the content of uploaded documents. Users can upload PDF, TXT, or DOCX files, and the application will process the documents to provide contextual answers to user queries.

## Features

- User registration and authentication.
- Upload and store multiple document types (PDF, TXT, DOCX).
- Vector embedding of documents for efficient querying.
- Voice input functionality for asking questions.
- Interactive chat interface to engage with the document content.

## Technologies Used

- **Streamlit**: A Python library for building interactive web applications.
- **SQLite**: A lightweight database for storing user credentials and document metadata.
- **Langchain**: A framework for building applications powered by language models.
- **Google Generative AI**: For document embedding and contextual responses.
- **SpeechRecognition**: For converting speech to text input.
- **pydub**: For audio manipulation.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Shantharaju-pojects/Document_Genie-AI_chatbot.git
   cd document-genie
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   Create a `.env` file in the project root and add the following lines, replacing placeholders with your actual API keys:

   ```plaintext
   GROQ_API_KEY=your_groq_api_key
   GOOGLE_API_KEY=your_google_api_key
   ```

## Usage

1. Run the application:

   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to `http://localhost:8501`.

3. Register a new account or log in with existing credentials.

4. Upload documents and ask questions using the chat interface or voice input.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Langchain](https://langchain.readthedocs.io/en/latest/)
- [Google Generative AI](https://cloud.google.com/generative-ai)

```
![1  REG ](https://github.com/user-attachments/assets/b2ef5908-4984-4282-8b80-0d7392b2e7a6)
![1  REG ](https://github.com/user-attachments/assets/754339cc-ad36-4b7a-8dff-7b58d51bb189)

