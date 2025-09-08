from string_utils import StringUtils

string_utils = StringUtils()


class TestStringUtils:
    def test_capitalize_positive(self):
        assert string_utils.capitalize("skypro") == "Skypro"
        assert string_utils.capitalize("s") == "S"

    def test_capitalize_negative(self):
        assert string_utils.capitalize("123") == "123"
        assert string_utils.capitalize(" ") == " "

    def test_trim_positive(self):
        assert string_utils.trim("   skypro") == "skypro"
        assert string_utils.trim(" skypro") == "skypro"
        assert string_utils.trim("skypro") == "skypro"
        assert string_utils.trim("") == ""
        assert string_utils.trim("        skypro") == "skypro"

    def test_trim_negative(self):
        assert string_utils.trim("skypro   ") == "skypro   "
        assert string_utils.trim("\tskypro") == "\tskypro"

    def test_contains_positive(self):
        assert string_utils.contains("SkyPro", "S") is True
        assert string_utils.contains("SkyPro", "y") is True
        assert string_utils.contains("SkyPro", "P") is True
        assert string_utils.contains("SkyPro", "") is True
        assert string_utils.contains("aaaaa", "a") is True

    def test_contains_negative(self):
        assert string_utils.contains("SkyPro", "U") is False
        assert string_utils.contains("SkyPro", "s") is False
        assert string_utils.contains("", "a") is False

    def test_delete_symbol_positive_single(self):
        assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert string_utils.delete_symbol("aaaaa", "a") == ""
        assert string_utils.delete_symbol("SkyPro", "S") == "kyPro"
        assert string_utils.delete_symbol("SkyPro", "o") == "SkyPr"
        assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"

    def test_delete_symbol_positive_multiple(self):
        assert string_utils.delete_symbol("banana", "a") == "bnn"
        assert string_utils.delete_symbol("hello world", "l") == "heo word"

    def test_delete_symbol_negative_not_found(self):
        assert string_utils.delete_symbol("SkyPro", "z") == "SkyPro"
        assert string_utils.delete_symbol("", "a") == ""

    def test_delete_symbol_positive_substring(self):
        assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert string_utils.delete_symbol("ababab", "ab") == ""
        assert string_utils.delete_symbol("testtest", "st") == "tete"

