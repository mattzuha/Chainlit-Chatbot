
# 🤖 Custom Data Chatbot with Ollama 3.1 8b

This project presents a multi-page chatbot app enabling users to interact with a Language Model (LLM) for diverse use cases, including Q&A from custom documents. The app is built with **Langchain** and **Chainlit** to make it accessible and user-friendly.


## 🔗 Useful Links 
- **[Chainlit Documentation](https://docs.chainlit.io)** 📚 - Get started with comprehensive documentation.
- **[Chainlit Discord](https://discord.gg/k73SQ3FyUh)** 💬 - Join our community for support, project sharing, and networking!

We’re excited to see what you create with Chainlit! Happy coding! 💻😊


## 💬 Chatbot Use Cases
This chatbot is designed to answer user queries using:
- **Conversational Interactions** - Engage directly with the chatbot.
- **Document-based Context** - Answers from custom documents (PDF & TXT).


## 🚀 Getting Started
Follow these steps to set up and run the chatbot locally.

### Prerequisites
- **Python 3.7+** - Make sure you have Python installed.
- **Ollama 3.1** - Download and install from [Ollama's official site](https://www.ollama.com).


### 🛠️ Installation

1. **Clone the repository:**
   ```shell
   git clone https://github.com/mattzuha/TestChat4.git
   cd TestChat4
   ```

2. **Install dependencies:**
   ```shell
   pip install -r requirements.txt
   ```

3. **Start Ollama Model:**
   ```shell
   ollama run llmama 3.1
   ```

### ⚙️ Setting Up the Vector Database
For document-based interactions, run the following command to ingest documents and create a vector database:
```shell
python ingest.py
```

### 🖥️ Running Locally
```shell
# Run the main Chainlit app
chainlit run model.py
```

### 📦 Running with Docker

1. **Build Docker Image:**
   ```shell
   docker build -t langchain-chatbot .
   ```

2. **Run Docker Container:**
   ```shell
   docker run -p 8501:8501 langchain-chatbot
   ```

## 🌐 Accessing the App
- **Chainlit App**: You can access the app [here](https://www.facebook.com/)

## 💁 Authors
- **10421091 - Nguyen Nguyen Minh**
- **10...... - Nguyen Khanh Hoang Minh**

--- 

Hope you enjoy using this chatbot! 🎉
