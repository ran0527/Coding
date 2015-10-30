class Solution(object):
    def combinationSum2(self, candidates, target):
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
        if target == 0:
            result.append(list(path))

        n = len(candidates)
        prev = None
        for i in range(current, n):
            num = candidates[i]
            num_1 = candidates[i-1]
            if target-num < 0:
                break
            if prev == None or prev != num:
                path.append(num)
                self.recursive(candidates, target-num, path, result, i+1)
                path.pop()
                prev = num
        
