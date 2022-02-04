def letterCombination(digit):
    if digit == "":
        return []
    stringData = {
        "1": "suneel",
        "2": "aditya",
        "3": "arjun",
        "4": "ravi",
        "5": "abhishek",
        "6": "shivam",
        "7": "vijay",
        "8": "raju",
        "9": "rituraj"
    }
    result = [""]
    for num in digit:
        temp = []
        for an in result:
            for char in stringData[num]:
                temp.append(an + char)
        result = temp
    return result


string = "51"
print(letterCombination(string))
