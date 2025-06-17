from pathlib import Path


def get_season_paths(paths):
    b_path = []
    for folder in paths:
        for file in Path(folder).iterdir():
            if file.is_file():
                b_path.append(str(file.resolve()))
    return [file for file in b_path if Path(file).suffix == ".mkv"]