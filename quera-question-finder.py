# Importing the libraries
from bs4 import BeautifulSoup
import requests
import html5lib

#Get first person and second person url from user.
first_url = input("Please enter first person profile url: ")
second_url = input("Please enter second person profile url: ")

# Make a GET request to fetch the raw HTML content
first_html_content = requests.get(first_url).text
second_html_content = requests.get(second_url).text

# Parse the html content
first_soup = BeautifulSoup(first_html_content, "html5lib")
second_soup = BeautifulSoup(second_html_content, "html5lib")


#We add solved questions by first person to this list later
list_of_first_person_solved_questions = []


#Iterate through all html tag in first_html_content
for link in first_soup.find_all("a"):
    try:
        #Because just problems have class attribiut with name of ui small blue label
        #program must just append tags with that conditions to list_of_first_person_solved_questions.
        if(link.get("class")[0] == "ui" and link.get("class")[1] == "small"):
            list_of_first_person_solved_questions.append(link.get("href"))
    except TypeError:
        pass

#Link of questions that first person didn't solved will go to this file
output_file = open("output.txt", 'w')

#Iterate through all a tag in second_html_content
for link in second_soup.find_all("a"):
    try:
        #Because just problems have class attribiut with name of ui small blue label
        #program must just check if tag with this conditions is not in list_of_first_person_solved_questions
        if(link.get("class")[0] == "ui" and link.get("class")[1] == "small"):
            if(link.get("href") not in list_of_first_person_solved_questions):
                #Write url to output file.
                output_file.write("https://quera.ir" + link.get("href") + "\n")
    except TypeError:
        pass

output_file.close()
