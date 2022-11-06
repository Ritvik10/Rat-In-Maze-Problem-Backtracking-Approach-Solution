res = []
 
def isValid(row, col, m, n):
         
    if (row >= 0 and row < n and col >= 0 and col < n and m[row][col] == 1):
        return True
 
    return False
 
     
def findPathHelper(m, n, x, y, dx, dy, path):
   
    global res
     
    if (x == n - 1 and y == n - 1):
        res.append(path)
        return
 
    dir = "DLRU"
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if (isValid(row, col, m, n)):
            m[row][col] = 2             # used to track visited cells of matrix
            findPathHelper(m, n, row, col, dx, dy, path + dir[i])
            m[row][col] = 1             # mark it unvisited yet explorable
         
def findPath(m,n):
    global res
     
    res.clear()
     
    # dx, dy will be used to follow `DLRU` exploring approach
    # which is lexicographically sorted order
    dx = [ 1, 0, 0, -1 ]
    dy = [ 0, -1, 1, 0 ]
    if (m[0][0] == 1):
        m[0][0] = 2
        findPathHelper(m, n, 0, 0, dx, dy, "")
 
    return res
 
# driver code
m = [ [ 1, 0, 0, 0, 0 ],
      [ 1, 1, 1, 1, 1 ],
      [ 1, 1, 1, 0, 1 ],
      [ 0, 0, 0, 0, 1 ],
      [ 0, 0, 0, 0, 1 ] ]
n = len(m)
 
ans = findPath(m, n)
print(ans)
 
