def actual_memory_size(ms: str) -> str:
    memory_size = float(ms[:-2])
    actual_memory_size = memory_size * 0.93

    if ms.endswith("MB"):
        return f"{actual_memory_size:.0f}MB"
    if ms.endswith("GB") and actual_memory_size < 1:
        return f"{actual_memory_size * 1000:.0f}MB"
    return f"{actual_memory_size:.2f}GB"
