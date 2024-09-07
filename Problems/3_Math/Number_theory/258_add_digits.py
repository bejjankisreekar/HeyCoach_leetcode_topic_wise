class Solution:
    def addDigits(self, num: int) -> int:
        temp = num
        sum = 0
        if len(str(temp)) == 1:
            return temp
        while len(str(temp)) > 1:
            sum = self.cal_sum(temp)
            temp = sum

        return sum

    def cal_sum(self, temp):
        sum = 0
        while temp > 0:
            digit = temp % 10
            sum += digit
            temp //= 10

        return sum

