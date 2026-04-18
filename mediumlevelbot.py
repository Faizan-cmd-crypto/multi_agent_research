from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()


messages = [
]

prompt = ChatPromptTemplate.from_messages([
    "system","you are a sad AI, you have to give response in sad way.",
    MessagesPlaceholder(variable_name="chat_history"),
    "human", "{user_input}"
])

model = ChatGroq(model="llama-3.3-70b-versatile")
print("Press 0 to exist")
while True:
    user = input("You :")
    if user == '0':
        break
    else:
        formatted_messages = prompt.format_messages(
            chat_history=messages,
            user_input=user
        )
        
        response = model.invoke(formatted_messages)
        messages.append(HumanMessage(content=user))
        messages.append(AIMessage(content=response.content))
        
        print("AI:",response.content) 