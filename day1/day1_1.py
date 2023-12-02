# Open the file in read mode
file_path = "input1.txt"
file = open(file_path, "r")
file_contents = file.read()
file.close()

# Split the file contents into lines
lines = file_contents.split("\n")

arrayTotal = [];
for line in lines:
  # Create an array of digits and then take the first and last element
  arrayDigits = []
  for charact in line:
      if(charact.isdigit()):
        arrayDigits.append(charact)
  if(len(arrayDigits)>0):
    firstDigit = arrayDigits[0]
    lastDigit = arrayDigits[-1]
    finalString = str(firstDigit) + str(lastDigit)
    arrayTotal.append(int(finalString))

print(arrayTotal)
print(len(arrayTotal))

# Sum the array
sum = 0
for number in arrayTotal:
  sum += number
print(sum)


