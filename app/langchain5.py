from langchain import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI

api_key = "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"
llm = OpenAI(model_name="text-davinci-003", openai_api_key=api_key)
response_schema = [
    ResponseSchema(name="bad_string", description="这是一个格式不正确的用户输入字符"),
    ResponseSchema(name="good_string", description="这是你的回复，重新格式化的回复"),
]

output_parse = StructuredOutputParser.from_response_schemas(response_schema)

format_instruction = output_parse.get_format_instructions(output_parse)

# print(format_instruction)

template = """
{format_instruction}
% 用户输入：
{user_input}
你的响应：
"""

prompt = PromptTemplate(
    input_variables=["user_input"],
    partial_variables={"format_instruction": format_instruction},
    template=template,
)

prompt_value = prompt.format(user_input="欢迎广州来到")

# print(prompt_value)

llm_out = llm(prompt_value)

print(llm_out)
