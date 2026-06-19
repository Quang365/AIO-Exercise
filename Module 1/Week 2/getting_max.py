def max_kernel(num_list, k):
    start_indices = list(range(0, len(num_list) - k + 1))
    end_indices = list(range(k, len(num_list) + 1))

    result = []

    for start_index, end_index in zip(start_indices, end_indices):
        kernel = num_list[start_index:end_index]
        max_value = max(kernel)
        result.append(max_value)

    return result

print(max_kernel([3, 4, 5, 1, -44, 5, 10, 12 ,33 ,1], 3))