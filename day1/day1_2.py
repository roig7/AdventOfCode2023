import re
# Open the file in read mode
file_path = "input2.txt"
file = open(file_path, "r")
file_contents = file.read()
file.close()

# Split the file contents into lines
lines = file_contents.split("\n")

arrayString = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',  'nine']
arrayNumber = [1, 2 , 3, 4, 5, 6, 7, 8, 9]
arrayTotal = [];

def convert_word_to_number(line):
    word_vals = [ ('one', '1'),
                  ('two', '2'),
                  ('three', '3'),
                  ('four', '4'),
                  ('five', '5'),
                  ('six', '6'),
                  ('seven', '7'),
                  ('eight', '8'),
                  ('nine', '9') ]

    new_line = ''
    for ix in range(len(line)):
        sub_made = False
        for wv in word_vals:
            word = wv[0]
            if line[ix:ix + len(word)] == word:
                new_line += wv[1]
                sub_made = True
                break
        if not sub_made:
            new_line += line[ix]
    return new_line


def get_calibration_value_with_number_after(line):
    # Add numbers after matching spelled out words in the original line
    modified_line = convert_word_to_number(line)

    # Extract the first and last digit from the modified line
    first_digit = next((char for char in modified_line if char.isdigit()), None)
    last_digit = next((char for char in reversed(modified_line) if char.isdigit()), None)

    return str(first_digit) + str(last_digit) if first_digit and last_digit else 0


for line in lines:
  arrayTotal.append(get_calibration_value_with_number_after(line))

print(arrayTotal)

# Sum the array
sum = 0
for number in arrayTotal:
  sum += int(number)
print(sum)


# Testsss
test_line = "onetwothree"
print(convert_word_to_number(test_line))
print(get_calibration_value_with_number_after(test_line))