import httpx
from flask import jsonify, Response
from config import session, puid

def proxy(request, path):
    url = f"https://chat.openai.com/backend-api/{path}"
    req_puid = request.headers.get("Puid")

    headers = {
        "Host": "chat.openai.com",
        "Origin": "https://chat.openai.com/chat",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Keep-Alive": "timeout=360",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Authorization": request.headers.get("Authorization")
    }

    cookies = {"_puid": req_puid or puid}


    try:
        response = session.request(request.method, url, headers=headers, data=request.data, params=request.args, cookies=cookies)
    except httpx.RequestError as e:
        return jsonify({"error": str(e)}), 500

    content_type = response.headers.get("Content-Type", "application/json")
    return Response(response.content, status=response.status_code, content_type=content_type)
