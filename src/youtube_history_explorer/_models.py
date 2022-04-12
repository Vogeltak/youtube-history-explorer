class WatchEvent(object):
    """
    Represent the event of watching a video.

    A WatchEvent is identified by the following two-tuple:
        - video id
        - datetime stamp
    """
    def __init__(self, video_id, timestamp):
        self.video_id = video_id
        self.timestamp = timestamp
