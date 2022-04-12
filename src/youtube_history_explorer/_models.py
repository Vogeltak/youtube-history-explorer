from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


class WatchEvent:
    """
    Represent the event of watching a video.

    A WatchEvent is identified by the following two-tuple:
        - video id
        - datetime stamp

    An instance can be extended with video parts for content details, snippet
    information, and statistics.
    """
    def __init__(self, video_id, timestamp):
        self.video_id = video_id
        self.timestamp = timestamp


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VideoContentDetails:
    """
    A dataclass to represent the video content detail information.

    See https://developers.google.com/youtube/v3/docs/videos#contentDetails
    """
    duration: str
    dimension: str
    definition: str
    caption: str
    licensed_content: bool
    # NOTE:
    # Leaving out "region_restriction" and "content_rating", because those are
    # more complex objects that we do not really need right now.
    # See python-youtube (https://github.com/sns-sdks/python-youtube) if you
    # require a comprehensive API wrapper.
    projection: str
    has_custom_thumbnail: bool


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VideoSnippet:
    """
    A dataclass to represent the video snippet information.

    See https://developers.google.com/youtube/v3/docs/videos#snippet
    """
    published_at: str
    channel_id: str
    title: str
    description: str
    # NOTE:
    # Leaving out "thumbnails" and "localized", because those are more complex
    # objects that we do not really need right now.
    tags: list[str]
    category_id: str
    live_broadcast_content: str
    default_language: str
    default_audio_language: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VideoStatistics:
    """
    A dataclass to represent the video statistics information.

    See https://developers.google.com/youtube/v3/docs/videos#statistics
    """
    view_count: int
    like_count: int
    dislike_count: int
    favorite_count: int
    comment_count: int
