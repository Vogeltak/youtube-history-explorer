# YouTube History Explorer

The YouTube History Explorer—YHE for short—is a small Python project to interactively explore your YouTube watch history. It draws from a Google Takeout of your data and the YouTube Data API for enriched information.

Its aim is to provide you with the tools to interact with your YouTube watch history and create metrics and reports on statistics you care about.

## Quickstart

1. Download from PyPI
   ```sh
   pip install youtube-history-explorer
   ```
2. Import the package (e.g., in an interactive Python interpreter)
   ```python
   import youtube_history_explorer as yhe
   ```
3. Create a `WatchHistory` object from the Google Takout html export
   ```python
   with open('watch-history.html', 'r') as f:
       data = f.read()

   history = yhe.WatchHistory(data)
   ```

## License

MIT License
Copyright (c) 2022 Max Crone

See [LICENSE](LICENSE).

This package draws inspiration from excellent projects such as [httpx](https://github.com/encode/httpx), and everything from [pallets](https://github.com/pallets) really.
