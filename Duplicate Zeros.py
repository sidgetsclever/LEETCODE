class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        l = len(arr)
        for i in range(l):
            if arr[i] == 0 and arr[i-1] is not 0:
                arr[i+1:] = arr[i:]
        del arr[l:]
