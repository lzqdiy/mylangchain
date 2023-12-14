from langchain.llms import OpenAI

api_key = "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"
llm = OpenAI(model_name="gpt-3.5-turbo-0613", openai_api_key=api_key)

prompt = """
今天是星期一，明天是星期三，这个说法有什么问题吗？
"""

print(llm(prompt))
