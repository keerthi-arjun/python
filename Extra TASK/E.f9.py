def count_char(string, char):
  count = 0
  for c in string:
    if c == char:
      count += 1
  return count

string = input("Enter a string: ")
char = input("Enter a character to count occurrences: ")

occurrences = count_char(string, char)
print("Number of occurrences of '" + char + "': " + str(occurrences))
