sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for i in range(100):
    print("Hi!,Please Answer The Following Questions!")
    print("\n")
    activity1 = int(input("Enter The Number Of Books You've Read For This Month: "))
    activity2 = int(input("Enter The Number Of Movies You Went To  For This Month: "))
    activity3 = int(input("Enter The Number Of Parties You Went For This Month: "))
    if activity1 > 0 and activity2 > 0 and activity3 > 0:
        sum1 = sum1 + 1
    if activity1 == 0 or activity2 == 0 or activity3 == 0:
        sum2 = sum2 + 1
    if activity1 > 0:
        sum3 = sum3 + 1
    sum4 = sum4 + activity1
    print("\n")
    print("Thank You!")
    print("\n")
print("The Number Of Students That Participated In All 3 Activities is :", sum1)
print("The Number Of Students That Participated In Only 2 Activities is :", sum2)
print("The Number Of Students That Read At Least 1 Book Is :", sum3)
print(sum4, "Is The Amount Of Books That Were Read In Total")
