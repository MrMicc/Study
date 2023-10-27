from src.contains_duplicate import ContainsDuplicate

class TestContainsDuplicate:

    def test_one_duplicate(self):
        input = [1,2,3,1]
        solution = ContainsDuplicate()
        assert solution.containsDuplicate(nums=input) == True

    def test_no_duplicate(self):
        input = [1,2,3,4]
        solution = ContainsDuplicate()
        assert solution.containsDuplicate(nums=input) == False

    def test_duplicate_in_the_middle(self):
        input = [1,1,1,3,3,4,3,2,4,2]
        solution = ContainsDuplicate()
        assert solution.containsDuplicate(nums=input) == True

    
