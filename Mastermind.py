import random


def computer_choice_of_code() -> list:
    colors = ["red", "yellow", "blue", "green", "white", "black"]
    computer_choice = random.choices(colors, k=4)
    print(computer_choice)
    return computer_choice


def good_color_good_place(input_coder: list, input_decoder: list) -> tuple:
    count = 0
    unmatched_coder = []
    unmatched_decoder = []
    for i in range(len(input_coder)):
        if input_coder[i] == input_decoder[i]:
            count += 1
        else:
            unmatched_coder.append(input_coder[i])
            unmatched_decoder.append(input_decoder[i])
    return count, unmatched_coder, unmatched_decoder


def good_color_bad_place(unmatched_coder: list, unmatched_decoder: list) -> int:
    count = 0
    for color in unmatched_coder:
        if color in unmatched_decoder:
            count += 1
            unmatched_decoder.remove(color)
    return count


def compare_choices(input_coder: list, input_decoder: list) -> list:
    correct_position_count, unmatched_coder, unmatched_decoder = good_color_good_place(input_coder, input_decoder)
    correct_color_count = good_color_bad_place(unmatched_coder, unmatched_decoder)
    print(correct_position_count, correct_color_count)
    return [correct_position_count, correct_color_count]


solena_input = ["black", "blue", "yellow", "green"]

print(solena_input)
compare_choices(computer_choice_of_code(), solena_input)
