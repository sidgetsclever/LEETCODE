class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i]/2 == arr[j] or arr[i]*2 == arr[j]:
                    count += 1
                    #print('for', i, " ", j)
        if count > 0:
            return 1
        else: 
            return 0
