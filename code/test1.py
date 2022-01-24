import copy

def is_even(a) :
    if a%2 ==0:return True   
    else : return False

def condition(reference_list,copied_list):
    if is_even(len(reference_list)):return (len(copied_list)>0)
    else :return(len(copied_list)>1)

