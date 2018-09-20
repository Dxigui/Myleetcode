def NumberOf1(n):
        # write code here
        bin_n = bin(n)
        print(bin_n)
        if bin_n[0] == '-':
            int_n = int(bin_n[3:])
            
            return bin_n[3:].replace('1', '2').replace('0', '1').count('1') + 1
        else:
            return bin_n.count('1')


if __name__ == '__main__':
    print(NumberOf1(-2147483648))
