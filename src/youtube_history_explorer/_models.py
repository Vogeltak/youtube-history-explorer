from dataclasses import dataclass, field
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
        self.content_details = None
        self.snippet = None
        self.statistics = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VideoContentDetails:
    """
    A dataclass to represent the video content detail information.

    See https://developers.google.com/youtube/v3/docs/videos#contentDetails
    """
    duration: str = field(default=None, repr=False)
    dimension: str = field(default=None, repr=False)
    definition: str = field(default=None, repr=False)
    caption: str = field(default=None, repr=False)
    licensed_content: bool = field(default=None, repr=False)
    # NOTE:
    # Leaving out "region_restriction" and "content_rating", because those are
    # more complex objects that we do not really need right now.
    # See python-youtube (https://github.com/sns-sdks/python-youtube) if you
    # require a comprehensive API wrapper.
    projection: str = field(default=None, repr=False)
    has_custom_thumbnail: bool = field(default=None, repr=False)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VideoSnippet:
    """
    A dataclass to represent the video snippet information.

    See https://developers.google.com/youtube/v3/docs/videos#snippet
    """
    published_at: str = field(default=None, repr=False)
    channel_id: str = field(default=None, repr=False)
    title: str = field(default=None, repr=False)
    description: str = field(default=None, repr=False)
    # NOTE:
    # Leaving out "thumbnails" and "localized", because those are more complex
    # objects that we do not really need right now.
    tags: list[str] = field(default=None, repr=False)
    category_id: str = field(default=None, repr=False)
    live_broadcast_content: str = field(default=None, repr=False)
    default_language: str = field(default=None, repr=False)
    default_audio_language: str = field(default=None, repr=False)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class VideoStatistics:
    """
    A dataclass to represent the video statistics information.

    See https://developers.google.com/youtube/v3/docs/videos#statistics
    """
    view_count: int = field(default=None, repr=False)
    like_count: int = field(default=None, repr=False)
    dislike_count: int = field(default=None, repr=False)
    favorite_count: int = field(default=None, repr=False)
    comment_count: int = field(default=None, repr=False)
