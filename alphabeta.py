MAX, MIN = 1000, -1000

def alphabeta(depth, nodeIndex,depth_limit, maximizingPlayer, values, alpha, beta): 
    if depth == depth_limit: 
        return values[nodeIndex] 

    if maximizingPlayer: 
        best = MIN
        for i in range(0, 2): 
            val = alphabeta(depth + 1, nodeIndex * 2 + i,depth_limit, False, values, alpha, beta) 
            best = max(best, val) 
            alpha = max(alpha, best) 
            if beta <= alpha: 
                break
        return best

    else:
        best = MAX
        for i in range(0, 2): 
            val = alphabeta(depth + 1, nodeIndex * 2 + i,depth_limit, True, values, alpha, beta) 
            best = min(best, val) 
            beta = min(beta, best) 
            if beta <= alpha: 
                break
        return best 

    

values = []
depth_limit = int(input("Enter the depth of tree: "))
for i in range(0,2**depth_limit):
    value = int(input(f"Enter value for node{i+1}: "))
    values.append(value)
print("The optimal value is :", alphabeta(0, 0,depth_limit, True, values, MIN, MAX)) 
