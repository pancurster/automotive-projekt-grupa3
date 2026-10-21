#!/usr/bin/env python3
import zipfile
from pathlib import Path

def unzip_raw_data(zip_file_path, destination_path):
    """
    Unzip archive. Return paths list of extracted files.
    """
    src = Path(zip_file_path)
    dst = Path(destination_path)

    if not src.exists():
        print(f'Path {src} does not exists!')
        return []
    if not dst.exists():
        print(f'Path {dst} does not exists!')
        return []

    z = zipfile.ZipFile(src)
    z.extractall(dst)
    extracted_files = [dst / Path(f.filename) for f in z.filelist]
    return extracted_files

