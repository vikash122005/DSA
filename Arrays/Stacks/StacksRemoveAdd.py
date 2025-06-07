class Solution(object):
    def sum_of_all(self, x):
        total = 0
        for num in x:
            total += num
        return total
    def calPoints(self, operations):
        x = []
        for i in range(len(operations)):
            if(operations[i] == "D"):
                x.append(x[-1] * 2)
            elif(operations[i] == "C"):
                x.pop()
            elif operations[i] == "+":
                x.append(x[-1] + x[-2])
            else:
                val = operations[i]
                x.append(int(val))
        return self.sum_of_all(x)