import textwrap

def wrap(string, max_width):
  return textwrap.fill(string, width=max_width)

if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', int(4)
    result = wrap(string, max_width)
    print(result)