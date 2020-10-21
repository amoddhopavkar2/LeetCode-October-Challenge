# Asteroid Collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            collision = False
            if asteroid < 0:
                while result and (last := result[-1]) > 0:
                    if last == -(asteroid):
                        result.pop()
                        collision = True
                        break
                    elif last < -(asteroid):
                        result.pop()
                    else:
                        collision = True
                        break
        
            if not collision:
                result.append(asteroid)
        return result
