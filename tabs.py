from splinter import Browser

browser = Browser()

url = 'https://www.ultimate-guitar.com/search.php?search_type=title&order=&value='

title = raw_input('What is the name of the song? ')

artist = raw_input('What is the name of the artist? ')

query = (title + '+' + artist).replace(" ", "+")

browser.visit(url + query.lower())

if browser.is_text_present('No matches'):
    print('Tab was unable to be found\n')
else:
    print('Tab exists')

browser.quit()
