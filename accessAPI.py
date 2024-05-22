import requests
import json

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

def retrieve_summary(book, chapter):
    # Construct the URL for the API call
    url = f"{base_url}{book}/{chapter}"
    
    # Send a GET request to the API and store the response
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the summary from the JSON response
        data = response.json()
        summary = data.get('summary', 'Summary not found')
        
        # Print the summary
        print(f"Summary of {book} chapter {chapter}:")
        print(summary)
    else:
        print(f"Failed to retrieve summary. Status code: {response.status_code}")

def main():
    print("Welcome to the Book of Mormon Summary Tool!")
    
    # Ask the user for the book and chapter
    book = input("Which book of the Book of Mormon would you like? ")
    chapter = input(f"Which chapter of {book} are you interested in? ")
    
    # Retrieve and print the summary
    retrieve_summary(book.lower(), chapter)

    # Ask if the user wants to view another summary
    choice = input("Would you like to view another (Y/N)? ").upper()
    if choice == 'N':
        print("Thank you for using Book of Mormon Summary Tool!")

if __name__ == "__main__":
    main()
