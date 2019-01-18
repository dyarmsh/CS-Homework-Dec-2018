def armstrong():
     for n in range(100, 501):
         n1 = int(n%10)
         nn2 = int(n/10)
         n2 = int(nn2%10)
         n3 = int(nn2/10)
         cube_sum = n1**3 + n2**3 + n3 **3
         if cube_sum == n:
            armstrong_no = n
            print(armstrong_no)
        
armstrong()
