import requests
import os
import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"] 
    return embedding


jsons = os.listdir("jsons")  # read all jsons file
my_dicts = [] # created an empty dictionary
chunk_id = 0 # initialise chck_id as zero

for json_file in jsons: # iterate all the jsons files
    with open(f"jsons/{json_file}") as f: # read the content of all jsons files one by one
        content = json.load(f)     # python dict name content will store the chunks and text
    print(f"Creating Embeddings for {json_file}") #print for each file to know the status
    embeddings = create_embedding([c['text'] for c in content['chunks']]) #bulk mai saare text ko ek list bana ke bhej diya -- we are creating embeddings here
       
    for i, chunk in enumerate(content['chunks']): #Iterate all the chunks
        chunk['chunk_id'] = chunk_id #Add chunk id to all the chunks
        chunk['embedding'] = embeddings[i] #Add embeddings 
        chunk_id += 1
        my_dicts.append(chunk) #We got the dictionary
# print(my_dicts)
   

df = pd.DataFrame.from_records(my_dicts) # Creating dataframes from the dictionary
#Save this dataframe
joblib.dump(df,'embeddings.joblib')
