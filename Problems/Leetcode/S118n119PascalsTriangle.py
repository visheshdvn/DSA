class Solution:
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]

        triangle = [[1], [1, 1]]

        for i in range(2, numRows):
            lst = []
            for j in range(i+1):
                if j == 0 or i == j:
                    lst.append(1)
                    continue

                lst.append(triangle[i-1][j-1] + triangle[i-1][j])

            triangle.append(lst)

        return triangle

    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]

        ret_row = [1, 1]

        for i in range(1, rowIndex+1):
            lst = []
            for j in range(i+1):
                if j == 0 or i == j:
                    lst.append(1)
                    continue

                lst.append(ret_row[j-1] + ret_row[j])

            ret_row = lst

        return ret_row


numRows = int(input())
ob = Solution()
# print(ob.generate(numRows))
print(ob.getRow(numRows))
