import asyncio
from datetime import date
from urllib.parse import urlencode, urlsplit, SplitResult
import json

def SplitURL(query: dict) -> SplitResult:
    URL = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"
    return urlsplit(f"{URL}?{urlencode(query)}")

async def RequestCountOfSubmittedDocuments(date_: date):
    url = SplitURL({"date": date_})
    reader, writer = await asyncio.open_connection(url.hostname, 443, ssl=True)
    req = f"GET {url.path}?{url.query} HTTP/1.0\n" f"Host: {url.hostname}\n" f"\n"
    writer.write(req.encode("latin-1"))
    resp = await reader.read()
    writer.close()
    parsed = json.loads(resp.split(b"\r\n\r\n")[-1])
    return parsed["metadata"]["resultset"]["count"]

async def main():
    counts = await asyncio.gather(
        *(
            RequestCountOfSubmittedDocuments(date_)
            for date_ in (
                date(2020, 9, 1),
                date(2020, 10, 10),
                date(2020, 11, 20),
            )
        )
    )
    print(*counts, sep="\n")

asyncio.run(main())