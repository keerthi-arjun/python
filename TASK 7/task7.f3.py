class SumToZero:
    def __init__(self, numbers):
        self.numbers = numbers
        
    def find_triplets(self):
        self.numbers.sort()
        triplets = []
        for i in range(len(self.numbers) - 2):
            if i > 0 and self.numbers[i] == self.numbers[i - 1]:
                continue
            left = i + 1
            right = len(self.numbers) - 1
            while left < right:
                current_sum = self.numbers[i] + self.numbers[left] + self.numbers[right]
                if current_sum == 0:
                    triplets.append([self.numbers[i], self.numbers[left], self.numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and self.numbers[left] == self.numbers[left - 1]:
                        left += 1
                    while left < right and self.numbers[right] == self.numbers[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return triplets

numbers = [-25,-10,-7,-3,2,4,8,10]
sum_to_zero = SumToZero(numbers)
print("Triplets that sum to zero:", sum_to_zero.find_triplets())
    