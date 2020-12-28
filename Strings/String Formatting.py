def print_formatted(number):
    # your code goes here
    l=len(bin(number)[2:])
    for i in range(1,number+1):
        """res = []
        res.append(str(i).rjust(l))
        res.append(oct(i)[2:].rjust(l))
        res.append(hex(i)[2:].upper().rjust(l))
        res.append(bin(i)[2:].rjust(l))
        print(*res) """
        
        #one liner
        
        print(str(i).rjust(l)+' '+oct(i)[2:].rjust(l)+' '+hex(i)[2:].upper().rjust(l)+' '+bin(i)[2:].rjust(l)+' ')
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
