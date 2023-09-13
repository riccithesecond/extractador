import requests
from bs4 import BeautifulSoup

def extract_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                links.append(href)
        
        return links
    except Exception as e:
        return [f"Error: {str(e)}"]

def main():
    website_url = input("Enter the URL of the website: ")
    
    links = extract_links(website_url)

    if not links:
        print("No links found on the website.")
    elif "Error" in links[0]:
        print(f"Unable to fetch links. Error: {links[0]}")
    else:
        print("\nLinks on the website:")
        for link in links:
            print(link)

if __name__ == "__main__":
    main()
