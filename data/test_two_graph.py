#https://stackoverflow.com/questions/43470535/python-download-pdf-embedded-in-a-page

from selenium import webdriver
from time import sleep

def download_pdf(lnk):

    options = webdriver.ChromeOptions()

    download_folder = "./data"

    profile = {"plugins.plugins_list": [{"enabled": False,
                                         "name": "Chrome PDF Viewer"}],
               "download.default_directory": download_folder,
               "download.extensions_to_open": "",
               "plugins.always_open_pdf_externally": True}

    options.add_experimental_option("prefs", profile)

    print("Downloading file from link: {}".format(lnk))

    driver = webdriver.Chrome(options = options)
    driver.get(lnk)

    filename = lnk.split("/")[5].split(".htm")[0]
    print("File: {}".format(filename))

    print("Status: Download Complete.")
    print("Folder: {}".format(download_folder))

    driver.close()


download_pdf("https://www.datasport.com/en/diploma/?racenr=16913&stnr=1100")