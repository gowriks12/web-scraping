from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get("https://allevents.in/atlanta/today?ref=home-page").text
soup = BeautifulSoup(html_text, 'lxml')
# all_events = soup.find_all('div', class_ = 'resgrid-row')
# all_events = soup.find_all('li', class_ = 'item event-item box-link f')
container = soup.find_all('ul', class_ = 'resgrid-ul')
# print(container)
all_events = soup.find_all('li', class_ = 'item event-item f box-link')
all_events.extend(soup.find_all('li', class_ ='item event-item box-link'))
# for events in all_events:
#     event = events.find_all('li', class_ = 'item event-item f box-link')
for i, e in enumerate(all_events):
    month = e.find('span', class_ = 'up-month')
    date = e.find('span', class_ = 'up-day')
    name = e.find('h3').text
    print("Name: ", name)
    venue = e.find('span', class_ = "up-venue toh").text.strip()
    try:
        t = e.find('span', class_ = 'tick-price').text.strip()
    except:
        t = "Unavailable"
    with open(f'posts/{i}.txt', 'w') as f:
        f.write(f'Event Name: {name}\nEvent Location:{venue}\nEvent Date: {month.text} {date.text}\nTicket Price:{t}\n')

    # print(event)
