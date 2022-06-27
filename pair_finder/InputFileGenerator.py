from random import randint

INPUT_SIZE = 50
NUMBER = 12
INPUT_FILEPATH = './txt_files/input.txt'


def generate():
    list_of_input_numbers = [randint(0, NUMBER) for _ in range(INPUT_SIZE)]

    with open(INPUT_FILEPATH, 'w') as outputStream:
        input_string = str(list_of_input_numbers).strip('[]')
        outputStream.write(input_string)
        # [output_stream.write(f'{number},') for number in list_of_input_numbers]
