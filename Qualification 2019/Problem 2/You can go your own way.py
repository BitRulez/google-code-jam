def same_direction(input_path):
    """
    1st_dir = The first direction of the input_path
    not_1st_dir = The opposite direction of 1st

    Search for the first occurrence of two consecutive not_1st_dir letters in the input string.

    Every time a not_1st_dir char is found it will be added to the output string.
    Only the first one of the two consecutive not_1st_dir will be added to the output string.

    Add to the output string 1st_dir until the end of the matrix.
    Add to the output string not_1st_dir until the end of the matrix.

    :param input_path: User's input path
    :return: The output path
    """
    two_in_a_row = 0
    output_path = ""
    input_first_direction = input_path[0]

    if input_first_direction == "E":
        opposite_direction = "S"
    else:
        opposite_direction = "E"

    for i, char in enumerate(input_path):
        if input_path[i] == opposite_direction:
            two_in_a_row = two_in_a_row + 1
            if two_in_a_row < 2:
                output_path = output_path + opposite_direction
            else:
                count_of_other_letter = (max_moves_same_dir - len(output_path))
                output_path = output_path + input_first_direction * max_moves_same_dir + opposite_direction * count_of_other_letter
                break
        else:
            two_in_a_row = 0

    return output_path


cases_count = int(input())

list_of_matrix_width = []
list_of_input_path = []
for i in range(0, cases_count):
    list_of_matrix_width.append(int(input()))
    list_of_input_path.append(list(input()))

for i, input_path in enumerate(list_of_input_path):

    max_moves_same_dir = list_of_matrix_width[i] - 1

    if input_path[0] == input_path[len(input_path) - 1]:
        if input_path[0] == "S":
            print("Case #{}: {}".format(i + 1, same_direction(input_path)))

        elif input_path[0] == "E":
            print("Case #{}: {}".format(i + 1, same_direction(input_path)))

    elif input_path[0] != input_path[len(input_path) - 1]:
        if input_path[0] == "S" and input_path[len(input_path) - 1] == "E":
            output_path = ("E" * max_moves_same_dir + "S" * max_moves_same_dir)
            print("Case #{}: {}".format(i + 1, output_path))

        elif input_path[0] == "E" and input_path[len(input_path) - 1] == "S":
            output_path = ("S" * max_moves_same_dir + "E" * max_moves_same_dir)
            print("Case #{}: {}".format(i + 1, output_path))
