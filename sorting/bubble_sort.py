class BubbleSort():

    # filter for integers
    def __filter_list(self, array):
        filtered_list = []
        for item in array:
            if isinstance(item, int):
                filtered_list.append(item)
        return filtered_list

    # flatten list
    def __flatten_list(self, array):
        if len(array) == 0:
            return array
        if isinstance(array[0], list):
            return self.__flatten_list(array[0]) + self.__flatten_list(array[1:])
        return array[:1] + self.__flatten_list(array[1:])

    # bubble sort
    def bubble_sort(self, array: list, max_length: int):
        if len(array) > max_length:
            raise ValueError(f'Elements must be less then {max_length}')
        flat_list = self.__flatten_list(array)
        filtered_list = self.__filter_list(flat_list)
        n = len(filtered_list)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if filtered_list[j] > filtered_list[j + 1]:
                    filtered_list[j], filtered_list[j+1] = filtered_list[j+1], filtered_list[j]
        return filtered_list
