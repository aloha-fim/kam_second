from dotenv import load_dotenv
import os
#from PyPDF2 import PdfReader
#import docx
import json
import requests
import pandas as pd
import csv

from langchain.text_splitter import CharacterTextSplitter
# [deprecared] from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
# [deprecated] from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
# [deprecated] from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
# [deprecated] from langchain.callbacks import get_openai_callback
from langchain_community.callbacks import get_openai_callback
from langchain_community.document_loaders import JSONLoader, CSVLoader
# [deprecated] from langchain.document_loaders.csv_loader import CSVLoader
# from langchain_community.document_loaders import CSVLoader

# chroma
from langchain.schema import Document



load_dotenv()

#def read_pdf(file_path):
#    with open(file_path, "rb") as file:
#        pdf_reader = PdfReader(file)
#        text = ""
#        for page_num in range(len(pdf_reader.pages)):
#            text += pdf_reader.pages[page_num].extract_text()
#    return text


def read_json_chat():

    ########################################################################################
    ## Path 1 Production
    api_url = "https://kam-second.onrender.com/load_data"


    response = requests.get(api_url)

    data = response.json()

    # Convert data to dict
    # json_data = json.loads(response.text)

    # Convert dict to string
    json_data = json.dumps(data)

    return json_data


def process_json_query(query):
    #text = read_json_chat()
    #print(text)

    text = pd.read_csv("./data/postdefined_users.csv", index_col=0)

    # split into chunks
    char_text_splitter = CharacterTextSplitter(separator="\n", chunk_size=256,
                                               chunk_overlap=25, length_function=len)

    text_chunks = char_text_splitter.split_text(text)

    # create embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    docsearch = FAISS.from_texts(text_chunks, embeddings)

    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")

    # process user query
    docs = docsearch.similarity_search(query)

    # Adjust your code to include an 'input' dictionary
    input_data = {
        'input_documents': docs,
        'question': query,
    }

    # Now, pass the 'input_data' dictionary to the 'invoke' method
    response = chain.invoke(input=input_data)
    #response = chain.invoke(question=query, input_documents=docs)
    return response


def process_pdf_query(pdf_path, query):
    text_pdf = read_pdf(pdf_path)

    forvava_text = read_json_chat()

    text = text_pdf + forvava_text
    # split into chunks
    char_text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)

    text_chunks = char_text_splitter.split_text(text)

    # create embeddings
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(text_chunks, embeddings)

    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")

    # process user query
    docs = docsearch.similarity_search(query)

    # Adjust your code to include an 'input' dictionary
    input_data = {
        'input_documents': docs,
        'question': query,
    }

    # Now, pass the 'input_data' dictionary to the 'invoke' method
    response = chain.invoke(input=input_data)
    #response = chain.invoke(question=query, input_documents=docs)
    return response


def process_json_magic(query):
    ##### API route #####
    #text = read_json_chat()
    #print(text)

    ##### Langchain ######
    #loader = CSVLoader(file_path="./data/gpt_postdefined_users.csv", encoding = 'UTF-8')
    #text = loader.load()

    ##### Langchain output #####
    #text_load = loader.load()
    #text = text_load.page_content

    ##### pandas #####
    # Read the CSV file into a pandas DataFrame
    #df = pd.read_csv("./data/gpt_postdefined_users.csv")

    ##### Microsoft ######
    with open("./data/postdefined_users_gpt.csv", encoding = "ISO-8859-1") as file:
        reader = csv.reader(file, delimiter=",")
        text_reader = list(reader)

    # gpt rate limit of token
        text_limit = text_reader[:3000]

    # reading csv file
    #text = open("./data/postdefined_users_gpt.csv", "r")

    # turn list into string
    #    text = ' '.join([i for i in text])
        text = ' '.join(str(x) for x in text_limit)

    # replacing ',' by | for GPT
        text = text.replace(" ", " | ")


    # split into chunks
    char_text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000,
                                               chunk_overlap=200, length_function=len)

    text_chunks = char_text_splitter.split_text(text)

    # create embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    docsearch = FAISS.from_texts(text_chunks, embeddings)

    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")

    # process user query
    docs = docsearch.similarity_search(query)

    # Adjust your code to include an 'input' dictionary
    input_data = {
        'input_documents': docs,
        'question': query,
    }

    # Now, pass the 'input_data' dictionary to the 'invoke' method
    response = chain.invoke(input=input_data)
    #response = chain.invoke(question=query, input_documents=docs)
    return response


