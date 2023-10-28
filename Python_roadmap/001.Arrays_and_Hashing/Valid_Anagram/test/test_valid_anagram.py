from src.valid_anagram import Anagram

class TestValidAnagram:

    def test_valid_anagram(self):
        anagram = Anagram()
        input_1 = "anagram"
        input_2 = "nagaram"

        assert anagram.is_anagram(input_1, input_2) == True
    
    def test_invalid_anagram(self):
        anagram = Anagram()
        input_1 = "rat"
        input_2 = "car"

        assert anagram.is_anagram(input_1, input_2) == False

    def test_different_words(self):
        anagram = Anagram()
        input_1 = "rat"
        input_2 = "dedo"

        assert anagram.is_anagram(input_1, input_2) == False
