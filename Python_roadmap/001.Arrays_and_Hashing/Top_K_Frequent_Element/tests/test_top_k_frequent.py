from src.top_k_frequent import TopKFrequent


class TestTopKFrequent:

    def test_top(self):

        result = TopKFrequent().top([1, 1, 1, 2, 2, 3], 2)

        assert result == [1, 2]

        result = TopKFrequent().top([1], 1)

        assert result == [1]

    def test_top_with_negative(self):

        result = TopKFrequent().top([4, 1, -1, 2, -1, 2, 3], 2)

        assert result == [-1, 2]
