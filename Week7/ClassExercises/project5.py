def main():
    count = 0
    my_string = input("Enter a sentence: ")

    for ch in my_string:
        if ch == 't' or ch == 'T':
            count += 1
    print(f"The letter t appears {count} times.")

if __name__ == '__main__':
    main()