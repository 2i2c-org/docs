# Download figures we keep in Google Drive

from pathlib import Path
from requests import get
figures = {
    "https://drive.google.com/uc?export=download&id=1Mr51-s3D_KHPsAuTXbczaQ7mlPZUs9gm": "collaborative_learning_hub.png",
    "https://drive.google.com/uc?export=download&id=16r5xE7SguunLfMh5LhSynSUfjb7IXs_n": "shared_responsibility_diagram.png",
    "https://drive.google.com/uc?export=download&id=1gWAIQVKcB-uxuJsBHqlDlRTq88oki1zn": "scalable_research_hub.png",
}
for url, filename in figures.items():
    path_image = Path("../images").joinpath(filename)
    if not path_image.exists():
        print(f"Downloading {filename}...")
        resp = get(url)
        path_image.write_bytes(resp.content)
    else:
        print(f"Diagram image exists, delete this file to re-download: {path_image}")
