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

## snapshots

![1  REG ](https://github.com/user-attachments/assets/5b1a36b7-1e14-4c51-a62a-ef657b7675bd)
![2  reg](https://github.com/user-attachments/assets/c0f52b1d-7ba9-4fb4-9c74-1b3bc2156f89)
![3  reg](https://github.com/user-attachments/assets/1c89c631-8e47-429a-8c29-4179929d95c5)
![3 1 reg](https://github.com/user-attachments/assets/20215b0b-f62c-4c61-93bb-2cd2f706b750)
![4  log](https://github.com/user-attachments/assets/ad290d08-92d9-483a-941b-f52de968cfd3)
![4 1 log](https://github.com/user-attachments/assets/78190fc5-9057-4162-8673-b47ceb0b26ed)
![5  log](https://github.com/user-attachments/assets/58147e0e-6bbf-49e9-acd1-cc77516ec9b7)
![6  home](https://github.com/user-attachments/assets/2db3b787-a9a9-4089-abb4-20356af4070c)
![7  uplod](https://github.com/user-attachments/assets/9fdc398f-d30b-44bb-b3c0-7b304cac1fbc)
![8  process](https://github.com/user-attachments/assets/ed7c2e94-7c84-4fbb-b52b-10a55ce445ac)
![9  db ready](https://github.com/user-attachments/assets/932adbd5-fffb-4181-8e11-0e524c14d14b)
![10  right resp](https://github.com/user-attachments/assets/a7c797a5-4a6a-43f5-ac92-1494d5898d71)
![11  wrong resp](https://github.com/user-attachments/assets/ad992c47-4fd0-4f3f-b1d2-a47c99203da5)
![12  voice input](https://github.com/user-attachments/assets/ac59acab-fb7c-4128-9cc5-c411a772e58f)
![13  voice input right resp](https://github.com/user-attachments/assets/1ac86391-02ab-4834-ac5c-8237b9fb4c22)
![14  voice input not resp](https://github.com/user-attachments/assets/417d0bb3-2493-499c-896d-cc64c885d93d)
















