import os
from json import load
from requests import get
from multiprocessing.pool import ThreadPool


OUTPUT_DIR = "output"
INPUT_FILENAME = "messages.json"
MAX_THREADS = 100


def downloadFile(dat):
    if os.path.exists(dat["dir"]):
        return

    r = get(dat["url"])
    with open(dat["dir"], 'wb') as f:
        f.write(r.content)


if __name__ == "__main__":
    urls = []

    with open(INPUT_FILENAME, encoding="utf8") as inputFile:
        data = load(inputFile)
        fileCount = 0

        for msg in data["messages"]:
            for atch in msg["attachments"]:
                name = atch["fileName"]
                ext = '.' + name.split(".")[-1]

                newFileName = str(fileCount).zfill(4) + ext
                newFileDir = os.path.join(OUTPUT_DIR, newFileName)

                urls.append(
                    {"url": atch["url"], "dir": newFileDir, "name": newFileName})
                fileCount += 1

    fileCount = len(urls)
    if fileCount == 0:
        exit("No attachments were found. Exiting...")

    if not os.path.isfile(INPUT_FILENAME):
        exit(f"{INPUT_FILENAME} was not found. Exiting...")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    input(f"Found {fileCount} files. Press any key to start download...")
    with ThreadPool(MAX_THREADS) as p:
        p.map(downloadFile, urls)
    print("Download finished.")
