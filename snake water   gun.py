import random
print("\t \t Welcome in Snake Water Gun\a")
comp_score = 0
your_score = 0
list = ["S","W","G"]
comp = 0
you = 0
i = 1
while(i<=5):
    print("Print S(Snake),W(Water),G(Gun)")
    your_input = input()
    comp_choise = random.choice(list)
    your_input = your_input.capitalize()
    if(comp_choise == "S" and your_input == "S" or comp_choise == "W" and your_input == "W" or comp_choise == "G" and your_input == "G"):
        print("Draw")
        print(f"your_input = {your_input}")
        print(f"comp_choise = {comp_choise}")
    elif(comp_choise == "G" and your_input == "S"):
        print("You Loose")
        print(f"your_input = {your_input}")
        print(f"comp_choise = {comp_choise}")
        comp_score =  comp_score +1
    elif (comp_choise == "S" and your_input == "G"):
        print("You Win")
        print(f"your_input = {your_input}")
        print(f"comp_choise = {comp_choise}")
        your_score = your_score + 1
    elif (comp_choise == "S" and your_input == "W"):
        print("You Loose")
        print(f"your_input = {your_input}")
        print(f"comp_choise = {comp_choise}")
        comp_score = comp_score + 1
    elif (comp_choise == "W" and your_input == "S"):
        print("You Win")
        print(f"your_input = {your_input}")
        print(f"comp_choise = {comp_choise}")
        your_score = your_score + 1
    elif (comp_choise == "W" and your_input == "G"):
        print("You Loose")
        print(f"your_input = {your_input}")
        print(f"comp_choise = {comp_choise}")
        comp_score = comp_score + 1
    elif (comp_choise == "G" and your_input == "W"):
        print("You Win")
        print(f"your_input = {your_input}")
        print(f"comp_choise = {comp_choise}")
        your_score = your_score + 1
    i = i+1

print("\t\t\t Final Score \t\t\t")

if(comp_score<your_score):
    print("\t\tCongratulation ! You Win\t")
    print(f"\t\tyour_score = {your_score}")
    print(f"\t\tcomp_score = {comp_score}")
elif(comp_score>your_score):
    print("\tSorry ! You Loose try next time\t")
    print(f"\t\tyour_score = {your_score}")
    print(f"\t\tcomp_score = {comp_score}")
else:
    print("\t\tMatch Draw")
    print(f"\t\tyour_score = {your_score}")
    print(f"\t\tcomp_score = {comp_score}")
a = input()