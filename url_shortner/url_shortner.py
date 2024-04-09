from typing import Final
import requests

# Constants --> Final keyword input as [str]
API_KEY = 'YOUR_KEY'
BASE_URL = 'https://cutt.ly/api/api.php'


# Function to shorten any link with a custom name
def shorten_link(full_link): #will return string
    payload: dict = {'key': API_KEY, 'short': full_link, }
    request = requests.get(BASE_URL, params=payload)
    data = request.json() #dictionary format or ': dict'

    # Gets the relevant information we need
    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print('Link:', short_link)
        else:
            print('Error status:', url_data['status'])


def main():
    # Take user input
    link: str = input('Enter a link: ')

    # Shorten the link
    shorten_link(link)


if __name__ == '__main__':
    main()
