import requests

url = 'https://www.etoro.com/login'
headers = {
    'Cookie': 'eToroLocale=en-gb; __cflb=0N1X6nGeaLgXnvWY857hjBXJraZNcmBAJT7NYCNDyDfSHtHSTwSmXeuiSEZtGyAiLDG7F7h5gp1iTp4zSwbkztgk; _ga_B0NS054E7V=GS1.1.1693116490.2.1.1693116490.60.0.0; cf_clearance=G6i8HQVY9SZtgGRgKbAf2F2xtUdvmAM1C.O9siaZ1E0-1693116492-0-1-63248ffe.c3190eb7.3425d01e-0.2.1693116492; _gcl_au=1.1.1517120685.1693114333; __adal_id=7f34dea3-4f62-45e8-a281-7e6e7b968218.1693114333.3.1693116490.1693116490.58d09568-abcb-435c-a347-b2f30257e8ee; __adal_ca=so%3Dburpsuite%26me%3Dreferral%26ca%3Dreferral%26co%3Dhttp%253A%252F%252Fburpsuite%252F%26ke%3D%28not%2520set%29; __adal_cw=1693114333463; _scid=aa9be1e3-3c96-4821-a3bf-a9e30dfc01c7; _ga=GA1.2.956788614.1693114334; _gid=GA1.2.305573379.1693114335; _fbp=fb.1.1693114335814.1713048003; _sctr=1%7C1693072800000; etoroHPRedirect=1; intercom-device-id-x8o64ufr=252932ea-3b78-4613-a0b6-2e3c9d3630eb; __adal_ses=*; _scid_r=aa9be1e3-3c96-4821-a3bf-a9e30dfc01c7; mp_dbbd7bd9566da85f012f7ca5d8c6c944_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18a357d91e132a83-0e5552879c53da8-d535429-13c680-18a357d91e132a83%22%2C%22%24device_id%22%3A%20%2218a357d91e132a83-0e5552879c53da8-d535429-13c680-18a357d91e132a83%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _uetsid=7ddcb9c0449411ee93f23f5600319e93; _uetvid=364d3d10090c11ee8e17b156b7d40047',
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

response = requests.get(url, headers=headers)

# Display response headers
print("Response Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")
