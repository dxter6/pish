import os, bs4, requests
b = input("enter the site")
a = int(input("""enter the Attacks(1::Raw content,2::page-status-code,3::pretty-Html,4::clones the website in your desktop):"""))
page = requests.get(b)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
if a == 1:
    print(page.content)
if a == 2:
    print(page.status_code)
if a == 3:
    print(soup.prettify())
if a == 4:
    Html_file=open("hello.html","w")
    Html_file.write(soup.prettify())
    Html_file.close
