from langchain import OpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader,UnstructuredHTMLLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.chat_models import ChatOpenAI

# llm = ChatOpenAI(model="gpt-3.5-turbo-0613")
llm = OpenAI(model_name="text-davinci-003")


# data_file_path = "./data/test_wusong.txt"
# data_file_path = "./data/test_likui.txt"
# data_file_path = "./data/test_taiwan.txt"
# data_file_path = "./data/test_xingfa.txt"
data_file_path = "app/data/output.html"

# loader = TextLoader(data_file_path, encoding="utf-8")
loader = UnstructuredHTMLLoader(data_file_path, encoding="utf-8")

doc = loader.load()
# print(f"doc:{doc}")
print(f"You have {len(doc)} document")
print(f"You have {len(doc[0].page_content)} characters in that document")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1900,
                                               chunk_overlap=0)
docs = text_splitter.split_documents(doc)

print(f'Now you have {len(docs)} documents')

embeddings = OpenAIEmbeddings()

dosearch = FAISS.from_documents(docs, embeddings)

chain_type = "refine"
# chain_type = "map_reduce"
# chain_type = "stuff"
qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type=chain_type, retriever=dosearch.as_retriever()
)

# query = "麻生太郎来台湾做什么了？"
# query = "武松做了什么？"
# query = "李逵做了什么？"
# query = "中华人民共和国刑法第三条是什么？"
query = "台風7号の動きは教えてください。"
# query = "请告诉我第7号台风的行进方向。"


result = qa.run(query)

print(f"human:{query}")

print(f"AI:{result}")
