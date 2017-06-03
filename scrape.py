# from splinter import Browser
#
# browser = Browser()
#
# url = 'https://www.ultimate-guitar.com/search.php?search_type=title&order=&value='
#
# title = raw_input('What is the name of the song? ')
#
# artist = raw_input('What is the name of the artist? ')
#
# query = (title + '+' + artist).replace(" ", "+")
#
# browser.visit(url + query.lower())
#
# if browser.is_text_present('No matches'):
#     print('Tab was unable to be found\n')
# else:
#     print('Tab exists')
#
# browser.quit()
import sys, requests
from bs4 import BeautifulSoup

if len(sys.argv) > 1:
    query = "+".join(sys.argv[1:])
    url = 'https://www.ultimate-guitar.com/search.php?search_type=title&order=&value='

    result = requests.get(url + query)
    soup = BeautifulSoup(result.content, 'html.parser')

    tab_table = soup.find(class_='tresults')
    tab_row = tab_table.find_all('tr')

    valid_links = []
    reviews = {}
    star = {}
    review_numbers = []
    star_numbers = []

    for row in tab_row:
        for tab_type in row.find_all('strong'):
            if tab_type.text == 'tab':
                review = row.find(class_='tresults--rating').find('b')

                if review is not None:
                    reviews[int(review.text)] = row.find(class_='search-version--link').find('a')['href']

                    review_numbers.append(int(review.text))
                    review_numbers.sort(reverse=True)

                stars = row.find(class_='tresults--rating').find(class_='rating')
                if stars is not None:
                    star[str(stars['title'])] = row.find(class_='search-version--link').find('a')['href']
                    # print(stars['title'])
                    star_numbers.append(stars['title'])
                    star_numbers.sort(reverse=True)

    print(star)

    for num in range(0,3):
        valid_links.append(reviews[review_numbers[num]])

    # print(valid_links)
else:
    print("Usage: tab <song and/or artist>")
