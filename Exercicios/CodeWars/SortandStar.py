def two_sort(array):
    return '***'.join(sorted(array)[0])

word = two_sort(list(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
print(word)