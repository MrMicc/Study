from src.two_sum import TwoSum

class TestTwoSum:

    def test_small_list(self):
        two_sum = TwoSum([1]);
        try:
            two_sum.get_sum(0);
        except ValueError as error :
            assert str(error) == "Need more then one element in array";
       

    def test_get_sum(self):
        two_sum = TwoSum([2,7,11,15]);
        result = two_sum.get_sum(9);
        assert result == [0,1];

        two_sum = TwoSum([3,2,4]);
        result = two_sum.get_sum(6);
        assert result == [1,2];

        two_sum = TwoSum([3,3]);
        result = two_sum.get_sum(6);
        assert result == [0,1];


