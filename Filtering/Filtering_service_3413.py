def filtering(lst, condition):
 result = [i for i in lst if condition(i)]
 return result
