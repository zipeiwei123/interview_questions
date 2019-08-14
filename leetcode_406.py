"""Sort the array in descending order according to height
  if the adjcent has the same height, sort in ascending order according to k"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #sort in descending order by height
        people.sort(key = lambda x: (-x[0], x[1]))
        print(people)
        ans = []
        for p in people:
            #insert according to k/index
            ans.insert(p[1], p)
        return ans
            