x0 = 0.5
u = 2.1
N = 20
results = [None] * (N+1)

def samuelson(x, index):
    if (x>0):
        results[index] = u * samuelson(x-1, index + 1) - (u+1)*(samuelson(x-1, index + 1) )**3
        # print(result)
    else:
        results[index] = x0
    return results[index]

print("\n\nSamuelson Map Results")
samuelson(N, 0)
print results[::-1]
