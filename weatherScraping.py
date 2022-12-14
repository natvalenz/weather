import requests
from bs4 import BeautifulSoup

#Extract and print the first forecast item
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.5237&lon=-117.2164#.YzoVO3ZlBD8")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

#The name of the forecast item
period = tonight.find(class_="period-name").get_text()
#The description of the conditions
#A short description of the conditions
short_desc = tonight.find(class_="short-desc").get_text()
#The temperature low 
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

#extract the title attribute from the img tag
# treat the BeautifulSoup object like a dictionary, and pass in the attribute we want as a key
img = tonight.find("img")
desc = img['title']
print(desc)

# Extracting all the information from the page
# Select all items with the class period-name inside an item with the class tombstone-container in seven_day.
# Use a list comprehension to call the get_text method on each BeautifulSoup object.

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)

#same technique as above to get the other three fields
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)