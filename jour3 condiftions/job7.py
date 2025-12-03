text = "abcdefghijklmnopqrstuvwxyz" * 10   
index = 0     
n = 1          

while index + n <= len(text):               
    print(text[index:index + n])            
    index += n                              
    n += 2                                 