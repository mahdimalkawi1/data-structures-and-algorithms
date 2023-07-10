class InsertionSort:
    def __init__(self, input):
        self.input = input

    def sort(self):
        if len(self.input) == 0:
            return []

        sorted_array = [self.input[0]]
        for i in range(1, len(self.input)):
            self.insert(sorted_array, self.input[i])
        return sorted_array

    @staticmethod
    def insert(sorted_array, value):
        i = 0
        while i < len(sorted_array) and value > sorted_array[i]:
            i += 1

        sorted_array.insert(i, value)


sample_array = [8, 4, 23, 42, 16, 15]
insertion_sort = InsertionSort(sample_array)
sorted_result = insertion_sort.sort()
print("Sorted array:", sorted_result)
