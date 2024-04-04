import json
import requests
import time
class UserProfile:
    def __init__(self,name,id,profile_picture_URL):
        self.name=name
        self.id=id
        self.profile_picture_URL=profile_picture_URL
    def getFollowers(self):
        #returns a list of UserProfile that follow id
        res=[]
        url = f'https://spclient.wg.spotify.com/user-profile-view/v3/profile/{self.id}/followers?market=DE'
        headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en',
        'App-Platform': 'WebPlayer',
        'Authorization': 'Bearer BQAPKao6JKNWVPVggPLX72D386fuy4fM7cnsbnOnUxTg-VHO3G2BCWAtehX0G4_XwgyAewNSEq9UMTnw1crfA4dlTkqN8AdGIcgyjzmBxv3HVz9srsY',
        'Client-Token': 'AABhi4+l3X2xAtpQflj76vHtbdQ91WFNlG7AG4MTTpNlDG4OKIe6t0r1qDv4wExZqiLwTfiyJtl3hWKhwazYKQC/zOa597ina4MLnxdRuMAZ1lDiqfWAGRqJP47CKZRWROBtjU9GLu7jJNoZlpXQBx5Vm2zCSfz9iLdTrhh8+wHC/0yN+A5vxWkeX2UOP7cnRsduOD6dF4R4xxnxLnpcsrC2qmx1+ggjjy0rzmfJi+77R3wBk9MCc4pPOYroaosC6FI0Gt0+WKVymu1aQbtZ5X3R8PU1CXDw+yCbf7sL8r1XpxLfJNPDzMyYpmD9LueSh2Ybu3ckI0Wi',
        'Dnt': '1',
        'Origin': 'https://open.spotify.com',
        'Referer': 'https://open.spotify.com/',
        'Sec-Ch-Ua': '"Chromium";v="123", "Not:A-Brand";v="8"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Spotify-App-Version': '1.2.35.405.gd0b3e5e6',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
        response = requests.get(url, headers=headers)
        time.sleep(1)
        print(response.text)
        data= json.loads(response.text)
        if 'profiles' not in data:
            return []
        profiles=data['profiles']
        for profile in profiles:
            uri=profile['uri'].split(":")
            try:
                if 'image_url' in profile:
                    res.append(UserProfile(
                        profile['name'],
                        uri[2],
                        profile['image_url'])
                    )
                else:#no profile picture
                    res.append(UserProfile(
                        profile['name'],
                        uri[2],
                        "https://t4.ftcdn.net/jpg/02/15/84/43/360_F_215844325_ttX9YiIIyeaR7Ne6EaLLjMAmy4GvPC69.jpg")
                    )
            except KeyError:
                print("Error parsing proile")
        return res