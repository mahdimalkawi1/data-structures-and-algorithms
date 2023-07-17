class MergeSort:
    def sort(self, arr):
        self.merge_sort(arr)

    def merge_sort(self, arr):
        n = len(arr)

        if n > 1:
            mid = n // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            self.merge(left, right, arr)

    def merge(self, left, right, arr):
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
