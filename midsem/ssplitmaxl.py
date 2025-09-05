def max_l_word(s: str) -> str:
    return max(s.split(), key=len)

print(max_l_word("Hello World from Python"))