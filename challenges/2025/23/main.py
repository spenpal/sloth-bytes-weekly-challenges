def next_letters(s: str) -> str:
    if not s:
        return "A"
    if s[-1] != "Z":
        return s[:-1] + chr(ord(s[-1]) + 1)
    return next_letters(s[:-1]) + "A"
