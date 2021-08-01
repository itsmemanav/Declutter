# This Script will organize the Downloads folder and move the files into their respective sub-directories.

import os
import shutil


def main():
    HOME = os.path.expanduser("~")
    os.chdir(f"{HOME}{os.path.sep}Downloads")

    map_ext_to_dir = {
        ".png": "Pictures",
        ".jpg": "Pictures",
        ".jpeg": "Pictures",
        ".svg": "Pictures",
        ".pdf": "Documents",
        ".xlsx": "Documents",
        ".csv": "Documents",
        ".docx": "Documents",
        ".mp4": "Videos",
        ".mkv": "Videos",
        ".mp3": "Music",
        ".iso": "Programs",
        ".exe": "Programs",
        ".7z": "Compressed",
        ".zip": "Compressed"
    }

    for content in os.listdir():
        if os.path.isfile(content):
            ext = os.path.splitext(content)[1].lower()

            if ext in map_ext_to_dir.keys():
                tgt_dir_basename = map_ext_to_dir[ext]
                tgt_dir_abspath = f"{os.getcwd()}{os.path.sep}{tgt_dir_basename}"

                # Create sub-directory if it doesn't exist
                if not os.path.isdir(tgt_dir_basename):
                    os.mkdir(tgt_dir_abspath)

                try:
                    shutil.move(content, tgt_dir_abspath)
                except FileNotFoundError as err:
                    print(err)


if __name__ == "__main__":
    main()
