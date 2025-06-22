def remove_virus(files: str) -> str:
    files = files.split(": ")[1].split(", ")
    bad_patterns = ["virus", "malware"]
    safe_patterns = ["antivirus", "notvirus"]
    safe_files = []
    for file in files:
        if any(bad in file for bad in bad_patterns) and not any(
            safe in file for safe in safe_patterns
        ):
            continue
        safe_files.append(file)
    return f"PC Files: {', '.join(safe_files)}" if safe_files else "PC Files: Empty"
