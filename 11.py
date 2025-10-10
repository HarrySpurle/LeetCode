class Solution:
    def maxArea(self, height):
        leftpointer = 0
        rightpointer = len(height) - 1
        maxarea = 0

        while leftpointer < rightpointer:
            maxarea = max(maxarea, (rightpointer - leftpointer) * min(height[leftpointer], height[rightpointer]))
            if height[leftpointer] < height[rightpointer]:
                leftpointer += 1
            else:
                rightpointer -= 1

        return maxarea