import requests 
s = requests.Session()

def request():
    headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer BQCRRPk6TRvvKEkLmOcI1aVbKllqbWiZa2o4jz_Qk2JHltxFwynxzzqmWLZhA7gOR0EhMNd1wmUIi_zhpz3l9rxYcAAWuHx39f_msPOqJN91RZ2c4NI',
    'Sec-Fetch-Site': 'same-site',
    'Accept-Language': 'en-GB',
    'Sec-Fetch-Mode': 'cors',
    'Host': 'spclient.wg.spotify.com',
    'Origin': 'https://open.spotify.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
    'Referer': 'https://open.spotify.com/',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'spotify-app-version': '1.2.35.387.gd3ea0cba',
    'app-platform': 'WebPlayer',
    'Priority': 'u=3, i',
    'client-token': 'AADhb170OuF6JwOOs5RkGeNW8BPJuDszA3RSkLGDpjawyIlTzhFINHDJPoEeHcujUcD15Vw5ktw49YdMpWXtbQrtt8bPB+S96yHkkn4crwuOya5mPn+Y4wk2YzHFAae/ucWEtsipu/QPrT4GuhE+G6Lvx6V9SJsQFxdu53Q6LLRebq5G8R6vgwxDA9uS4CMMQbi21L90PcfXhc2j/kPMd7PE13iLxjHAlVkgh5DcJg8zk0xYvSOoLgjeNIq52TEfHJNNmNE2fTrUxy1OwCwfWc4JtvASng5Xi4Y7K8SMn1AnhtHPaSfTVcml3dkent/gR1mb9dKchleTDg==',
    }

    params = {
        'market': 'CH',
    }

    req = s.get(
        'https://spclient.wg.spotify.com/user-profile-view/v3/profile/81s0j2853r21a3jdqh2zzqsyz/followers',
        params=params,
        headers=headers,
    )
    print(req.text)
    print(req.status_code)



if __name__ == "__main__":
    print('test')
    request()