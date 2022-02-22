from pathlib import Path
from sys import argv
from shutil import move


def get_dir(filename):
    """
        This function takes filename and returns name of the
        parent directory of the respective filename
        Returns Miscellaneous if Parent is not found
    """
    ext = filename.suffix[1:]
    return dirs.get(ext, "Miscellaneous")


dirs = {
    # Images
    "jpeg": "Images",
    "png": "Images",
    "jpg": "Images",
    "tiff": "Images",
    "gif": "Images",

    # Videos
    "mp4": "Videos",
    "mkv": "Videos",
    "mov": "Videos",
    "webm": "Videos",
    "flv": "Videos",

    # Music
    "mp3": "Music",
    "ogg": "Music",
    "wav": "Music",
    "flac": "Music",

    # Program Files
    "py": "Program Files",
    "js": "Program Files",
    "cpp": "Program Files",
    "html": "Program Files",
    "css": "Program Files",
    "c": "Program Files",
    "sh": "Program Files",

    # Documents
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "ppt": "Documents",
    "ods": "Documents",
    "csv": "Documents"
}

if len(argv) != 2:
    print("=" * 35)
    print("[ERROR] Invalid number of arguments were given")
    print(f"[Usage] python {Path(__file__).name} <dir_path>")
    print("=" * 35)
    exit(1)

# Directory Path
PATH = Path(argv[1])

for filename in PATH.iterdir():

    path_to_file = filename.absolute()

    if path_to_file.is_file():
        destination = PATH / get_dir(filename)

        if not destination.exists():
            destination.mkdir()

        move(str(path_to_file), str(destination))