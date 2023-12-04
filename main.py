with open('1.txt', "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)


author = input("Хто написав ці рядки? ")
with open('1.txt', "a", encoding = "UTF-8") as file:
    file.write(f"({author})\n")

while True:
    answer = input("Бажаєте додати че одну цитату? (так/ні)")
    answer = answer.lower()
    if answer == "Так":
        quote = input("Введить цитатуЖ ")
        author = input("введіть автора: ")
        file = open("1.txt", "a", encoding = "UTF-8")
        file.write(f"{1}\n({author})\n")
        file.close()
    else:
        break

with open('1.txt', "r", encoding= "UTF-8") as file:
    for line in file:
        print(line)

