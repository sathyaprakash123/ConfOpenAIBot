# ConfOpenAIBot

Bot is designed to provide troubleshooting steps for Confluence issues based on knowledge gathered from KBs.

1. Knowledge_source.txt is a text file that contains urls of possible Confluence KBs that can help troubleshoot an issue
2. Source is a folder, that contains all the text data extracted from the links from knowledge_source.txt
3. knowledge_collector.py is the python script that extracts data and stores it under the source folder as text files
4. ConfAPI.py is the python script that receives the query from user and uses the data from the source folder to provide a topic specific response. The syntax of usage is : python3 ConfAPI.py "user query about confluence"

 **Pre-requisites**
Install the following libraries. Python might request installation of more libraries while running the script, do please install them as well

1. Install Python3 version: 3.11.3
2. pip3 install langchain
3. pip3 install beautifulsoup4
4. pip3 install openai
5. pip3 install unstructured
6. pip3 install chromadb
7. pip3 install tiktoken
8. pip3 install flask

Or check the requirements.txt

Steps to run:

1. Ensure that the path location from ConfAPI.py, line number 32 points to the source folder on your local machine
2. Ensure that the path location from knowledge_collector.py, line 40, points to the source folder on the local machine (same location as above)
3. run python3 knowledge_collector.py so that data is gathered and stored under source folder
4. You can then ask any query such as : python3 ConfAPI "confluence is slow" 

Using flask:
1. If there are no files under the source directory, run knowledge collector.py to generate them
2. export your OPENAI API Key:
export OPENAI_API_KEY=<your_key>
3. Change directory to the root of the project (The director that contains app.py)
4. Start the flask server:
python3 app.py
5. Open a browser and navigate to localhost:5000
http://127.0.0.1:5000/
6. Ask your question . . . . 