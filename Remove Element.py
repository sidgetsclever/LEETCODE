class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = nums.count(val)
        for _ in range(c):
            nums.pop(val)
        
