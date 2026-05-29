import pytest

from src.detector import detect_frequent_characters

# Arrange
@pytest.mark.parametrize(
    "test_input,expected",
    [
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
        pytest.param("äöüä", ["ä"], id="Type_German_Umlaute"),
        pytest.param("🚀🛸🚀", ["🚀"], id="Type_Unicode_Emojis"),
        pytest.param("abcA", [], id="Logic_Case_Sensitivity_A_vs_a"),
        pytest.param("   ", [" "], id="Logic_Multiple_Spaces"),
        pytest.param("a\nb\nc\n", ["\n"], id="Logic_Multiple_Newlines"),
        
        # Performance stress test
        pytest.param("x" * 100000 + "y" * 100000, ["x", "y"], id="Scale_Large_Input_Volume"),
    ],
)

def test_detect_frequent_characters(test_input, expected):
    # Act
    result = detect_frequent_characters(test_input)
    
    # Assert
    assert sorted(result) == sorted(expected)