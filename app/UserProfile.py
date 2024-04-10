import json
import requests
import time
class UserProfile:
    def __init__(self,name,id,profile_picture_URL,session):
        self.name=name
        self.id=id
        self.profile_picture_URL=profile_picture_URL
        self.session=session
    def getFollowers(self):
        #returns a list of UserProfile that follow id
        res=[]
        url = f'https://spclient.wg.spotify.com/user-profile-view/v3/profile/{self.id}/followers?market=DE'
        headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en',
        'App-Platform': 'WebPlayer',
        'Authorization': f'Bearer {self.session.bearerAuth}',
        'Client-Token': self.session.client_token,
        'Dnt': '1',
        'Origin': 'https://open.spotify.com',
        'Referer': 'https://open.spotify.com/',
        'Sec-Ch-Ua': '"Chromium";v="123", "Not:A-Brand";v="8"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Spotify-App-Version': self.session.client_version,
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
                        profile['image_url'],
                        self.session)
                    )
                else:#no profile picture
                    res.append(UserProfile(
                        profile['name'],
                        uri[2],
                        "https://t4.ftcdn.net/jpg/02/15/84/43/360_F_215844325_ttX9YiIIyeaR7Ne6EaLLjMAmy4GvPC69.jpg",
                        self.session)
                    )
            except KeyError:
                print("Error parsing proile")
        return res
