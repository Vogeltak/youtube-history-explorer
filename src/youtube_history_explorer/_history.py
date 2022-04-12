from ._models import WatchEvent
from ._utils import extract_watch_events
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
    def __init__(self, watch_history, api_key=None):
        self.events = extract_watch_events(watch_history)
        self.api_key = api_key

    def __len__(self):
        return len(self.events)

    def fetch_details(api_key=None):
        """
        Retrieve content details for all WatchEvents.

        Details will be stored in the WatchEvent instances themselves.
        """
