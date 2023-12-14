from langchain.llms import OpenAI
from langchain import PromptTemplate

api_key = "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"
llm = OpenAI(model_name="gpt-3.5-turbo-0613", openai_api_key=api_key)
template = """
我想去{location}旅游，我在哪里能做什么？
"""
prompt = PromptTemplate(input_variables=["location"], template=template)

final_prompt = prompt.format(location="沈阳")
print(llm(final_prompt))
