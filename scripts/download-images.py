"""Download figures we keep in Google Drive.

Delete the local file to force a re-download.
"""

from pathlib import Path
from urllib.request import urlretrieve

FIGURES = {
    "https://drive.google.com/uc?export=download&id=16r5xE7SguunLfMh5LhSynSUfjb7IXs_n": "shared_responsibility_diagram.png",
}

for url, filename in FIGURES.items():
    path_image = Path(__file__).parent.parent / "images" / filename
    if not path_image.exists():
        print(f"Downloading {filename}...")
        urlretrieve(url, path_image)
    else:
        print(f"Figure exists, delete this file to re-download: {path_image}")
