def main():
    with open("books/frankenstein.txt") as f:
        counter = 0
        file_contents = f.read()
        print(len(file_contents.split()))

if __name__ == "__main__":
    main()