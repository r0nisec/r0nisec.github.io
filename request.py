import http.client

# Define the request headers
headers = {
    'Host': 'www.etoro.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers'
}

# Set verbose mode (True to show headers, False to hide)
verbose_mode = True

# Establish a connection to the server
connection = http.client.HTTPSConnection('www.etoro.com')

# Send the GET request
connection.request('GET', '/login', headers=headers)

# Get the response
response = connection.getresponse()

if verbose_mode:
    # Print the request headers
    print("Request Headers:")
    for header, value in headers.items():
        print(f"{header}: {value}")

    # Print a separator
    print("\n" + "=" * 50 + "\n")

    # Print the response headers
    print(f"Response Status: {response.status} {response.reason}")
    print("Response Headers:")
    for header, value in response.getheaders():
        print(f"{header}: {value}")

    # Print a separator
    print("\n" + "=" * 50 + "\n")

# Read and print the response body (if needed)
response_data = response.read()
print("Response Body:")
print(response_data.decode('utf-8'))

# Close the connection
connection.close()
