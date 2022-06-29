# from pair_finder.pair_finder_static import PairFinderStatic
import pair_finder

if __name__ == '__main__':
    # pair_finder_12 = PairFinder()
    # # pair_finder_12.sumOfNumbers = 12
    # pair_finder_12.run()
    pair_finder.Finder.run()

    #
    # # as a test
    # with open('./txt_files/input.txt', 'r') as inputStream:
    #     NUMBER = 12
    #     countNumbers = [0] * (NUMBER + 1)
    #     content = inputStream.read()
    #     listOfNumbers = content.split(',')
    #     for count, value in enumerate(listOfNumbers):
    #         listOfNumbers[count] = int(value)
    #
    #     for value in listOfNumbers:
    #         countNumbers[value] = countNumbers[value] + 1
    #
    #     print(countNumbers)
    #
    #     countPairs = [0] * (int(NUMBER / 2) + 1)
    #
    #     for count, value in enumerate(countPairs):
    #         countPairs[count] = min(countNumbers[count], countNumbers[NUMBER - count])
    #         if NUMBER % 2 == 0:
    #             countPairs[int(NUMBER/2)] = int(countPairs[int(NUMBER/2)]/2)
    #
    #     for count, value in enumerate(countPairs):
    #         print(f'Number of pairs {count}-{NUMBER - count}: {value}')

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

