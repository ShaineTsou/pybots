# This password checker uses Pwned Password API by Have I Been Pwned? (https://haveibeenpwned.com/API/v3#PwnedPasswords)
# Password is hashed by using sha1 method of Python built-in module hashlib (https://docs.python.org/3/library/hashlib.html)

# Usage: 'python3 checkmypass.py [file_name]'
# [file_name] file stores passwords line by line
import sys
import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_hash_count_from_response(hash_to_check, response):
    all_hash_count_pairs = (line.split(':')
                            for line in response.text.splitlines())
    for hash, count in all_hash_count_pairs:
        if hash_to_check == hash:
            return int(count)
    return 0


def get_password_leaks_count(password):
    # Get first 5 characters and the tail of hashed password
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]

    response = request_api_data(first5)

    return get_hash_count_from_response(tail, response)


def main(file):
    with open(file, 'r') as file:
        passwords = file.read().splitlines()

    for password in passwords:
        count = get_password_leaks_count(password)
        if count > 0:
            print(
                f'\'{password}\' was found {count} times... You should probably change your password')
        else:
            print(f'\'{password}\' was NOT found. Carry on!')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
