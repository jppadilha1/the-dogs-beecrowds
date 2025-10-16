num_words = int(input())
target_one = "one"

for _ in range(num_words):
    word = input()

    if len(word) == 5:
        print(3)
    else:
        matches = 0
        for i in range(3):
            if word[i] == target_one[i]:
                matches += 1
        
        if matches >= 2:
            print(1)
        else:
            print(2)