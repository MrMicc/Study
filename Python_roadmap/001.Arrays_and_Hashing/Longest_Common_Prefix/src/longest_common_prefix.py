from typing import List

class Prefix:

    def longest_common_prefix(self, words: List[str]) -> str:

        if words == []:
            return ""
        prefix = words[0]


        for word in words[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

        return prefix


