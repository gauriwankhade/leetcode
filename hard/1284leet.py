

class Solution(object):
    def minFlips(self, mat):
        self.length = len(mat)
        self.mLen = len(mat[0])
        flag = count = 0
        visited = {}

        while (count < 1000):
            queue = [(0, 0)]
            visited = {}
            while (queue):
                if not self.checkMat(mat):
                    elem = queue.pop(0)
                    if not visited.get(elem):
                        visited[elem] = True
                        self.flipMatrix(elem[0], elem[1], mat, queue)
                    count += 1
                else:
                    return count

             
            
        return - 1


    def flipMatrix(self, i, j, mat, queue):
        #print('i, j: ', i, j)
        mat[i][j] = 1 - mat[i][j]
        if self.length > i + 1 :
            #print('i + 1: ', i + 1)
            mat[i + 1][j] = 1 - mat[i + 1][j]
            queue.append((i + 1, j))
        if self.mLen > j + 1:
            #print('j + 1: ', j + 1)
            mat[i][j + 1] = 1 - mat[i][j + 1]
            queue.append((i, j + 1))
        if i - 1 >= 0:
            #print('i - 1: ', i - 1)
            mat[i - 1][j] = 1 - mat[i - 1][j]
            queue.append((i - 1, j))
        if j - 1 >= 0:
            #print('j - 1: ', j - 1)
            mat[i][j - 1] = 1 - mat[i][j - 1]
            queue.append((i, j - 1))

    def checkMat(self, mat):
        summ = 0
        for num in mat:
            summ += sum(num)
        #if summ == 0: print(f'found it - summ {summ}')
        if summ <= 0:
            return True
        return False


s = Solution()
nums =  [[0,0],[0,1]]
print(nums, len(nums))
print(s.minFlips(nums))

        