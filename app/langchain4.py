from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.llms import OpenAI

api_key = "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"
llm = OpenAI(model_name="text-davinci-003", openai_api_key=api_key)
# llm = OpenAI(model_name="gpt-3.5-turbo-0613", openai_api_key=api_key)
template = "示例输入:{input}\n示例输出:{output}"
example_prompt = PromptTemplate(input_variables=["input", "output"],
                                template=template)

examples = [
    {"input": "海盗", "output": "船"},
    {"input": "飞行员", "output": "飞机"},
    {"input": "驾驶员", "output": "汽车"},
    {"input": "树", "output": "地面"},
    {"input": "鸟", "output": "鸟巢"},
]

# examples = [
#     {"input": "中国", "output": "亚洲"},
#     {"input": "美国", "output": "美洲"},
#     {"input": "法国", "output": "欧洲"},
# ]

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples, OpenAIEmbeddings(openai_api_key=api_key), FAISS, k=3
)
similar_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="根据下列示例，写出输出",
    suffix="输入:{noun}\n输出:",
    input_variables={"noun"},
)

my_noun = "学生"

print(similar_prompt.format(noun=my_noun))
print(llm(similar_prompt.format(noun=my_noun)))
