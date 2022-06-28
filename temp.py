# from random import randint
#
# INPUT_SIZE = 100
# NUMBER = 12
#
# input = [randint(0, NUMBER) for i in range(INPUT_SIZE)]
# print(input)
#
# countNumbers = [0] * (NUMBER + 1)
#
# for value in input:
#     countNumbers[value] = countNumbers[value] + 1
#
# print(countNumbers)
#
# countPairs = [0] * (int(NUMBER/2)+1)
#
# for count, value in enumerate(countPairs):
#     countPairs[count] = min(countNumbers[count], countNumbers[NUMBER-count])
#
# for count, value in enumerate(countPairs):
#     print(f'Number of pairs {count}-{NUMBER-count}: {value}')

print(type(int(float('0.0'))))
