from __future__ import annotations
from typing import List


class Interval(object):
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> None:
        return f'({self.start}, {self.end})'


class Solution:
    def can_attemp_meetings(self, intervals: List[Interval]) -> bool:

        for ref_idx in range(len(intervals)-1):
            for check_idx in range(ref_idx + 1, len(intervals)):
                ref = intervals[ref_idx]
                check = intervals[check_idx]

                if ref.start < check.start:
                    if ref.end > check.start:
                        return False

                else:
                    if ref.start < check.end:
                        return False

        return True


intervals = [
    Interval(0, 30), Interval(5, 10), Interval(15, 20)
]
print(Solution().can_attemp_meetings(intervals))

intervals = [
    Interval(5, 8), Interval(8, 10)
]
print(Solution().can_attemp_meetings(intervals))
