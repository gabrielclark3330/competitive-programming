n, s = [int(x) for x in input().split()]

cards = [int(x) for x in input().split()]

reversable_numbers = ("1", "2", "5", "6", "8", "9", "0")
reverse_number = {"1":"1", "2":"5", "5":"2", "6":"9", "8":"8", "9":"6", "0":"0"}

def numbers_add_to_s(numbers, s):
    hashes = {}
    is_index_flipped = set()

    for index, number in enumerate(numbers):
        hash_of_number = s-number
        hashes[hash_of_number] = index
        if is_card_reversable(number):
            hash_of_flipped_number = s-flip_number(number)
            hashes[hash_of_flipped_number] = index
            is_index_flipped.add(index)

    for index, number in enumerate(numbers):
        if is_card_reversable(number):
            flipped_number = flip_number(number)
            if flipped_number in hashes and hashes[flipped_number]!=index:
                return True

        if number in hashes and hashes[number]!=index:
                return True

    return False

def flip_number(number):
    new_number = ""
    for character in str(number):
        new_number = new_number + reverse_number[character]
    return int(new_number)

def is_card_reversable(number):
    for character in str(number):
        if character not in reversable_numbers:
            return False
    return True

#[2, 1] --> 7
if numbers_add_to_s(cards, s):
    print("YES")
else:
    print("NO")

