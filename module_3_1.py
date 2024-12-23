calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    line = str(string)
    result = (len(line), line.upper(), line.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Fox'))
print(string_info('Armagedon'))
print(is_contains('cycle', ['recycling', 'cyclic', 'sphere']))
print(is_contains('Urban', ['BAN', 'urBAN', 'BaBan']))

print(calls)