import copy

def is_even(a) :
    if a%2 ==0:return True   
    else : return False

def condition(reference_list,copied_list):
    if is_even(len(reference_list)):return (len(copied_list)>0)
    else :return(len(copied_list)>1)

test = ['a','b','c','d','f']

print(len(test))
for i in range(0, int(len(test)/2)):
     print(f'1er retrait: {test.pop(0)} 2eme retrait {test.pop(0)}')
     print(test)
     print(len(test))

