
import json
import time
import urllib.request
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.page import Page

access_token = ''
app_secret = ''
app_id = ''
PAGE_ID = ''

FacebookAdsApi.init(access_token=access_token)

page = Page(PAGE_ID)

with open('posts.json', 'r') as f:
    posts = json.load(f)

for post in posts:
    try:
        image_name = 'image.jpg'
        urllib.request.urlretrieve(post['photo_url'], image_name)

        page.create_photo(
            image=open(image_name, 'rb'),
            message=post['message'],
            published=True
        )

        time.sleep(60)

    except Exception as e:
        print(f'Ошибка публикации сообщения в Facebook: {e}')
