# LlamaIndex RAG Implementation

A Streamlit-based web app for **retrieval-augmented generation (RAG)** using PDFs.  
Users can upload PDF documents and ask questions, and the app retrieves answers using **LlamaIndex** and **OpenAI** embeddings.

---

## Features

- Upload one or multiple PDFs.
- Convert PDFs into a **vector store index** using LlamaIndex.
- Ask questions and get **contextual answers** from the PDFs.
- **Submit** and **Clear** buttons for easy Q&A workflow.
- Modular code structure for easy maintenance and extension.

---

## Folder Structure

project/
│
├─ main.py # Streamlit UI
├─ config.py # Load API keys from .env
├─ file_handler.py # PDF upload and save logic
├─ indexer.py # LlamaIndex creation and query engine
├─ requirements.txt # Python dependencies
├─ .env.example # Example for storing API keys
├─ .gitignore # Files to exclude from GitHub
└─ README.md # Project documentation


---

## Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo

2. Create a virtual environment and activate it
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt

4. Set up your OpenAI API key
cp .env.example .env
# Edit .env and add your actual key
 5. Run the app
 streamlit run main.py

Usage

Open the app in your browser.

Upload one or more PDF files.

Type a question about the PDF content.

Click Submit to get the answer.

Use Clear to reset the question and answer fields.

Security

Do not commit .env with your API key to GitHub.

Use .env.example as a template for others.

For deployment (e.g., Streamlit Cloud or Heroku), set the API key in environment variables or secrets, not in .env.

Dependencies

streamlit

llama-index

openai

python-dotenv

Optional (if extending functionality):

numpy, scikit-learn, scipy, matplotlib, chromadb, huggingface-hub, tiktoken


License

MIT License – see LICENSE
 for details.

 Future Improvements

Support for multiple PDFs simultaneously.

Integration with ChromaDB or other vector databases for persistent storage.

Multi-user deployment with authentication.

UI enhancements with better conversation history and context display.


---

This README covers:

- **Project overview**
- **Features**
- **Setup & usage instructions**
- **Security practices**
- **Dependencies**
- **Future improvements**

---

If you want, I can **also create a “ready-to-push” GitHub repo structure** including **modular files, `.env.example`, sample PDFs**, and this README — so you can just `git push` and it’s ready for use.  

Do you want me to do that next?
