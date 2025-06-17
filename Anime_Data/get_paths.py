from pathlib import Path
import json



def get_paths(path):
    
    config_path = Path(__file__).parent.parent / "config.json"
    with open(config_path, 'r') as f:
        data = json.load(f)
        
        suffixs = data['suffixs']
    
    paths = [
        str(file.resolve())
        for file in Path(path).iterdir()
        if file.suffix in suffixs
    ]
    
    if not paths:
        Season = 1
        
        
        
        paths = [
            str(file.resolve())
            for file in Path(path).iterdir()
            if file.is_dir()
        ]
    else:
        Season = 2
        
        
    return paths , Season