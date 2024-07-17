calls = 0
def count_calls():
    global calls
    calls += 1
def string_info (string):
    count_calls()
    len_ = len(string)
    upper_ = string.upper()
    lower_ = string.lower()
    return (len_, upper_, lower_)

def is_contains (string, list_to_search):
    count_calls()
    string_upper = string.upper()
    list_s_up = [num.upper() for num in list_to_search]
    return string_upper in list_s_up


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print("Количество вызовов функций", calls)