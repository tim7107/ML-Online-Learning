from scipy.special import comb

def calculate_ab(_list,a,b):
    cur_a,cur_b=0,0
    length=len(_list)
    _list=list(_list)
    for i in range(length):
        if _list[i]== '1':
            a+=1
            cur_a+=1
        else:
            b+=1
            cur_b+=1
    return (a,b,cur_a,cur_b)
"""
    Read the text file line by line 
    store into list
"""
fp=open('C:/Users/tim/Desktop/碩一/碩一下/ML/HW02/test.txt')
line = fp.readline()
content=[]

while(line):
    line=line.strip('\n')
    content.append(line)
    line=fp.readline()
fp.close

txt_length=len(content)

'''start=content[0]
it_a,it_b=calculate_ab(start,0,0)
it_p=float(it_a/(it_a+it_b))'''
"""
    Start to calculate
"""
prev_a,prev_b=0,0
p=float(0)
for i in range (txt_length):
    """
        Case i+1
    """
    print('case%d: %s' %(i+1,content[i]))
    """
        Beta prior
    """
    post_a,post_b,cur_a,cur_b=calculate_ab(content[i],prev_a,prev_b)
    p=float(cur_a/(cur_a+cur_b))
    Likelihood=comb(cur_a+cur_b,cur_a)*(p**cur_a)*((1-p)**cur_b)
    print('Likelihood: %f' %(Likelihood))
    
    print('Beta Prior: a=%d b=%d' %(prev_a,prev_b))
    prev_a,prev_b=post_a,post_b
    if i+1!=txt_length:
        print('Beta Postirior: a=%d b=%d' %(post_a,post_b))
    print('\n')
    