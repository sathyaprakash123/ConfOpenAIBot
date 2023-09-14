# ConfOpenAIBot

Bot is designed to provide troubleshooting steps for Confluence issues based on knowledge gathered from KBs.

1. Knowledge_source.txt is a text file that contains urls of possible Confluence KBs that can help troubleshoot an issue
2. Source is a text file, that contains all the text data extracted from the links from knowledge_source.txt
3. knowledge_collector.py is the python script that extracts data and stores it in a specic path
4. ConfAPI.py is the python script that receives the query from user and uses the data from the above files to provide a topic specific response. The syntax of usage is : python3 ConfAPI.py "user query about confluence"

   **Pre-requisites**
Install the following libraries. Python might request installation of more libraries while running the script, do please install them as well

1. Install Python3 version: 3.11.3
2. pip3 install langchain
3. pip3 install beautifulsoup4
