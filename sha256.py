
# written by Mohammad.Amin.Kiani

import hashlib

''' --------------------------------------------------------------------------- '''

fp_hashed = open("hashed_passwords.txt" , 'r') # GET
lines_hashed = fp_hashed.readlines()

# ==============================================

fp_opened = open("opened_passwords.txt" , 'w')  # PUT

# ==============================================

for line in lines_hashed :
    user = [i.strip() for i in line.split(',')]  # < class list >
    name = user[0]         # < class str >
    password = user[1]     # < class str >
    
    l = list(range(1000,10000))
    all_pass = {i:hashlib.sha256(str(i).encode("utf8")).hexdigest() for i in l}  # dict { i : hash.i }
    
    for key,value in all_pass.items():
        if password == value :
            fp_opened.write('%s,%s\n' % (name, key))
            

fp_opened.close()
            
fp_hashed.close()

''' --------------------------------------------------------------------------- '''