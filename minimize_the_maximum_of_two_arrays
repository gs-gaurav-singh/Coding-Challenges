import math

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def can(M):

            cnt1 = M - M // divisor1
            cnt2 = M - M // divisor2
            cnt_both = M - M // divisor1 - M // divisor2 + M // math.lcm(divisor1, divisor2)

            return cnt1 >= uniqueCnt1 and cnt2 >= uniqueCnt2 and (cnt1 + cnt2 - cnt_both) >= (uniqueCnt1 + uniqueCnt2)

        left, right = 1, 10**18
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left
