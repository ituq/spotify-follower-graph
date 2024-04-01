
from selenium import webdriver
from bs4 import BeautifulSoup
from pyvis.network import Network
import re
def getNameFromFollowerList(a_element):
    return a_element.find("p").find("span").text
def getFollowers(id,driver):
    url =f'https://open.spotify.com/user/{id}/followers'
    driver.get(url)

    driver.implicitly_wait(2)  # seconds

    html_content = driver.page_source

    soup = BeautifulSoup(html_content, 'html.parser')
    driver.quit()

    # Compile a regex pattern to match the desired href format
    pattern = re.compile(r'^/user/[a-zA-Z0-9]+')

    # Find all <a> elements with an 'href' attribute matching the pattern
    user_links = soup.find_all('a', href=pattern)
    return user_links
# Option to run Chrome in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome()

driver.quit()

net=Network()
net.show_buttons(filter_=['physics'])
net.add_node(0,"base")
for index, neigh in enumerate(user_links, start=1):
    net.add_node(index, getNameFromFollowerList(neigh))
    net.add_edge(index, 0)
net.show("basic.html")
getFollowers("test")





    





