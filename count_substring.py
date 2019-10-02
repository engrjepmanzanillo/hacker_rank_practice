#https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    # create a new array container
    new_list = []
    for i in range(len(string)):
        new_list.append(string[i:len(sub_string)+i])
    return new_list.count(sub_string)


if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'
    new_list = []
    print(count_substring(string, sub_string))
