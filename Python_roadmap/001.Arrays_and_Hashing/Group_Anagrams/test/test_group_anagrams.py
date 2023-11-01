from src.group_anagrams import GroupAnagrams


class TestGroupAnagrams:

    def test_empty_group_anagrams(self):
        groupAnagrams = GroupAnagrams();
        
        assert groupAnagrams.group_angrams(strs=[""]) == [[""]];


    def test_group_anagrams(self):
        groupAnagrams = GroupAnagrams();
        result = groupAnagrams.group_angrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]);

        assert sorted(result) == sorted([["tan", "nat"], ["bat"], ["eat", "tea", "ate"]]);
