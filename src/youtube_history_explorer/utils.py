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
            # Pattern group will contain 11 characters that immediately follow "watch?v="
            video_id = re.search(r'(?<=watch\?v=).{11}', m_text).group()
        except:
            print('Failed to find video_id in:')
            print(m_text)
            continue
        try:
            # Of the form: Apr 7, 2022, 5:18:48 PM CEST (for English language exports)
            datetime_str = re.search(r'(... \d{1,2}, \d{4}, \d{1,2}:\d\d:\d\d .. [A-Z]+)', m_text).group()
        except:
            print('Failed to find datetime string in:')
            print(m_text)
            datetime_str = ''

        # Attempt to parse datetime string
        # For now, the only format to attempt is
        # '%b %d, %Y, %I:%M:%S %p %Z'
        formats = ['%b %d, %Y, %I:%M:%S %p %Z']

        try:
            datetime_stamp = datetime.datetime.strptime(datetime_str, formats[0])
        except ValueError:
            print(f'Failed to parse "{datetime_str}" according to {formats[0]}')
            datetime_stamp = None

        events.append(WatchEvent(video_id, datetime_stamp))

    return events


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
