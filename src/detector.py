from line_profiler import profile

@profile
def detect_frequent_characters(string: str | list | tuple):
    found_once: set[str] = set()
    found_frequently: set[str] = set()
    for e in string:
        if e in found_frequently:
            next
        else:
            if e in found_once:
                found_frequently.add(e)
            else:
                found_once.add(e)
   # print(found_frequently)
   # print(found_once)
    return found_frequently

if __name__ == "__main__":
    print("Running detector in terminal:")
    detect_frequent_characters("banana")