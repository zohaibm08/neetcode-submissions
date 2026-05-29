class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inNums = {}
        A = []

        for j in range(len(nums)):
            inNums[nums[j]] = j 
        
        for i in range(len(nums)):
            need = target - nums[i]
            if need in inNums and inNums[need] != i:
                A.append(i)
                A.append(inNums[need])
                return A

        return A