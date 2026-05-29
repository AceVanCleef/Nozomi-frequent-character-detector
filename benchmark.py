from src.detector import detect_frequent_ascii_characters, detect_frequent_characters

if __name__ == "__main__":
    test_input = ("x" + "y") * 50000  # 100'000 characters
    detect_frequent_characters(test_input)
    detect_frequent_ascii_characters(test_input)