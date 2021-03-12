import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
from time import sleep
import os, sys, shutil, subprocess
import zipfile

class ChromeSearch(unittest.TestCase):

   def setUp(self):
      download_directory = ("/Users/liathe.najdawi/Documents/Test/Downloads")
      options = webdriver.ChromeOptions()
      #Chrome preferences
      profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
           "download.default_directory": download_directory , 
           "download.extensions_to_open": "applications/pdf","download.prompt_for_download": False}
      options.add_experimental_option("prefs", profile)


      # Takes the directory where file is downloaded and Cleans it and prepare for the new download
      for filename in os.listdir(download_directory):
         file_path = os.path.join(download_directory, filename)
         try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                  os.unlink(file_path)
            elif os.path.isdir(file_path):
                  shutil.rmtree(file_path)
         except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

      #Creates anew folder where the .zip gets unzipped and labels it the browser version
      global path
      path = ("/Users/liathe.najdawi/Documents/Test/Downloads/89")
      try:
         os.mkdir(path)
      except OSError:
         print ("Creation of the directory %s failed" % path)
      else:
         print ("Successfully created the directory %s " % path)

      self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options  ) 

   

   def test_search_in_python_org(self):
      driver = self.driver
      driver.get("https://chromeenterprise.google/browser/download/")
      print(driver.title)
      driver.find_element_by_xpath('//*[@id="win64Bundle"]/div[2]/a').click()
      
      driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/a').click()

      #Download process Checks to make sure nothing is in the Directory and will continue to Install until download is Complete
      print("Waiting for downloads")
      while any([filename.endswith("") for filename in 
               os.listdir("/Users/liathe.najdawi/Documents/Test/Downloads")]):
         time.sleep(2)
         print(".")

         if filename.endswith (".zip"):
            print("DOWNLOAD COMPLETE")
            print("NOW EXTRACTING")

            # Takes the .zip file and unzips it to global variabel path
            with zipfile.ZipFile('/Users/liathe.najdawi/Documents/Test/Downloads/GoogleChromeEnterpriseBundle64.zip', 'r') as zip_ref:
               zip_ref.extractall(path)
            
            print("DOWNLOAD HAS BEEN EXTTACTED")

            subprocess.Popen("/Users/liathe.najdawi/Documents/Test/Downloads/89/Installers/GoogleChromeStandaloneEnterprise64.msi", shell=True)

            break
            driver.close()

            
      else:
         time.sleep(2)
         print("Waiting for downloads")




if __name__ == "__main__":
   unittest.main()
