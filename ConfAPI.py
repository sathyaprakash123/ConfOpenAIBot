# Need this library to set environment parameters to connect to OPEN API
import os

# Need this to get query from the user so that it can be read from command line
import sys

# Getting constant values such as the OpenAI key
import constants

# Lang chain library that can look at a folder full of files for training data
from langchain.document_loaders import DirectoryLoader

# Library to create indexing out of the data collected from folder for faster access
from langchain.indexes import VectorstoreIndexCreator

from langchain.llms import OpenAI

#Library for chat model for human like response
from langchain.chat_models import ChatOpenAI

from pathlib import Path
from urllib.request import urlopen

# Reading the open API Key from constants
os.environ["OPENAI_API_KEY"] = constants.APIKEY

#Getting the query from the system parameters
query = sys.argv[1]
print("The query is :", query)

#Letting the directory loader to read data from source
loader = DirectoryLoader("/Users/sganeshan/Documents/ConfSupportBot/ConfOpenAIBot/source", glob="*.txt")

# Setting indexing on the text data collected
index = VectorstoreIndexCreator().from_loaders([loader])

#Printing the query response from Chatbot
print(index.query(query, llm=ChatOpenAI()))
