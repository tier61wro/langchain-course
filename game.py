from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from prompts.game import game_templates, human_prompt
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=1,
    timeout=(10, 120),
    max_retries=0
)

# history = []
history = InMemoryChatMessageHistory()


while True:
    user_input = input("🙋‍♂️ Сообщение: ")

    # human_text = human_prompt.format_messages(text=user_input)
    human_message = HumanMessage(content=user_input)
    messages = game_templates.format_messages() + history.messages + [human_message]
    response = model.invoke(messages)

    print("Бот: 🤖", response.text)

    history.add_message(human_message)
    history.add_message(AIMessage(content=response.content))

    # print("\n=== HISTORY ===")
    # for message in history:
    #     print("----")
    #     print(type(message).__name__, ":", message.content)
    # print("\n=== HISTORY END ===")

    if "угадал" in user_input.lower():
        history.clear()