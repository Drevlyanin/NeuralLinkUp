
import facebook 
import requests


app_id = 'YOUR_APP_ID'
app_secret = 'YOUR_APP_SECRET'
access_token = app_id + '|' + app_secret

graph = facebook.GraphAPI(access_token=access_token, version="12.0")
graph.put_photo(image=open('image.jpg', 'rb'), message='text')

try:
    post_id = graph.put_photo(image=open('image.jpg', 'rb'), message='text')
    if post_id:
        print('error')
except Exception as e:
    print(f"Error: {e}")
