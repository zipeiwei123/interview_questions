"""Trie, easy solution, check if the prefix exist, use defaultdict for structure of Trie"""
import collections
class Solution:
    def longestWord(self, words: List[str]) -> str:
        #special case
        if not words:
            return 0
        trie = {}
        result = []
        #create trie as 1:['w'], 2:[]'word']
        for word in words:
            l = len(word)
            trie[l] = trie.get(l,[])+[word]
        print(trie)
        #sort the word length in descending order
        sorted_words=sorted(list(trie.keys()))[::-1]
        print(sorted_words)
        
            
                        
                
#         ans = ""
#         #covert word to set
#         word_set = set(words)
#         for word in words:
#              if len(word) >= len(ans)  or len(word) == len(ans) and word < ans:
#                     if all(word[:k] in word_set for k in range(1, len(word))):
#                         ans = word
        
#         return ans