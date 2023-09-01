import os
import sys
import constants

from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from pathlib import Path
from urllib.request import urlopen

os.environ["OPENAI_API_KEY"] = constants.APIKEY
query = sys.argv[1]
print("The query is :", query)

loader = DirectoryLoader("/Users/sganeshan/Documents/ConfSupportBot/ConfOpenAIBot/source", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])
print(index.query(query, llm=ChatOpenAI()))
