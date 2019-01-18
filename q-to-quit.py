#allowing user input of 'q' to terminate the program:
add = 0 
prod = 1
cnt = 0 

while True:
    num = input('ENTER NUMBER:')
    if num == 'q': break
    num = int(num)
    add = add + num
    prod = prod * num
    cnt += 1
    avg = add/cnt

print('AVERAGE:', avg)
print('PRODUCT:', prod)
