# Import libraries
import requests
from bs4 import BeautifulSoup

# https://stackoverflow.com/questions/43470535/python-download-pdf-embedded-in-a-page

# URL from which pdfs to be downloaded
url = "https://services.datasport.com/2014/lauf/zuerich/alfab.htm"
# url = "http://www.datasport.com/jump/16913/7081/pu/dipl.htm"
# url = "https://www.datasport.com/en/diploma/?racenr=16913&stnr=7081"
#url = "https://www.datasport.com/sys/diplom/diplomservice.htm?payload=494D20B660F0EC48D4FE7B01E0D5D7FE48D7600532DDE8766A3001DBC1FF7B32AFBB01B2F0DDCDD25A47C05B8947217DA83C27264A499B394D7BE3672111C3E2411388AB75A7C24902C342F769A5CEDC53AFB413593432E7EA03BA084907D98F0589C923B86A8268297BE34FCD072ADAB716D29FAA4AFF8B220B4BDBED370F5E"

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')

i = 0

# From all links check for pdf link and
# if present download file
for link in links:
    if ('.pdf' in link.get('href', [])):
        i += 1
        print("Downloading file: ", i)

        # Get response object for link
        response = requests.get(link.get('href'))

        # Write content in pdf file
        pdf = open("pdf"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")

print("All PDF files downloaded")