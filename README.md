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
   GROQ_API_KEY="enter_your_groq_api_key"
   GOOGLE_API_KEY="enter_your_google_api_key"
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

## Snapshots

![1  REG ](https://github.com/user-attachments/assets/5b1a36b7-1e14-4c51-a62a-ef657b7675bd)
![4  log](https://github.com/user-attachments/assets/ad290d08-92d9-483a-941b-f52de968cfd3)
![6  home](https://github.com/user-attachments/assets/2db3b787-a9a9-4089-abb4-20356af4070c)
![9  db ready](https://github.com/user-attachments/assets/932adbd5-fffb-4181-8e11-0e524c14d14b)
![10  right resp](https://github.com/user-attachments/assets/a7c797a5-4a6a-43f5-ac92-1494d5898d71)
![13  voice input right resp](https://github.com/user-attachments/assets/1ac86391-02ab-4834-ac5c-8237b9fb4c22)
















