class Solution:
    """
    @param cars:  integer array of length denoting the parking slots where cars are parked
    @param k: integer denoting the number of cars that have to be covered by the roof
    @return: return the minium length of the roof that would cover k cars
    """
    def ParkingDilemma(self, cars, k):
        # write your code here
        cars.sort()
        ret = cars[k - 1] - cars[0] + 1
        for i in range(k, len(cars)):
            length = cars[i] - cars[i - k + 1] + 1
            if length < ret:
                ret = length
        return ret

# easy: https://www.lintcode.com/problem/parking-dilemma/
