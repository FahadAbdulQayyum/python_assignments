# Web Scraping Program Python Project

import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)

# # # # # # # # # # # # # # # # # # # # # # 

# Web Scraping Program Python Project

import requests
from bs4 import BeautifulSoup as bs

# Input GitHub username
github_user = input('Input GitHub User: ')
url = f'https://github.com/{github_user}'

try:
    # Send a GET request to the GitHub profile page
    r = requests.get(url)
    
    # Check if the request was successful
    if r.status_code != 200:
        print(f"Error: Unable to fetch data for user '{github_user}'. Status code: {r.status_code}")
    else:
        # Parse the HTML content
        soup = bs(r.content, 'html.parser')
        
        # Find the profile image
        profile_image_tag = soup.find('img', {'alt': 'Avatar'})
        
        if profile_image_tag and 'src' in profile_image_tag.attrs:
            profile_image_url = profile_image_tag['src']
            print(f"Profile Image URL: {profile_image_url}")
        else:
            print(f"No profile image found for user '{github_user}'.")
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")