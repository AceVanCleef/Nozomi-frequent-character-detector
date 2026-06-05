from typing import List

from line_profiler import profile
import array

@profile
def detect_frequent_characters(string: str | list | tuple):
    if string is None:
        raise TypeError("Input parameter can't be none.")
    
    if not isinstance(string, (str, list, tuple)):
        raise TypeError("Invalid data type: Input parameter must be an iterable type of str, list or tuple")
    
    found_once: set[str] = set()
    found_frequently: set[str] = set()
    for e in string:
        if e in found_frequently:
            continue
        else:
            if e in found_once:
                found_frequently.add(e)
            else:
                found_once.add(e)

    return found_frequently

@profile
def detect_frequent_ascii_characters(string: str | list | tuple):
    if string is None:
        raise TypeError("Input parameter can't be none.")
    
    if not isinstance(string, (str, list, tuple)):
        raise TypeError("Invalid data type: Input parameter must be an iterable type of str, list or tuple")
    
    ascii_tracker = array.array('L', [0] * 256)
    
    try:
        for e in string:
            ascii_tracker[ord(e)] += 1
    except IndexError:
        raise ValueError(f"Character {e} lies outside the legal ascii character code range.")

    found_frequently: List[str] = list()
    for index, value in enumerate(ascii_tracker):
        if value >= 2:
            found_frequently.append(chr(index))
    return found_frequently

if __name__ == "__main__":
    print("Running detector in terminal:")
    detect_frequent_characters("banana")
    detect_frequent_ascii_characters("banana")