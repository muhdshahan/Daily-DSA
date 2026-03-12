class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        print(arr)
        minimum = max(arr)*1000
        for i in range(len(arr)-1):
            print("enter")
            if arr[i+1]-arr[i]<minimum:
                minimum=arr[i+1]-arr[i]
        rslt = []
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==minimum:
                rslt.append([arr[i],arr[i+1]]) 
        return rslt