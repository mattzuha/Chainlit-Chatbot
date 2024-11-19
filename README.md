
# 🤖 Custom Data Chatbot with Ollama 3.1

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

# Prerequisites
-  **Python:** Ensure you have Python 3.7+ installed.
-  **Ollama 3.1:** Download and install Ollama 3.1 from their official site.

# Initial setup
```shell
# run ingest.py to create vector store
$ python ingest.py

# one cmd and download llama 3.1
$ ollama run llama3.1 
```

## 🖥️ Running Locally
```shell
$ chainlit run model.py
```

## 💁 Authors
- **10421091 - Nguyen Nguyen Minh**
- **10421114- Nguyen Khanh Hoang Minh**

--- 

Hope you enjoy using this chatbot! 🎉
