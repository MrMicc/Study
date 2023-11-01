from typing import List; 
from collections import defaultdict;

class GroupAnagrams:

    def group_angrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hash map to store the anagrams

        result = defaultdict(list);

        for str in strs:
            
            seen = ''.join(sorted(str));
            if seen in result:
                result[seen].append(str);
            else:
                result[seen] = [str];


        print(list(result.values()));
        return list(result.values());


