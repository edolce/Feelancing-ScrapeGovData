import requests
from twocaptcha import TwoCaptcha

import base64

if __name__ == '__main__':


    # decode base64 string data
    decoded_data = base64.b64decode("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")
    # write the decoded data back to original format in  file
    img_file = open('image.jpeg', 'wb')
    img_file.write(decoded_data)
    img_file.close()

    import easyocr

    reader = easyocr.Reader(['en'])
    result = reader.readtext('image.jpg', detail=0)
    print(result)


def test():
    headers0 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://electoralsearch.eci.gov.in',
        'Referer': 'https://electoralsearch.eci.gov.in/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0',
        'appName': 'ELECTORAL_SEARCH',
        'sec-ch-ua': '"Opera";v="99", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    response = requests.get("https://gateway.eci.gov.in/api/v1/captcha-service/generateCaptcha",headers=headers0)

    base64 = response.json()["captcha"]
    captchaId = response.json()["id"]

    solver = TwoCaptcha("8e4d3a745d75dc4a4461b1f7d891c636")
    captcha_id = solver.normal(base64)["code"]

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://electoralsearch.eci.gov.in',
        'Referer': 'https://electoralsearch.eci.gov.in/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0',
        'applicationName': 'ELECTORAL_SEARCH',
        'sec-ch-ua': '"Opera";v="99", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    print(captcha_id)

    json_data = {
        "captchaData": captcha_id,
        "captchaId": captchaId,
        "epicNumber": "RMP7954993",
        "isPortal": True,
        "securityKey": "na"
    }

    print(response.cookies)

    response2 = requests.post(
        'https://gateway.eci.gov.in/api/v1/elastic/search-by-epic-from-national-display',
        headers=headers,
        json=json_data,
        cookies=response.cookies.get_dict()
    )
    print(response2.json())
    print(response2.status_code)

# def solve_captcha(api_key, site_key, url):
#     solver = TwoCaptcha(api_key)
#
#     try:
#         # Get the captcha solution using 2captcha service
#         captcha_id = solver.solve_captcha(site_key=site_key, url=url)
#         print("Captcha solved successfully!")
#         # Poll for the captcha solution
#         response = None
#         while response is None:
#             response = solver.get_captcha_result(captcha_id)
#             if response['status'] == 1:
#                 return response['code']
#             elif response['status'] == 2:
#                 print("Captcha is not ready yet. Waiting...")
#             else:
#                 print("Captcha solving failed.")
#                 break
#
#     except Exception as e:
#         print(f"Error occurred: {str(e)}")
#         return None
#
# # Replace these with your actual 2captcha API key, site key, and the URL with the captcha
# API_KEY = "YOUR_2CAPTCHA_API_KEY"
# SITE_KEY = "CAPTCHA_SITE_KEY"
# URL_WITH_CAPTCHA = "URL_WITH_CAPTCHA"
#
# captcha_response = solve_captcha(API_KEY, SITE_KEY, URL_WITH_CAPTCHA)
# if captcha_response:
#     # Use the captcha response in your HTTP request
#     data = {
#         # Your request data here...
#         'captcha_response': captcha_response,
#         # Other parameters...
#     }
#
#     response = requests.post('YOUR_REQUEST_URL', data=data)
#     print(response.text)
