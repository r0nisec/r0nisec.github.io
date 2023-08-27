#!/bin/bash

# The HTTP request headers
request_headers=$(cat <<EOF
Host: www.etoro.com
Cookie: ... (your cookie values here)
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Te: trailers
EOF
)

# The URL to request
url="https://www.etoro.com/login"

# Create temporary files for storing request and response
request_file=$(mktemp)
response_file=$(mktemp)

# Use curl to send the request and save response
curl -v -s -o "$response_file" -H "$request_headers" "$url"

# Display the request headers
echo "Request Headers:"
echo "----------------"
echo -e "$request_headers\n"

# Display the response headers
echo "Response Headers:"
echo "-----------------"
sed -n '/^< /q;p' "$response_file"

# Display the response body
echo -e "\nResponse Body:"
echo "--------------"
sed '1,/^$/d' "$response_file"

# Clean up temporary files
rm "$request_file" "$response_file"
