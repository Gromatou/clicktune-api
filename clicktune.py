#you need to install :
#pip install selenium
#pip install beautifulsoup4
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
class clicktune:
    def __init__(self):
        chromeop = Options()
        chromeop.add_argument("--headless=new")  # Run Chrome in headless mode
        chromeop.add_argument(f"user-agent={"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}")  # Set the user-agent
        self.driver = webdriver.Chrome(chromeop)
        self.driver.get("https://www.clictune.com/links/index")
        self.driver.implicitly_wait(2)
        time.sleep(1)
        self.driver.find_element("name", "email").send_keys("exemple@gmail.com") #enter your clicktune email here
        time.sleep(1)
        self.driver.find_element("name", "password").send_keys("password") #enter your clicktune pasword here
        self.driver.find_element("name", "Connexion").click()
        time.sleep(5)
        self.driver.get("https://www.clictune.com/links/index")
        time.sleep(2)

    def add_links(self,listoflinks):
        linkform = self.driver.find_element("name", "link")
        for k in range (len(listoflinks)):
            linkform.send_keys(listoflinks[k])
            linkform.send_keys("\n")
        self.driver.find_element("name", "validate").click()
        soup = BeautifulSoup(self.driver.page_source, features="lxml")
        rows = soup.select('tr.pair, tr:not([class])')
        for row in rows:
            link_element = row.select_one('td:nth-of-type(3) a')
            if link_element:
                clictune_link = link_element.get('href')
                leboncoin_link_element = row.select_one('td:nth-of-type(3) span i')
                if leboncoin_link_element:
                    leboncoin_link = leboncoin_link_element.get_text()[:-1]
                    for j in range (len(listoflinks)):
                        if (listoflinks[j] == leboncoin_link):listoflinks[j] = clictune_link
        return listoflinks

##################################################################
#################### here exemple how to use #####################
##################################################################
exemple = clicktune()
listoflinks=["https://www.leboncoin.fr/recherche?text=remplier","https://www.leboncoin.fr/recherche?text=remplirraaa"] #enter your list of link here
print(exemple.add_links(listoflinks))



