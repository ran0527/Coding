class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        s_left = (C-A) * (D-B)
        s_right = (G-E) * (H-F)
        s_comb = max(min(C,G)-max(A,E), 0) * max(min(D,H)-max(B,F), 0)
        sum = s_left + s_right - s_comb
        return sum
        
