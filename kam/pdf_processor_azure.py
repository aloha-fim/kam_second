
import os
import re
import requests
import sys
from num2words import num2words
import os
import pandas as pd
import numpy as np
import tiktoken
from openai import AzureOpenAI
import json
import requests
import pandas as pd
import csv
import ast
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
  azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT"),
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),
  api_version = "2024-06-01",
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)

#df = pd.read_csv("./data/postdefined_users_azure_data_v4.csv")


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_embedding(text, model="text-embedding-ada-002"): # model = "deployment_name"
    return client.embeddings.create(input = [text], model=model).data[0].embedding

def search_docs(df, user_query, top_n=5, to_print=True):
    embedding = get_embedding(
        user_query,
        model="text-embedding-ada-002" # model should be set to the deployment name you chose when you deployed the text-embedding-ada-002 (Version 2) model
    )
    # Editing of embedding
    #df['ada_v2'] = df['ada_v2'].str[1:3000].tolist()

    #df['ada_v2'] = df['ada_v2'].str[:1000] + "]"

    # https://anupampawar.com/2024/04/03/ufuncnolooperror-ufunc-multiply-did-not-contain-a-loop-with-signature-matching-types/
    # Convert embeddings from string format back to numpy array
    #df['ada_v2'] = df['ada_v2'].apply(lambda x: np.array(ast.literal_eval(x)))
    # https://atoonk.medium.com/diving-into-ai-an-exploration-of-embeddings-and-vector-databases-a7611c4ec063
    df['ada_v2'] = df['ada_v2'].apply(eval).apply(np.array)

    df["similarities"] = df.ada_v2.apply(lambda x: cosine_similarity(x, embedding))

    response = (
        df[['full_name','quote','similarities']].sort_values("similarities", ascending=False)
        .head(top_n)
    )

    return response




