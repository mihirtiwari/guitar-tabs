import sys, requests, os
from bs4 import BeautifulSoup

if len(sys.argv) > 1:
    # by default will be locating in user's home directory
    directory = os.path.expanduser('~') + '/' + raw_input("Which directory would you like to put the tabs in? ")
    while os.path.isdir(directory) is False:
        print('Invalid path given.')
        directory = os.path.expanduser('~') + '/' + raw_input("Which directory would you like to put the tabs in? ")

    star_or_review = 1 if sys.argv[len(sys.argv) - 1] == '/s' else 0 # 0 is reviews and 1 is stars; set to review by default
    query = "+".join(sys.argv[1:len(sys.argv)])
    url = 'https://www.ultimate-guitar.com/search.php?search_type=title&order=&value='

    result = requests.get(url + query)

    if 'No matches' and 'No results' in result.text:
        print('No tabs were found!')
    else:
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
            num_tabs = 0
            for num in review_numbers:
                if num_tabs < 3:
                    valid_links.append(reviews[num])
                    num_tabs = num_tabs + 1
                else:
                    break
        else:
            total = 0
            for n in star_numbers:
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

        # start link scraping
        for links in valid_links:
            url = links
            result = requests.get(url)
            soup = BeautifulSoup(result.content, 'html.parser')

            tab = soup.find(class_="js-tab-content").text
            stripped_url = url[len('https://tabs.ultimate-guitar.com/')+ 2:]
            tab_title = stripped_url[stripped_url.find('/') + 1: stripped_url.find('.htm')].title()

            file_name = directory + '/' + tab_title + '.txt'

            tab_file = open(file_name, 'w')

            tab_file.write(tab)

            tab_file.close()

        print('Done! Your tabs can be found at -> ' + os.path.abspath(directory))

else:
    print("Usage: tab <song and/or artist> <sort by stars or reviews>")
