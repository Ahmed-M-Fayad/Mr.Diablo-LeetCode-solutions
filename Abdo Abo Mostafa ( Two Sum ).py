
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # to track every element in list
        for i in range(len(nums)):
            """
             - in this loop I will start from The element that be next the i
             - we do This because in case of  [ 3 , 3 ]we want to return the index of [ 0 , 1 ] not [ 0 , 0 ]
             - this Solution will become BIG O(n^2)   
            """
            for j in range(i+1 ,len(nums) ):
                # compare between the sumtion of Two Element and target
                if nums[i] + nums[j] == target:
                    return [i,j]


  #                                  BIG O(n)



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = [(value, idx) for idx, value in enumerate(nums)]

        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            value_i, idx_i = nums[i][0], nums[i][1]
            value_j, idx_j = nums[j][0], nums[j][1]

            if value_i + value_j == target:
                return [idx_i, idx_j]
            elif value_i + value_j < target:
                i += 1  # to increase value_i + value_j
            else:
                j -= 1  # to decrease value_i + value_j
print(Solution().twoSum(nums=[2,7,11,15],target= 9))
print(Solution().twoSum(nums=[3, 2, 4], target=6))
print(Solution().twoSum(nums=[3, 3], target=6))