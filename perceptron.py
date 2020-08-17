import numpy as np

# every sub list is a iteration input
# first parameter is b, second parameter is x1, third parameter is x2, fourth parameter is y
inputOR = [[1,0,0,0],[1,0,1,1],[1,1,0,1],[1,1,1,1]]
inputNAND = [[1,0,0,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
inputXOR = [[1,0,0,0],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
lRate = 0.1
max_iter = 8


def sign(num):
    if num >= 0:
        return 1
    else:
        return 0

def calc_vector_multi(w, input):
    b = input[0]
    x1 = input[1]
    x2 = input[2]
    return w[0]*b+w[1]*x1+w[2]*x2

def update_weight(w, lRate, input, sign):
    b = input[0]
    x1 = input[1]
    x2 = input[2]
    y = input[3]
    learn = lRate*(y-sign)
    w1 = learn*x1
    w2 = learn*x2
    wb = learn*b
    return [w[0]+wb, w[1]+w1, w[2]+w2]

def main(input, w=[0,0,0]):
    correct_count = 0
    j = 0
    ephoc_count = 1
    for i in range(max_iter*len(input)):
        if j == 4:
            j = 0
        if j == 0:
            print("Epoch Number "+str(ephoc_count))
            ephoc_count += 1
        print("Iteration "+str(i+1))
        if correct_count == 4:
            print("our best w is: "+str(w))
            break
        print("B="+str(input[j][0])+", X1="+str(input[j][1])+", X2=",str(input[j][2])+", y="+str(input[j][3]))
        signOfScore = sign(calc_vector_multi(w, input[j]))
        print("sign is: "+str(signOfScore))
        print("prediction is: "+str(signOfScore)+", true value is: "+str(input[j][3]))
        if signOfScore == input[j][3]:
            print("correct prediction, w is "+str(w))
            correct_count += 1
        else:
            w = update_weight(w, lRate, input[j], signOfScore)
            print("wrong prediction, new w is: "+str(w))
            correct_count = 0
        j += 1
        print()


main(inputOR) # OR function
main(inputNAND) # NAND function
main(inputXOR) # XOR function