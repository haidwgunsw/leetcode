if __name__ == '__main__':
    n = int(input())  # Uncomment this line to read n from input
    numbers = [str(x) for x in range(1, n+1)]  # Generate numbers from 1 to n and convert to strings
    
    print(''.join(numbers))
    