# 本质上是找到左右两边最低的柱子， 然后算他和height的差

class Solution:
    def trap(self, height: List[int]) -> int:

        #         At index i, left_max[i] := max height on the left
        left_max = []
        right_max = []

        max_height = 0

        for h in height:
            max_height = max(h, max_height)
            left_max.append(max_height)

        max_height = 0
        for h in height[::-1]:
            max_height = max(h, max_height)
            right_max.append(max_height)
        right_max = right_max[::-1]

        volumn = 0

        for i in range(len(height)):
            h = min(left_max[i], right_max[i])
            volumn += h - height[i]
        return volumn