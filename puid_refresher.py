import time
from threading import Thread
from config import session

def refresh_puid_cookie():
    global puid
    url = "https://chat.openai.com/backend-api/models"
    initial_cookie = {"_puid": puid}

    while True:
        response = session.get(url, cookies=initial_cookie)

        if response.status_code != 200:
            print("Error:", response.status_code)
            print(response.text)
            break

        print("Got response:", response.status_code)

        puid_cookie = response.cookies.get("_puid")
        if puid_cookie:
            puid = puid_cookie
            print("Puid set:", puid)

        time.sleep(6 * 3600)

    print("Error: Failed to refresh puid cookie")

Thread(target=refresh_puid_cookie).start()
