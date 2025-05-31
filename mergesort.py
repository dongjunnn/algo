class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(arr):
            if len(arr) == 1:
                return arr
            return merge(mergesort(arr[:len(arr)//2]), mergesort(arr[len(arr)//2:]))


        def merge(arr1, arr2):
            res = []
            ptr1 = ptr2 = 0
            while ptr1 < len(arr1) and ptr2 < len(arr2):
                if arr1[ptr1] < arr2[ptr2]:
                    res.append(arr1[ptr1])
                    ptr1 += 1
                else:
                    res.append(arr2[ptr2])
                    ptr2 += 1
            while ptr1 < len(arr1):
                res.append(arr1[ptr1])
                ptr1 += 1
            while ptr2 < len(arr2):
                res.append(arr2[ptr2])
                ptr2 += 1
            return res
        
        return mergesort(nums)
