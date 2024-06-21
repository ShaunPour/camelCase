def main():
    Input_Container = input("camelCase: ")
    arr = []

    for letter in Input_Container:
        if letter.isupper():
            arr.append('_')
            arr.append(letter.lower())
        else:
            arr.append(letter)

    print("snake_case: " + ''.join(arr))
main()
