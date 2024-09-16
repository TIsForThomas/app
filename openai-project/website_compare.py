import openai
import requests
from bs4 import BeautifulSoup

# Function to extract text from a webpage
def get_website_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract text from paragraphs
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])
    return text[:2000]  # Limiting to the first 2000 characters to avoid too much data

# Function to get the summary and comparison from OpenAI
def compare_websites(url1, url2):
    content1 = get_website_content(url1)
    content2 = get_website_content(url2)

    prompt = f"Compare these two websites based on the following content:\n\nWebsite 1: {content1}\n\nWebsite 2: {content2}\n\nGive a detailed comparison with strengths and weaknesses."

    # OpenAI API call
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=300,
      temperature=0.7
    )
    
    return response.choices[0].text

# Example URLs to compare
url1 = "https://rustoria.co/servers"
url2 = "https://moose.gg/moose"

# Compare the websites
comparison = compare_websites(url1, url2)
print(comparison)
