from langchain_core import chat_history
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from rich import print
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

history = []

prompt = ChatPromptTemplate.from_messages([
    "system","You are a book summarizer assistant. You have to summarize book in 3 lines.",
    MessagesPlaceholder(variable_name="chat_history"),
    "human","{user_input}"
])

model = ChatGroq(model="llama-3.3-70b-versatile")

chain = prompt | model | StrOutputParser()

while True:
    user = input("You :")
    if user == "0":
        break
    else:
       history.append(("human",user))

       result = chain.invoke({"chat_history":history,"user_input":user})
       history.append(("ai",result))
       print("AI :",result)


