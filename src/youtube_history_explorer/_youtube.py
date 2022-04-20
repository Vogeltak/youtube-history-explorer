import requests
from ._models import VideoContentDetails, VideoSnippet, VideoStatistics
from ._utils import log

class YouTube:
    """
    Fetch video data from YouTube Data API.
    """
    API_ENDPOINT = 'https://youtube.googleapis.com/youtube/v3/videos?part=snippet&part=contentDetails&part=statistics&key={}{}'

    def __init__(self, api_key=None):
        self._api_key = api_key

    def fetch(self, events, api_key=None):
        """
        Retrieve details for all IDs that occur in the list of WatchEvents.

        As of now, the parts of the YouTube Data API for video that are
        requested are snippet, contentDetails, and statistics. In the future,
        this could be made to be tweaked by the caller. Beware that it requires
        appropriate data classes in the models module.
        """
        if not api_key and not self.api_key:
            log('Error: could not find an API key', err=True)
            return

        if api_key:
            self._api_key = api_key

        for i in range(0, len(events), 50):
            i = min(i, len(events))
            j = min(i + 50, len(events))

            # Format multi-id API request
            # Experimental limit was found to be 50 per request
            id_url_params = ''.join([f'&id={x.video_id}' for x in events[i:j]])

            # Fetch content details for every video ID
            r = requests.get(self.API_ENDPOINT.format(self._api_key, id_url_params))

            for item in r.json().get('items'):
                for e in events:
                    if e.video_id == item.get('id'):
                        e.content_details = VideoContentDetails.from_dict(item.get('contentDetails'))
                        e.snippet = VideoSnippet.from_dict(item.get('snippet'))
                        e.statistics = VideoStatistics.from_dict(item.get('statistics'))
