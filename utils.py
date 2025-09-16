import re


def find_ranked_matches(text: str, query: str):
    """
    Return [(word, percent)] sorted by descending percent, then alphabetically.
    percent = 100 * len(query) / len(word)
    """
    rx = re.compile(rf"\b\w*{re.escape(query)}.*\b", re.IGNORECASE)
    seen = set()
    results = []

    for m in rx.finditer(text):
        word = m.group(0)
        key = word.lower()
        if key in seen:
            continue
        seen.add(key)
        pct = round(100 * len(query) / len(word), 2)
        results.append((word, pct))

    results.sort(key=lambda t: (-t[1], t[0].lower()))
    return results


if __name__ == "__main__":
    import os
    files_location = os.path.join("fake-filesystem")
    query = "pixel"
    text = "\n".join(os.listdir(files_location))
    
    
    print(find_ranked_matches(text, query)[0][0])
    