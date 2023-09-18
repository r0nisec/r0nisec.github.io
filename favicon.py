import mmh3
import requests
import codecs

# Prompt the user to enter the favicon icon URL
favicon_url = input("Enter the favicon icon URL: ")

# Send a request to retrieve the favicon.ico file
response = requests.get(favicon_url)

# Check if the request was successful
if response.status_code == 200:
    # Encode the content of the response using base64 encoding
    favicon = codecs.encode(response.content, "base64")
    
    # Calculate the MurmurHash3 hash value
    hash_value = mmh3.hash(favicon)
    
    # Print the hash value
    print("Hash:", hash_value)
else:
    print("Error: Failed to retrieve the favicon icon.")
