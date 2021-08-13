def is_palindrome(string: str) -> bool :
        string = string.replace(" ","").lower()
        return string == string[::-1]


def run():
    print(is_palindrome(1))


run()