import json, os

def readFile(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)
    
    with open(file_path, "r") as f:
        return json.load(f)
    
def writeFile(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)