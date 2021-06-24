from bs4 import BeautifulSoup
import requests
import time

#JOB ADS WEB SCRAPING PROJECT.
#Functionalities: filtering unfamiliar skills, runs app every 10 minutes, saves indexed .txt files in "posts" folder.

#Filtering out unfamiliar skills I don't posses. 
print("Put some skill you are not familiar with")
unfamiliar_skill = input(">")
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
  html_text = requests.get("https://es.indeed.com/ofertas?q=python&l=Espa%C3%B1a").text
  soup = BeautifulSoup(html_text, "lxml")
  jobs = soup.find_all("div", class_= "jobsearch-SerpJobCard")

  for index, job in enumerate(jobs):
    published_date = job.find("span", class_ = "date").text
    if "Recien publicado" in published_date or "Hoy" in published_date or "hace 1 día" in published_date or "hace 2 días" in published_date or "hace 3 días" in published_date or "hace 4 días" in published_date or "hace 5 días" in published_date or "hace 6 días" in published_date or "hace 7 días" in published_date:
      company_name = job.find("span", class_="company").text.replace(" ", "")
      requirements = job.find("div", class_="summary").text
      #To be able to display more_info, I needed to cut "/rc/clk" from the beginning of the string given by href and add "https..." in order to get to the redirected website.
      more_info = "https://es.indeed.com/ver-oferta" + job.h2.a['href'].strip("/rc/clk")
      if unfamiliar_skill not in requirements:
        with open(f"posts/{index}.txt", "w") as f:
          f.write(f"Company Name: {company_name.strip()} \n")
          f.write(f"Requirements: {requirements.strip()} \n")
          f.write(f"More Info: {more_info}")
        print(f"File saved as: {index}.txt")
    
if __name__ == "__main__":
  while True:
    find_jobs()
    time_wait = 10
    print(f"Waiting {time_wait} minutes...")
    time.sleep(time_wait * 60) #Allows the program to wait certain amount of time instead of running constantly.
