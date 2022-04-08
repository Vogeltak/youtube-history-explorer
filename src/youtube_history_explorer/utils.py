import re
import datetime

from .models import WatchEvent


def extract_watch_events(watch_history):
    events = []

    div_pattern = 'class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"'
    matches = [m for m in re.finditer(div_pattern, watch_history)]

    for m in matches:
        m_len = watch_history[m.start():].find('</div>')
        m_text = watch_history[m.start():m.start()+m_len]
        try:
            video_id = re.search(r'(?<=watch\?v=).{11}', m_text).group()
            datetime_str = re.search(r'(... \d{1,2}, \d{4}, \d:\d\d:\d\d .. [A-Z]+)', m_text).group()
        except:
            print('Failed to find video_id or datetime in:')
            print(m_text)

    return []


def parse_iso_duration(iso_duration):
    """
    Parse an ISO 8601 time duration string into a datetime.timedelta instance.

    Args:
        iso_duration: an ISO 8601 time duration string
    Returns:
        a datetime.timedelta instance
    """
    m = re.match(r'^P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?$', iso_duration)
    if m is None:
        raise ValueError(f'Invalid ISO 8061 duration string: {iso_duration}')

    d = [int(n) if n else 0 for n in m.groups()]

    return datetime.timedelta(days=d[0], hours=d[1], minutes=d[2], seconds=d[3])
