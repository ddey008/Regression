class Solution(object):

    def combinationSum(self, candidates, target):
        candidates.sort()
        return self.recursion_helper(candidates, [], target, [])

    def recursion_helper(self, candidates, result, target, temp_list, sum=0, i=0):
        # Base Case
        if len(candidates) == 1:
            if target == candidates[i]:
                temp_list.append(candidates[i])
                result.append(temp_list)
            return result

        # Checking if target reached
        if sum == target:
            result.append(temp_list[:])
            temp_list.pop(-1)
            return result

        # Backtracking if sum greater
        if sum > target:
            temp_list.pop(-1)
            return result

        elif sum < target:
            for j in range(i,len(candidates)):
                if sum + candidates[j] <= target:
                    sum += candidates[j]
                    temp_list.append(candidates[j])
                    self.recursion_helper(candidates, result, target, temp_list, sum, j)
                    sum -= candidates[j]
                else:
                    break
        if temp_list:
            temp_list.pop(-1)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([8,7,4,3], 11))