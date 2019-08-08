def centered_average(input):
    return sum(sorted(input)[1:-1]) / (len(input) - 2)


print(centered_average([1, 2, 3]))
print(centered_average([3, 2, 1]))
print(centered_average([1, 2, 3, 4]))
print(centered_average([1, 2, 4, 4]))
print(centered_average([-100, 2, 4, 6, 200]))
