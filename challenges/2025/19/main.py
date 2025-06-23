def no_yelling(sentence: str) -> str:
    return (
        sentence.rstrip("?") + "?"
        if sentence.endswith("?")
        else sentence.rstrip("!") + "!"
    )
