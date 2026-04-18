from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from typing import List, Optional
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate([
    "system", "You are a good lyrics maker. You can make good song out of old and new orcaan makeyour own lyrics.",
    MessagesPlaceholder(variable_name="chat_history"),
    "human","{user_input}"
])

history = []


model = ChatGroq(model="llama-3.3-70b-versatile")

while True:
    user = input("You : ")
    if user == "0":
        break
    else:
        formatted_messages = prompt.format_messages(
            chat_history=history,
            user_input=user
        )
        
        response = model.invoke(formatted_messages)
        history.append(HumanMessage(content=user))
        history.append(AIMessage(content=response.content))
        
        print("AI : ",response.content)