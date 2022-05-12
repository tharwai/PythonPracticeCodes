def fibona (n):
    if n <= 1 : return 1
    else: return fibona(n-1)+fibona(n-2)
print (fibona ( 5 ) )