"""Still two lines confused"""

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        #if the word is not exist
        if not words:
            return []
        match_words = []
        for word in words:
            first_index = text.find(word)
            #only record the one that has word
            while first_index != -1:
                #for each word, need to check all the word
                match_words.append([first_index, first_index+len(word) - 1])
                #update i
                first_index= text.find(word, first_index+1)
                print(first_index)
            # if first_index != -1:
            #     match_words.append([first_index, first_index+len(word) - 1])
        match_words.sort()
        return match_words
        
        