import pandas as pd

from ._models import WatchEvent
from ._utils import extract_watch_events, parse_iso_duration
from ._youtube import YouTube


class WatchHistory:
    """
    Manage your personal YouTube watch history.

    Pass your Google Takeout watch-history.html and an API key, and this class
    will enrich your complete history and provide ways to explore statistics.

    Example usage:
        Create an instance of youtube_history_explorer.WatchHistory:

            >>> import youtube_history_explorer as yhe
            >>> history = yhe.WatchHistory(watch_history='contents of watch-history.html')

        Quickly list the number of watch events in your history:

            >>> len(history)

        Enrich history with content details and statistics:

            >>> history.fetch_details(api_key='your api key')
    """
    def __init__(self, watch_history):
        self.events = extract_watch_events(watch_history)
        self.youtube = YouTube()

    def __len__(self):
        return len(self.events)

    def fetch_details(self, api_key):
        """
        Retrieve content details for all WatchEvents.

        Details will be stored in the WatchEvent instances themselves.
        """
        self.youtube.fetch(self.events, api_key)

    def get_watchtime_per_period(self, period='D'):
        df = pd.DataFrame([[e.timestamp, parse_iso_duration(e.content_details.duration)] for e in self.events if e.content_details], columns=['timestamp', 'watchtime']).set_index('timestamp')
        g = df.groupby(pd.Grouper(freq=period))
        return g.sum()
