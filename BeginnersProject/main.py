from bs4 import BeautifulSoup;

with open("home.html", "r") as html_file:
  content = html_file.read()

  soup = BeautifulSoup(content, "lxml")
  #PRETTIFY
  #print(soup.prettify()) This instance can be use to prettify the HTML content.
  #FIND/FIND_ALL
  #find() / find_all() - tag = soup.find("h5") or courses_html_tags = soup.find_all("h5"). 
  course_cards = soup.find_all("div", class_="card")

  for course in course_cards:
    #Accessing HTML tags content.
    course_name = course.h5.text
    #Use of split method to access the price specifically.
    course_price = course.a.text.split()[-1]

    print(f"{course_name} costs {course_price}")