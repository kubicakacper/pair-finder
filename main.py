from PairFinder import PairFinder

if __name__ == '__main__':
    instance1 = PairFinder()
    # instance1.sumOfNumbers = 12
    instance1.run()

    # as a test
    with open('./input.txt', 'r') as inputStream:
        NUMBER = 12
        countNumbers = [0] * (NUMBER + 1)
        content = inputStream.read()
        listOfNumbers = content.split(',')
        for count, value in enumerate(listOfNumbers):
            listOfNumbers[count] = int(value)

        for value in listOfNumbers:
            countNumbers[value] = countNumbers[value] + 1

        print(countNumbers)

        countPairs = [0] * (int(NUMBER / 2) + 1)

        for count, value in enumerate(countPairs):
            countPairs[count] = min(countNumbers[count], countNumbers[NUMBER - count])
            if NUMBER % 2 == 0:
                countPairs[int(NUMBER/2)] = int(countPairs[int(NUMBER/2)]/2)

        for count, value in enumerate(countPairs):
            print(f'Number of pairs {count}-{NUMBER - count}: {value}')




    # input = [random.randint(0, NUMBER) for i in range(INPUT_SIZE)]
    # # print(input)
    # countNumbers = [0] * (NUMBER + 1)
    # # print(counterOfNumbers)
    # # counterOfNumbers[i] = counterOfNumbers[i]+1) for i in input
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




    # for count, value in enumerate(countPairs):
    #     for i in range(value):
    #         print(f'[{count},{NUMBER-count}],')


# class Geeks:
#     def __init__(self):
#         self._age = 0
#
#     # using property decorator
#     # a getter function
#     @property
#     def age(self):
#         print("getter method called")
#         return self._age
#
#     # a setter function
#     @age.setter
#     def age(self, a):
#         if (a < 18):
#             raise ValueError("Sorry you age is below eligibility criteria")
#         print("setter method called")
#         self._age = a
#
# mark = Geeks()
#
# mark.age = 19 
#
# print(mark.age)
#
#     string = '4.4,5,7,3'
#     list = string.split(',')
#     list[0] = int(list[0])
#     print(type(list[0]))
#     print(list[0])
