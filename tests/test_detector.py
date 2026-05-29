import pytest

from src.detector import detect_frequent_ascii_characters, detect_frequent_characters

# Arrange
SHARED_ASCII_CASES = [
    # Testing input types
    pytest.param("caiopa", ["a"], id="Input_Type_String"),
    pytest.param(['c', 'a', 'i', 'o', 'p', 'a'], ["a"], id="Input_Type_List"),
    pytest.param(('c', 'a', 'i', 'o', 'p', 'a'), ["a"], id="Input_Type_Tuple"),
    
    # Regular test cases and edge cases
    pytest.param("", [], id="Logic_Empty_String"),
    pytest.param("abcdef", [], id="Logic_No_Duplicates"),
    pytest.param("banana", ["a", "n"], id="Logic_Multiple_Duplicates"),
    pytest.param("aaaaa", ["a"], id="Logic_Single_Character_Heavy_Repetition"),
    pytest.param("aabcde", ["a"], id="Logic_Single_Character_Position_Agnostic_Prefix"),
    pytest.param("bcdeaa", ["a"], id="Logic_Single_Character_Position_Agnostic_Suffix"),
    pytest.param("bcaade", ["a"], id="Logic_Single_Character_Position_Agnostic_In_Between"),
    pytest.param("abbccc", ["b", "c"], id="Logic_Exact_Boundary_Check"),
    
    # Testing different character categories (unicode & robustness)
    pytest.param("123245", ["2"], id="Type_Numbers"),
    pytest.param("a!b!c!", ["!"], id="Type_Special_Characters"),
    pytest.param("abcA", [], id="Logic_Case_Sensitivity_A_vs_a"),
    pytest.param("   ", [" "], id="Logic_Multiple_Spaces"),
    pytest.param("a\nb\nc\n", ["\n"], id="Logic_Multiple_Newlines"),
    pytest.param("äöüä", ["ä"], id="Type_German_Umlaute"),

    # Performance stress test
    pytest.param("x" * 100000 + "y" * 100000, ["x", "y"], id="Scale_Large_Input_Volume"),
]

UNICODE_ONLY_CASES = [
    pytest.param("🚀🛸🚀", ["🚀"], id="Type_Unicode_Emojis"),
    pytest.param("ĀÿĀ", ["Ā"], id="Type_ASCII_Upper_Boundary"),   
]

INVALID_PARAMETER_VALUES = [
    pytest.param(None, "Input parameter can't be none.", id="Logic_None_Input_Value"),
    pytest.param({"a", "b", "c", "c"}, "Invalid data type", id="Logic_Set_Input_Type"),
    pytest.param({1: "a", 2: "b", 3: "c"}, "Invalid data type", id="Logic_Dictionary_Input_Type"),
    pytest.param(1234556, "Invalid data type", id="Logic_Numerical_Input_Type"),
    pytest.param(1.234556, "Invalid data type", id="Logic_Float_Input_Type"),
    pytest.param(object(), "Invalid data type", id="Logic_Object_Input_Type"),
]

@pytest.mark.parametrize("test_input, expected", SHARED_ASCII_CASES + UNICODE_ONLY_CASES)
def test_detect_frequent_characters(test_input, expected):
    # Act
    result = detect_frequent_characters(test_input)
    
    # Assert
    assert sorted(result) == sorted(expected)

@pytest.mark.parametrize("test_input, expected", INVALID_PARAMETER_VALUES)
def test_detect_frequent_characters_invalid_input(test_input, expected):
    # Act
    with pytest.raises(TypeError) as exception_info:
        detect_frequent_characters(test_input)
    
    assert expected in str(exception_info.value)
    

@pytest.mark.parametrize("test_input, expected", SHARED_ASCII_CASES)
def test_detect_frequent_ascii_characters(test_input, expected):
    # Act
    result = detect_frequent_ascii_characters(test_input)
    
    # Assert
    assert sorted(result) == sorted(expected)
    
@pytest.mark.parametrize("test_input, expected", UNICODE_ONLY_CASES)
def test_detect_frequent_ascii_characters_boundaries(test_input, expected):
    # Act
    with pytest.raises(ValueError) as exception_info:
        detect_frequent_ascii_characters(test_input)
    
    # Assert
    assert "outside the legal ascii character code range" in str(exception_info.value)
    
@pytest.mark.parametrize("test_input, expected", INVALID_PARAMETER_VALUES)
def test_detect_frequent_ascii_characters_invalid_input(test_input, expected):
    # Act
    with pytest.raises(TypeError) as exception_info:
        detect_frequent_ascii_characters(test_input)
    
    assert expected in str(exception_info.value)