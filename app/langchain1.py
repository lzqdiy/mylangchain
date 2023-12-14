from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

api_key = "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"

chat = ChatOpenAI(temperature=0.7, openai_api_key=api_key)
result = chat(
    [
        SystemMessage(content="你是一个很棒的点餐机器人，可以帮助用户在一个简短的句子中弄清楚应该吃什么"),
        HumanMessage(content="我喜欢西红柿，我应该吃什么？"),
    ]
)
print(result)
