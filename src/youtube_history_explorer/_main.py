import sys
import datetime
import json
import requests

from utils import parse_iso_duration

api_endpoint = 'https://youtube.googleapis.com/youtube/v3/videos?part=snippet&part=contentDetails&part=statistics{}&key={}'


def fetch(write_to_file=None):
    # Retrieve API key from secrets file
    with open('secrets.json', 'r') as f:
        secrets = json.load(f)

    if not secrets.get('api_key'):
        print('Error: could not find an API key in secrets.json')
        return

    # Retrieve list of video ID's from file
    with open('ids.txt', 'r') as f:
        ids = [x.strip() for x in f.readlines()]

    # Content details of videos
    videos = []

    for i in range(0, len(ids), 50):
        i = min(i, len(ids))
        j = min(i + 50, len(ids))

        # Format multi-id API request
        id_url_params = ''.join([f'&id={x}' for x in ids[i:j]])

        # Fetch content details for every video ID
        r = requests.get(api_endpoint.format(id_url_params, secrets.get('api_key')))

        videos += r.json().get('items')

    if write_to_file:
        with open(write_to_file, 'w') as f:
            f.write(json.dumps(videos))

    return videos


def total_duration(videos):
    """Sum up durations of all videos in provided list."""
    # Running total
    total = datetime.timedelta(seconds=0)

    for v in videos:
        duration = v.get('contentDetails').get('duration')
        try:
            delta = parse_iso_duration(duration)
            total += delta
        except ValueError:
            continue

    return total


def videos_longer_than(videos: list, duration: datetime.timedelta):
    """Find videos that are longer than a given duration."""
    candidates = []

    for v in videos:
        try:
            v_dur = parse_iso_duration(v['contentDetails']['duration'])
            if v_dur > duration:
                candidates.append(v)
        except ValueError:
            continue

    return candidates


def median(videos, statistic):
    # Extract statistic for all videos in list
    observations = []
    skipped = 0

    for v in videos:
        c = v['statistics'].get(statistic)
        if c:
            observations.append(c)
        else:
            skipped += 1

    print(f'{skipped} videos did not have {statistic} data')

    observations = sorted(observations)

    return observations[int(len(observations)/2)]

def main(read_from_file=None):
    if read_from_file:
        with open(read_from_file, 'r') as f:
            videos = json.load(f)
    else:
        videos = fetch(write_to_file='videos.json')

    total = total_duration(videos)
    
    print(f'Watched {len(videos)} videos for a total of {total}')

    print(f'Median view count is {median(videos, "viewCount")}')

    threshold = datetime.timedelta(hours=2, minutes=30)
    long_vids = videos_longer_than(videos, threshold)

    print(f'{len(long_vids)} videos are longer than {threshold} (for a total of {total_duration(long_vids)})')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(read_from_file=sys.argv[1])
    else:
        main()
