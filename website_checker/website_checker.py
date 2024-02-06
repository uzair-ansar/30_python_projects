import csv
import requests
from http import HTTPStatus
from fake_useragent import UserAgent


def get_websites(csv_path):
    """Load websites from csv file"""

    websites = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
    return websites


def get_user_agent():
    """Returns a user agent that can be used with requests"""

    ua = UserAgent()
    return ua.chrome


def get_status_description(status_code):
    """Uses the status code to return a readable description"""

    for value in HTTPStatus:
        if value == status_code:
            description = f'({value} {value.name}) {value.description}'
            return description
    return '(???) Unknown status code'


def check_website(website, user_agent):
    """Gets the status code for a website and prints teh result"""

    try:
        code = requests.get(website, headers={'User_Agent': user_agent}).status_code
        print(website, get_status_description(code))
    except Exception:
        print(f'***Could not get information for website: {website}')


def main():
    sites = get_websites('websites.csv')
    user_agent = get_user_agent()

    # check websites
    for i, site in enumerate(sites):
        check_website(site, user_agent)


if __name__ == '__main__':
    main()
