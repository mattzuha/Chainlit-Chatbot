# Custom Data Chatbot with Ollama 3.1 8b
This project demonstrates a multi-page chatbot app that allows users to interact with a Language Model (LLM) for various use cases, including chatting with custom documents. The app is built using Langchain and Chanlit, making it accessible and easy to use.

## Useful Links 🔗
- **Documentation:** Get started with our comprehensive [Chainlit Documentation](https://docs.chainlit.io) 📚
- **Discord Community:** Join our friendly [Chainlit Discord](https://discord.gg/k73SQ3FyUh) to ask questions, share your projects, and connect with other developers! 💬

We can't wait to see what you create with Chainlit! Happy coding! 💻😊

## 💬 Chatbot use cases
This chatbot is designed to answer user questions based on both interactive conversations and context extracted from custom documents (PDF and TXT files).

## <img src="https://pbs.twimg.com/profile_images/1657041791613370369/sm9jmDm3_400x400.jpg" width="40" height="22"> Chainlit App
You can access this app through this link: [chainlit-chatbot](https://www.facebook.com/)

## 🚀 Getting start
Follow these instructions to set up and run the chatbot locally. \
Prerequisites
-  **Python:** Ensure you have Python 3.7+ installed.
-  **Ollama 3.1:** Download and install Ollama 3.1 from their official site.

Installation
1. Clone the repository:
```shell
git clone https://github.com/mattzuha/TestChat4.git
cd TestChat4
```

2. Install the required dependencies:
```shell
pip install -r requirements.txt
```

3. Download and start the Ollama model in your command line:
```shell
ollama run llmama 3.1
```

Setting Up the Vector Database \
To enable document-based interactions, run the following command to ingest your documents and create a vector database:
```shell
python ingest.py
```

Running the App \
Start the Chanlit app by running the main script:
```shell
chanlit run Home.py
```

## 🖥️ Running locally
```shell
# Run main streamlit app
$ chainlit run model.py
```

## 📦 Running with Docker
```shell
# To generate image
$ docker build -t langchain-chatbot .

# To run the docker container
$ docker run -p 8501:8501 langchain-chatbot
```

## 💁 Author
10421091 - Nguyen Nguyen Minh
10...... - Nguyen Khanh Hoang Minh

