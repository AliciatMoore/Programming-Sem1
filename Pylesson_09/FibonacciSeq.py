num = int(input("Please enter your starting number: "))
size = int(input("Please enter your sequence size: "))

seq = []

output = ""
for i in range(0, size):
    if i ==0 or i == 1:
        seq.append(num)
    else:
        seq.append(seq[i - 2] + seq[i - 1])
    output += str(seq[i]) + " "
print(output)
        
