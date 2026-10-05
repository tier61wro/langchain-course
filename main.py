from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from schemas.translates import TranslatedText

load_dotenv()

values = {
    "lang": "скандинавский",
    "text": input("введите текст: ")
}

template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template_file("prompts/system.txt", input_variables=['lang']),
    HumanMessagePromptTemplate.from_template(
        "Скажи '{text}' на трех языках"
    )
])

prompt = template.format_messages(**values)

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=1,
    timeout=(10, 120),
    max_retries=0
)

# structured_model = model.with_structured_output(TranslatedText, strict=True, include_raw=True)
structured_model = model.with_structured_output(TranslatedText, strict=True)

# response = model.invoke(prompt)

response = structured_model.invoke(prompt)


print("=== PARSED ===")
print(response["parsed"])

print("\n=== RAW CONTENT ===")
print(response["raw"].content)

print("\n=== RAW MESSAGE ===")
print(response["raw"])

print("\n=== PARSING ERROR ===")
print(response["parsing_error"])