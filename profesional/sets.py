# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    whithot_duplicates = []
    for element in some_list:
        if element not in whithot_duplicates:
            whithot_duplicates.append(element)
    return whithot_duplicates

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

run()