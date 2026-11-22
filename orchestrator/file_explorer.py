from pathlib import Path

directory = Path("C:/Users/MICHAEL/Documents/GitHub/ai-development-environment")

def list_files(directory: Path):
    print(f"Listing files in directory: {directory}")
    results = []
    for item in directory.iterdir():
        if item.is_file():
            results.append(f"File: {item.name}")
        elif item.is_dir():
            results.append(f"Directory: {item.name}")

    return results

print(list_files(directory))