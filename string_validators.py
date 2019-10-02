#https://www.hackerrank.com/challenges/string-validators/problem
# string has any alphanumerics
def has_any_alnum(string):
  string_list = []
  for i in range(len(string)):
    string_list.append(string[i].isalnum())
  return any(string_list)

# string has any alphabeticals
def has_any_alpha(string):
  string_list = []
  for i in range(len(string)):
    string_list.append(string[i].isalpha())
  return any(string_list)

# string has any digits
def has_any_digit(string):
  string_list = []
  for i in range(len(string)):
    string_list.append(string[i].isdigit())
  return any(string_list)

# string has any lowercase
def has_any_lower(string):
  string_list = []
  for i in range(len(string)):
    string_list.append(string[i].islower())
  return any(string_list)

# string has any uppercase
def has_any_upper(string):
  string_list = []
  for i in range(len(string)):
    string_list.append(string[i].isupper())
  return any(string_list)

if __name__ == '__main__':
    s = 'qA2'
    print(has_any_alnum(s))
    print(has_any_alpha(s))
    print(has_any_digit(s))
    print(has_any_lower(s))
    print(has_any_upper(s))