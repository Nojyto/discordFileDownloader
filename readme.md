# Discord attachment downloader

Downloads all file attachments from a discord channel great for archiving memes.

## Usage

- Use [DiscordChatExporter]("https://github.com/Tyrrrz/DiscordChatExporter") to get a .json file.
- Name it as **messages.json** and place it next to the main.py.
- Run main.py
- Files will be place in **output** folder and named with 0000-9999 style.

## Notes

- Thread capability.
- Changeble constant variable base on preferences.

```python
OUTPUT_DIR = "output"
INPUT_FILENAME = "messages.json"
MAX_THREADS = 100
```
