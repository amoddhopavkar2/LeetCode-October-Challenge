# Bag of Tokens

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        points, max_points = 0, 0
        start = 0
        end = len(tokens) - 1

        while start <= end:
            if P >= tokens[start]:
                points += 1
                P -= tokens[start]
                start += 1
                max_points = max(points, max_points)

            elif points > 0:
                points -= 1
                P += tokens[end]
                end -= 1

            else:
                return max_points
        
        return max_points