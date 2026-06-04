class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} 

        for item in nums: 
            if item in count: 
                count[item] += 1 
            else:   
                count[item] = 1 
        return heapq.nlargest(k, count.keys(), key=count.get)

       
        
        
        
       

        
            