
# 🤖 **Custom Data Chatbot with Ollama 3.1 8b**  

This project presents a **multi-page chatbot app** enabling users to interact with a **Language Model (LLM)** for diverse use cases, specifically answering queries based on the **Encyclopedia of Human Development**. Built with **LangChain** and **Chainlit**, the app is designed to be accessible and user-friendly.  

---

## 🔗 **Useful Links**  
- 📚 **[Chainlit Documentation](https://docs.chainlit.io)** - Comprehensive resources to get started.  
- 💬 **[Chainlit Discord](https://discord.gg/k73SQ3FyUh)** - Join the community for support, collaboration, and project sharing!  
- 🌐 **[Ollama Official Website](https://ollama.ai)** - Learn more about Ollama and its offerings.  

---

## 💬 **Chatbot Use Cases**  
This chatbot is designed to:  
- **Provide Expert Answers**: Deliver detailed, accurate responses based on the **Encyclopedia of Human Development**.  
- **Simplify Knowledge Access**: Allow users to easily explore and understand topics related to human development.  
- **Support Learning and Research**: Assist students, educators, and researchers with contextual insights from a reliable source.  

---

## 🚀 **Getting Started**  
Follow these steps to set up and run the chatbot locally:  

### **Prerequisites**  
- **Python 3.7+** - Ensure Python is installed.  
- **Ollama 3.1** - Download and install from [Ollama's official site](https://www.ollama.ai).  

---

### 🛠️ **Installation**  

1. **Clone the repository:**  
   ```shell  
   git clone https://github.com/mattzuha/Chainlit-Chatbot.git  
   cd TestChat4  
   ```  

2. **Install dependencies:**  
   ```shell  
   pip install -r requirements.txt  
   ```  

3. **Start Ollama Model:**  
   ```shell  
   ollama run llama 3.1  
   ```  

### ⚙️ **Setting Up the Vector Database**  
For document-based interactions, run the following command to ingest documents and create a vector database:  
```shell  
python ingest.py  
```  

---

### 🖥️ **Running Locally**  
Start the chatbot by running:  
```shell  
chainlit run model.py  
```  

---

## 🎥 **YouTube Demo**  
Check out our chatbot in action on **YouTube**: [Demo Link](https://www.youtube.com/watch?v=z0TeFWldKLk)  

---

## 👤 **Authors**  
- **10421091 - Nguyen Nguyen Minh**  
- **10421114 - Nguyen Khanh Hoang Minh**  

---  

🎉 **We hope you enjoy using this chatbot! Happy coding!** 💻😊  
