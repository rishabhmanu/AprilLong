# def get_all_substrings(string):
#   length = len(string)
#   alist = []
#   for i in range(length):
#     for j in range(i,length):
#       alist.append(string[i:j + 1]) 
#   return alist

# print(get_all_substrings('abb'))

def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

# print(get_all_substrings('abb'))

l = get_all_substrings('abb')
l1 = set(l)
l1 = list(l1)
