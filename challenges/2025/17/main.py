def split_into_buckets(phrase: str, n: int) -> list[str]:
    words = phrase.split()
    if any(len(word) > n for word in words):
        return []

    buckets = []
    current = ""
    for word in words:
        if not current:
            current = word
        elif len(current) + 1 + len(word) <= n:
            current += " " + word
        else:
            buckets.append(current.strip())
            current = word
    if current:
        buckets.append(current.strip())

    return buckets
