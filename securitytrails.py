import sys
import requests

def fetch_dns_history(domain):
    url = f"https://api.securitytrails.com/v1/history/{domain}/dns/a?page=1"
    headers = {
        'APIKEY': '<API_KEY>',
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an exception if the request fails

        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == '__main__':
    if not sys.stdin.isatty():
        domain_name = sys.stdin.read().strip()
        dns_history = fetch_dns_history(domain_name)

        if dns_history is not None:
            ips = []

            for record in dns_history.get('records', []):
                values = record.get('values', [])
                for value in values:
                    ips.append(value.get('ip'))

            ips = list(set(ips))  # Remove duplicates
            ips.sort()  # Sort the IP addresses in ascending order

            for ip in ips:
                print(ip)
    else:
        print("No input received from pipe.")
