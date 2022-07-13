

class Solution(object):
    def groupAnagrams(self, strs):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        Map = defaultdict(list)
        for word in strs:
            letters = [0] * 26
            for char in word:
                letters[alpha.find(char)] += 1

            Map[tuple(letters)].append(word)
            
        return Map.values()
            
                