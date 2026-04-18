from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title("Medium Level Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = ChatPromptTemplate.from_messages([
    "system", "you are a sad AI, you have to give response in sad way.",
    MessagesPlaceholder(variable_name="chat_history"),
    "human", "{user_input}"
])

model = ChatGroq(model="llama-3.3-70b-versatile")

for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

if user := st.chat_input("You:"):
    with st.chat_message("user"):
        st.write(user)

    formatted_messages = prompt.format_messages(
        chat_history=st.session_state.messages,
        user_input=user
    )

    response = model.invoke(formatted_messages)

    with st.chat_message("assistant"):
        st.write(response.content)

    st.session_state.messages.append(HumanMessage(content=user))
    st.session_state.messages.append(AIMessage(content=response.content))
