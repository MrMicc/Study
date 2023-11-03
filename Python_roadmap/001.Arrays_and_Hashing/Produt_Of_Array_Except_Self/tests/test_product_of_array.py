from src.product_of_array import ProductOfArray


class TestProductOfArray:

    def test_product_of_array(self):
        product = ProductOfArray()
        assert product.product_of_array([1, 2, 3, 4]) == [24, 12, 8, 6]

        assert product.product_of_array([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    def test_product_except_self(self):
        product = ProductOfArray()

        assert product.product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
        assert product.product_except_self(
            [-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
