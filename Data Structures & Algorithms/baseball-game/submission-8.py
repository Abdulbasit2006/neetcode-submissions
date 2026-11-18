class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            match operations[i]:
                case "+":
                    record.append(int(record[-1] + record[-2]))
                case "D":
                    record.append(int(2 * record[-1]))
                case "C":
                    record.pop()
                case _:
                    record.append(int(operations[i]))
        sm = 0
        for i in range(len(record)):
            sm += int(record[i])
        return sm
                    


            


        