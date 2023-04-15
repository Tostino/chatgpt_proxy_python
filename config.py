import os
import httpx

port = int(os.environ.get("PORT", "8081"))
host = os.environ.get("HOST", "0.0.0.0")
access_token = os.environ.get("ACCESS_TOKEN")
puid = os.environ.get("PUID")
session = httpx.Client(timeout=360, cookies=httpx.Cookies(), follow_redirects=False)

if access_token is not None:
    print("Access token is set: ", access_token)
    session.headers.update({
        "Authorization": f"Bearer {access_token}",
        "Host": "chat.openai.com",
        "origin": "https://chat.openai.com/chat",
        "referer": "https://chat.openai.com/chat",
        "sec-ch-ua": 'Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110',
        "sec-ch-ua-platform": "Linux",
        "content-type": "application/json",
        "accept": "text/event-stream",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    })
