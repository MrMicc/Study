from src.longest_consecutive import LongestConsecutive


class TestLongestConsecutive():

    def test_order_longest_consecutive(self):
        consecutive = LongestConsecutive([100, 4, 200, 1, 3, 2])

        assert consecutive.get_longest_length() == 4

        consecutive = LongestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        assert consecutive.get_longest_length() == 9

        # [-1,-1,0,1,3,4,5,6,7,8,9]
        consecutive = LongestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])
        assert consecutive.get_longest_length() == 7
