from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage(content="you are a sad AI, you have to give response in sad way.")
]

model = ChatGroq(model="llama-3.3-70b-versatile")
print("Press 0 to exist")
while True:
    user = input("You :")
    messages.append(HumanMessage(user))
    if user == '0':
        break
    else:
        response = model.invoke(messages)
        messages.append(response)
        print("AI:",response.content)