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
   git clone https://github.com/yourusername/document-genie.git
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

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Langchain](https://langchain.readthedocs.io/en/latest/)
- [Google Generative AI](https://cloud.google.com/generative-ai)

```

### Customization Tips

- Replace `yourusername/document-genie.git` with the actual URL of your GitHub repository.
- Fill in the actual API keys for your environment variables in the instructions.
- Adjust any other details to match your project's specific needs.

Feel free to modify this `README.md` as necessary! Let me know if you need further help.
