class Anagram:
    def is_anagram(self, word1: str, word2: str) -> bool:
        hashmap_word1, hashmap_word2 = {}, {}
        print("oieee")


        if not self._same_lenght(word1, word2):
            return False

        for i in range(len(word1)):
            hashmap_word1[word1[i]] = hashmap_word1.get(word1[i],0)+1 
            hashmap_word2[word2[i]] = hashmap_word2.get(word2[i],0)+1


        for key in hashmap_word1:
            if hashmap_word1[key] != hashmap_word2.get(key,0):
                return False
        return True

    def _same_lenght(self, word1: str, word2: str) -> bool:
        return len(word1) == len(word2)
