from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    HumanMessage,   # Что мы хотим от модели
    SystemMessage,  # Как модель должна себя вести
)

from langchain_core.prompts import ()

load_dotenv()

text = input("введите текст:")
task_template = f"скажи {text} тремя способами на польском"


model = ChatOpenAI(
    model = "gpt-5-nano",
    temperature = 1,
    # timeout = 5,
)

response = model.invoke(
    [
        # SystemMessage(content="ты учитель польского языка в университете"),
        # SystemMessage(content="ты польский гопник"),

        SystemMessage(
            content="""
            Ты молодой польский уличный хулиган.
            Говори максимально разговорно, используй польский сленг,
            молодёжные выражения и уличную лексику.
            Не используй учебниковые и формальные выражения.
            """
        ),

        HumanMessage(content="скажи Привет по польски тремя способами")

    ]
)

# response = model.invoke("Объясни в одном предложении, что такое LangChain.")


print(response.response_metadata)
print(response.content)