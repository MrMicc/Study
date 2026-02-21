from src.longest_common_prefix import Prefix 

class TestLongestCommonPrefix:
    def test_longest_common_prefix_with_empty_list(self):
        input = []
        output = ""
        
        solution = Prefix()
        assert solution.longest_common_prefix(input) == output

    def test_longest_common_prefix(self):
        input = ["flower", "flow", "flight"]
        output = "fl"

        solution = Prefix()

        assert solution.longest_common_prefix(input) == output


        input = ["dog", "racecar", "car"]
        output = ""

        assert solution.longest_common_prefix(input) == output

        input = ["ab", "a"]
        output = "a"

        assert solution.longest_common_prefix(input) == output

        input = ["a", "ab"]
        output = "a"

        assert solution.longest_common_prefix(input) == output

        input = ["c", "acc", "ccc"]
        output = ""

        assert solution.longest_common_prefix(input) == output

