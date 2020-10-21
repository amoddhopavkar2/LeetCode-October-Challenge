# Minimum Domino Rotations For Equal Row

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if not A or not B or (len(A) != len(B)):
            return -1

        if len(A) == len(B) == 1:
            return 1
        
        result = -1
        for num in range(1, 7):
            count, a_count, b_count = 0, 0, 0
            while count < len(A):
                if A[count] == B[count] == num:
                    a_count += 1
                    b_count += 1
                elif A[count] == num:
                    a_count += 1
                elif B[count] == num:
                    b_count += 1
                else:
                    break
                count += 1

            if count == len(A):
                if result == -1:
                    result = min(len(A) - a_count, len(B) - b_count)
                else:
                    result = min(result, min(len(A) - a_count, len(B) - b_count))

        return result
