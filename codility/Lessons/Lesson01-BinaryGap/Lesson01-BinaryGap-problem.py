'''
input : 1041, 15, 32
output : 5, 0, 0
'''

def makeBinary(N):
    binary = []
    while N > 0:
        binary.append(N%2)
        N = N // 2
    return binary[::-1]

def countBinaryGap(binary):
    maxGap, cntGap = 0, 0
    for i in range(1, len(binary)):
        if binary[i] == 0:
            cntGap += 1
        elif binary[i] == 1:
            if cntGap > maxGap:
                maxGap = cntGap
            cntGap = 0
    return maxGap

def solution(N):
    return countBinaryGap(makeBinary(N))

