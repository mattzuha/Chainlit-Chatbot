from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOllama
from chainlit.types import ThreadDict
from typing import Optional
import chainlit as cl

# Path to the FAISS database for retrieval
DB_FAISS_PATH = "vectorstores/db_faiss"

# Custom prompt template for generating answers with context
custom_prompt_template = """Use the following pieces of information to answer the user's question. If you don't know the answer, please just say that you don't know the answer, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

# Function to set up the custom prompt template
def set_custom_prompt():
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
    return prompt

# Function to load the LLM model
def load_llm():
    llm = ChatOllama(
        model="llama3.1",
    )
    return llm

# Function to create a Conversational Retrieval QA chain with memory and a retriever
def retrieval_qa_chain(llm, prompt, db):
    # Define retriever with specific search parameters
    retriever = db.as_retriever(
        search_type='mmr',
        search_kwargs={'k': 2, 'fetch_k': 4}
    )

    # Setup memory to retain conversation context
    memory = ConversationBufferMemory(
        memory_key='chat_history',
        output_key='answer',
        return_messages=True
    )

    # Build the Conversational Retrieval QA Chain with LLM, retriever, and memory
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": prompt},
        verbose=True
    )

    return qa_chain

# Main function to initialize the bot with embedding model, FAISS database, and QA chain
def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)
    return qa

# Function to handle final response based on user query
def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response

### ChainLit ###

# Callback function to authenticate the user
@cl.password_auth_callback
def auth_callback(username: str, password: str) -> Optional[cl.User]:
    if (username, password) == ("admin", "admin"):
        return cl.User(identifier="admin")
    else:
        return None

# Function to initialize the bot and welcome the user
@cl.on_chat_start
async def start():
    chain = qa_bot()
    msg = cl.Message(content="Starting the bot....")
    await msg.send()
    msg.content = "Hi, Welcome to the Hi Bot. What is your query?"
    await msg.update()
    cl.user_session.set("chain", chain)

# Function to handle resuming a chat session
@cl.on_chat_resume
async def on_chat_resume(thread: ThreadDict):
    cl.user_session.set("chat_history", [])

    # Check if 'chain' exists in session, otherwise initialize
    if not cl.user_session.get("chain"):
        cl.user_session.set("chain", qa_bot())
    
    # Rebuild chat history from previous steps
    for message in thread["steps"]:
        if message["type"] == "user_message":
            cl.user_session.get("chat_history").append({"role": "user", "content": message["output"]})
        elif message["type"] == "assistant_message":
            cl.user_session.get("chat_history").append({"role": "assistant", "content": message["output"]})

# Function to handle incoming user messages and generate responses
@cl.on_message
async def main(message):
    chain = cl.user_session.get("chain")  # Retrieve the chain from the session
    
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    cb.answer_reached = True

    # Pass the extracted query to the chain and stream the result
    await chain.acall(message.content, callbacks=[cb])
