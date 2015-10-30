class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        path = []
        self.recursive(candidates, target, path, result, 0)
        return result


    def recursive(self, candidates, target, path, result, current):
        # end condition
        if target == 0:
            result.append(list(path))

        # goes deeper
        n = len(candidates)
        for i in range(current, n):
            num = candidates[i]
            if target-num < 0:
                break
            path.append(num)
            self.recursive(candidates, target-num, path, result, i)
            path.pop()
