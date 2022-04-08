import re
import sys
import datetime


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
