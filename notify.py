import requests
class LINENotifyBot:
    API_URL = "https://notify-api.line.me/api/notify"
    def __init__(self, access_token):
        self.headers = {'Authorization': 'Bearer ' + access_token}

    def send(self, message, image=None, sticker_package_id=None, sticker_id=None):
        message = '\n' + message
        payload = {
                'message': message,
                'stickerPackageId': sticker_package_id,
                'stickerId': sticker_id
            }
        files = {}
        if image != None:
            files = {'imageFile': open(image, 'rb')}
        r = requests.post(self.API_URL, headers=self.headers, data=payload, files=files)
