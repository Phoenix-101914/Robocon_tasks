class Solution(object):
    def generate(self, numRows):
        T_list=[[1]]
        if numRows==1:
            return T_list
        T_list.append([1,1])
        if numRows==2:
            return T_list
        for i in range(3,numRows+1):
            A=[1]
            for j in range(1,i-1):
                A.append(T_list[i-2][j-1]+T_list[i-2][j])
            A.append(1)
            T_list.append(A)
        return T_list
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
numRows=int(input("Enter number of rows "))
solution=Solution()
print(solution.generate(numRows))
