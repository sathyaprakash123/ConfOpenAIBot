# Module to extract data from KB links

from pathlib import Path
from urllib.request import urlopen
from bs4 import BeautifulSoup
import uuid

# Scraps data from all urls from the knowledge_source.txt file

print("## Knowledge Collector Called")
def knowledge_gather():
    print("## Calling Knowledge Gather")
    with open("knowledge_source.txt") as file:
        for url in file:
            print(url)
            gather_data_from_url(url)


# Scraps data from single KB
def gather_data_from_url(url):
    print("## Calling gather_data_from_url")


    #Cleans up the data from KB. Removes as much HTML noise as possible so that only the data text is storefd
    with urlopen(url) as response:
        body = response.read()

    soup = BeautifulSoup(body, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    print(text)
    dir_path = Path("/Users/sganeshan/Documents/ConfSupportBot/ConfOpenAIBot/source")
    file_path = dir_path.joinpath(str(uuid.uuid4()) + ".txt")
    if dir_path.is_dir():
        with open(file_path, "w") as f:
            f.write(text)
            print("File Created")
    else:
        print("Directory doesn\'t exist.")

# Calling knowledge gather, which will obtain the links from knowledge_source.txt one by one and extract the text content from these links and store them on data.txt
knowledge_gather()
