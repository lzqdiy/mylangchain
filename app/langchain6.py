from langchain import OpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

api_key = "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"
llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo-0613", openai_api_key=api_key)

loader = TextLoader("./data/test.txt", encoding="utf-8")
doc = loader.load()
# print(f"You have {len(doc)} document")
# print(f"You have {len(doc[0].page_content)} chars in that document")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=200)
docs = text_splitter.split_documents(doc)

embeddings = OpenAIEmbeddings(openai_api_key=api_key)

dosearch = FAISS.from_documents(docs, embeddings)

qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=dosearch.as_retriever()
)

query = "武松打死了什么？"

result = qa.run(query)

print(result)
