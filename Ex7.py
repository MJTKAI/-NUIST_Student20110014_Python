def studList():
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    for name in studentNames:
        print(f"{name} Evans")
    return studentNames


def addToList():
    studentNames = studList()
    new_name = input("Please enter a new name to add to : ")
    studentNames.append(new_name)
    for name in studentNames:
        print(f"{name} Evans")


if __name__ == "__main__":
    addToList()
    
