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
    star_or_review = 1 if sys.argv[len(sys.argv) - 1] == '/s' else 0 # 0 is reviews and 1 is stars; set to review by default
    query = "+".join(sys.argv[1:len(sys.argv)])
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
                stars = row.find(class_='tresults--rating').find(class_='rating')
                if review is not None and stars is not None:
                    link = row.find(class_='search-version--link').find('a')['href']
                    reviews[int(review.text)] = link

                    links = []

                    #dict can't store repeat keys
                    if stars['title'] not in star:
                        links.append(link)
                    else:
                        links = star[stars['title']]
                        links.append(link)

                    star[stars['title']] = links

                    review_numbers.append(int(review.text))
                    review_numbers.sort(reverse=True)

                    if stars['title'] not in star_numbers:
                        star_numbers.append(stars['title'])
                        star_numbers.sort(reverse=True)


    if star_or_review is 0: # sort by reviews
        for num in range(0,3):
            valid_links.append(reviews[review_numbers[num]])
    else:
        total = 0
        for num in range(0,3):
            if num < len(star_numbers):
                n = star_numbers[num]
                if len(star[str(n)]) >= 3:
                    i = 0
                    while total < 3:
                        valid_links.append(star[str(n)][i])
                        i = i + 1
                        total = total + 1
                else:
                    i = 0
                    while total < 3:
                        if i < len(star[str(n)]):
                            valid_links.append(star[str(n)][i])
                            total = total + 1
                            i = i + 1
                        else:
                            break;
            else:
                break;

    print(valid_links)
else:
    print("Usage: tab <song and/or artist> <sort by stars or reviews>")
