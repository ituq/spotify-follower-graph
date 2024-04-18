#Session Object to make Requests to Spotify
import json
import requests
import re
class Session:
    def __init__(self):
        #fetch bearer auth
        try:
            # Make the HTTP request to the URL
            response = requests.get('https://open.spotify.com')

            # Check if the response status is OK (200)
            if response.status_code != 200:
                raise Exception('Network response was not ok')

            # Get the HTML text content from the response
            my_html_content = response.text

            # Find the start of the accessToken in the HTML content
            access_token_start = my_html_content.find("accessToken") + 14

            # Get the accessToken from the content
            access_token = my_html_content[access_token_start:access_token_start + 115]
            print(f'bearerAuth:{access_token}')
            self.bearerAuth= access_token
        except Exception as e:
            print(f'Problem fetching bearer auth: {e}')
        ####################################################################
        #fetch client ID & app version
        #header to request html
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Dnt': '1',
            'Pragma': 'no-cache',
            'Referer': 'https://open.spotify.com/',
            'Sec-Ch-Ua': '"Chromium";v="123", "Not:A-Brand";v="8"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }
        # Send a GET request to the URL
        response = requests.get('https://open.spotify.com',headers=headers)

        # Check if the response was successful
        if response.status_code != 200:
            raise Exception('Network response was not ok')

        # Get the text content from the response
        html_content = response.text
        # find script to get ID and version from
        script_url_pattern = r'https://open\.spotifycdn\.com/cdn/build/web-player/web-player\.[a-zA-Z0-9]+\.js'
        script_url_match=re.search(script_url_pattern,html_content)
        script=requests.get(script_url_match.group(),headers=headers).text if script_url_match else "error"
        # Extract the clientId from the scipt
        ID_match=re.search(r'clientID:\s*\"([a-fA-F0-9]+)\"',script)
        client_id=ID_match.group() if ID_match else "Not found"
        #client_id is now of form 'clientID: "dmksacfjsndcasdocj"'
        extractPattern = r'"([^"]*)"'
        match=re.search(extractPattern,client_id)
        self.client_id=match.group(1) if match else "error"
        print(f'clientID:{self.client_id}')

        # Extract client version from script
        version_start_index=ID_match.start()+59 if ID_match else 0
        version=script[version_start_index:version_start_index+20]
        self.client_version = version
        print(f'clientVersion:{self.client_version}')
        #get client token
        url='https://clienttoken.spotify.com/v1/clienttoken'
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json',
            'Dnt': '1',
            'Origin': 'https://open.spotify.com',
            'Pragma': 'no-cache',
            'Referer': 'https://open.spotify.com/',
            'Sec-Ch-Ua': '"Chromium";v="123", "Not:A-Brand";v="8"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }
        payload = {
            "client_data": {
                "client_version": self.client_version,
                "client_id": self.client_id,
                "js_sdk_data": {
                    "device_brand": "Apple",
                    "device_model": "unknown",
                    "os": "macos",
                    "os_version": "10.15.7",
                    "device_id": "07b45f072b68c3f71e68610001a3b1ba",
                    "device_type": "computer"
                }
            }
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))

            if response.status_code != 200:
                error_body = response.text
                print(f'Request failed with status: {response.status_code} and body: {error_body}')
                raise Exception('Network response was not ok')

            response_data = response.json()
            print('client_token: '+response_data['granted_token']['token'])
            self.client_token=response_data['granted_token']['token']

        except Exception as e:
            print(f'Problem fetching client Token: {e}')
