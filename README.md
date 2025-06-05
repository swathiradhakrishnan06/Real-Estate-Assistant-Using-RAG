# 🏠 Real Estate News Assistant using Retrieval-Augmented Generation (RAG)

This project is a **GenAI-powered Real Estate Assistant** that extracts and summarizes insights from real estate-related **news articles** using **Retrieval-Augmented Generation (RAG)**.

Built with **Streamlit**, **LangChain**, **ChromaDB**, **Groq-hosted LLaMA 3**, and **Alibaba's GTE Embeddings**, the app enables users to input URLs of real estate news articles, retrieve key details, and ask questions with accurate source-backed answers.

---

## 🚀 Features

- 🔗 Input up to **3 real estate news URLs**
- 🧾 **Web Content Ingestion**:
  - Uses `UnstructuredURLLoader` or `SeleniumURLLoader` to handle structured and dynamic web pages
- 🧠 **RAG Pipeline**:
  - Recursive text splitting using `RecursiveCharacterTextSplitter`
  - Embeddings via **Alibaba-NLP/gte-base-en-v1.5**
  - Vector storage with **ChromaDB**
  - LLM-based response generation using **LLaMA-3-70B-Versatile** hosted on **Groq**
- 🖥️ **Streamlit Interface**:
  - URL inputs
  - **Retrieve Details** button
  - Natural language question input
  - Answer display with **source citation**

---

## 📁 Project Structure

```

real-estate-news-assistant/
├── main.py           # Streamlit UI logic
├── rag.py            # Core RAG pipeline (loading, embedding, retrieval, generation)
├── requirements.txt  # Python dependencies
├── .env              # API keys and config (not committed)
└── README.md         # Project documentation

````

---

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/swathiradhakrishnan06/Real-Estate-Assistant-Using-RAG.git
cd Real-Estate-Assistant-Using-RAG
````

2. **Install required packages**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
   Create a `.env` file in the project root with the following content:

```
GROQ_API_KEY=your_groq_api_key
```

4. **Run the application**

```bash
streamlit run main.py
```

---

## 🧪 Example Questions

Once you’ve added real estate news URLs and clicked **Retrieve Details**, try questions like:

* "What was the 30-year fixed mortgage rate along with the date?"
* "What did the Fed decide regarding interest rates in December 2024?"

---

## 🛠️ Tech Stack

| Component       | Tool / Service                               |
| --------------- | -------------------------------------------- |
| Frontend UI     | [Streamlit](https://streamlit.io)            |
| Framework       | [LangChain](https://www.langchain.com)       |
| LLM             | LLaMA 3 70B (via [Groq](https://groq.com))   |
| Embedding Model | Alibaba-NLP/gte-base-en-v1.5                 |
| Loaders         | `UnstructuredURLLoader`, `SeleniumURLLoader` |
| Vector DB       | [ChromaDB](https://www.trychroma.com)        |

---

## 📌 Notes

* Ensure the URLs point to **real estate-related news** with accessible HTML content.
* Groq is used for ultra-fast and cost-effective LLM inference.
* Alibaba's GTE model ensures efficient, multilingual embedding performance.


