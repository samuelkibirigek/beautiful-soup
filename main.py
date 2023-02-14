from bs4 import BeautifulSoup
import lxml

# Reading the local html file.
with open("website.html", encoding="utf-8") as file:
    contents = file.read()

# creating the soup object.
soup = BeautifulSoup(contents, "lxml")

# Returning of a full tag code line eg title tag
# print(soup.title)

# Returning the tag name
tag_name = soup.title.name
# print(tag_name)

# Returning the text in the tag Option 1
tag_text = soup.title.getText()
# print(tag_text)

# Option 2
tag_text_2 = soup.title.string
# print(tag_text_2)

# Returning the first tag in html file with many of the specified tag
first_paragraph = soup.p
# print(first_paragraph)

# Returning all the tags in html file of specified type as a LIST
all_anchor_tags = soup.find_all("a")
# print(all_anchor_tags)

# Outputting the text in all the tags in the returned list
for tag in all_anchor_tags:
    text = tag.getText()
    # print(text)

# Outputting the links in all the the tags in the returned list
for tag in all_anchor_tags:
    link = tag.get("href")
    # print(link)

# targeting elements using class
headings = soup.find_all(name="h3", class_="heading")
# print(headings)

# select returns all the tags with the specified class while select_one returns only one
# targeting elements using id
name = soup.select_one("#name")
# print(name)

# targeting elements using class and select
headings2 = soup.select(".heading")
# print(headings2)

# using css selectors to specify elements
company_url = soup.select_one("p a")
print(company_url)

