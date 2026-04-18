from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

@tool
def send_email(to: str, subject: str, body: str) -> str:
    """Sends an email to the given recipient with a subject and body."""
    sender = "faizanahmad1127@gmail.com"
    password = "oojj fgff lrml xekm"
    msg = MIMEText(body)
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, to, msg.as_string())
    return "Email sent!"

load_dotenv()

history = []
model = ChatGroq(model="llama-3.3-70b-versatile")

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a precise summarizer.
Read the content and return:
- TL;DR (1-2 sentences)
- Key points (max 5 bullet points)
- Takeaway (1 sentence)
Keep language simple. Do not add opinions."""),
    ("human", "Summarize this:\n\n{user}")
])

search_tool = TavilySearchResults(max_results=5)  # fix 1: renamed to search_tool
parser = StrOutputParser()
chain = prompt | model | parser

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
    elif user.lower().startswith("send email"):
        to = input("To: ")
        subject = input("Subject: ")
        body = input("Body: ")
        result = send_email.invoke({"to": to, "subject": subject, "body": body})  # fix 2: .invoke()
        print(result)
    else:
        response = chain.invoke({"user": user})
        history.append(HumanMessage(content=user))
        history.append(AIMessage(content=response))
        print("AI:", response)