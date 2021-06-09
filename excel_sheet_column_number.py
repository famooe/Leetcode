class Solution(object):
    def titleToNumber(self, columnTitle):
        total, count = 0, 0
        for i in columnTitle[::-1]:
            total += (ord(i) - 64) * (26 ** count)             #ord('A') = 65
            count += 1
        return total
