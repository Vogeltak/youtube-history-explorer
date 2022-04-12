import requests

class YouTube:
    """
    Fetch video data from YouTube Data API.
    """
    API_ENDPOINT = 'https://youtube.googleapis.com/youtube/v3/videos'

    def __init__(self, api_key):
        self._api_key = api_key
