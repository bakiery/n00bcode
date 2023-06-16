swim = int(input("enter time, in minutes, that it took you to swim: "))
cycle = int(input("enter time, in minutes, that it took you to cycle: "))
run = int(input("enter time, in minutes, that it took you to run: "))

total = swim + cycle + run
4
if total <= 100:
    print("AWARD: Provincial Colours")
elif total <= 105:
    print("AWARD: Provincial Half Colours")
elif total <= 110:
    print("AWARD: Provincial Scroll")
else:
    print("No award")