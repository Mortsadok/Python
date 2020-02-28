Id_num = input("Please insert your ID:")
OneSum = 0

while len(Id_num) != 8:
    Id_num = input("Please insert your ID:")

for x in range(0, len(Id_num)):
    if x % 2 == 0:
        OneSum += int(Id_num[x])

    if x % 2 != 0:
        if (int(Id_num[x]) * 2) > 9:
            BigThen = (int(Id_num[x]) * 2)
            while int(BigThen >= 1):
                OneSum += int(BigThen % 10)
                BigThen /= 10
        else:
            OneSum += (int(Id_num[x]) * 2)

Review_num = 10 - (OneSum % 10)

if Review_num == 10:
    print(Id_num + " 0")
else:
    print(Id_num, Review_num)
