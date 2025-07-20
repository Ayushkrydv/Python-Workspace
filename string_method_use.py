alpha = 'abcdefghijklmnopqrstuvwxyz'
n = 'manish'
t = ''#nbojti
i = 0
k=1
#print(alpha.index(n[i]))
t=t+(alpha[((alpha.index(n[i])+k)%26)])
t=t+(alpha[((alpha.index(n[i+1])+k)%26)])
t=t+(alpha[((alpha.index(n[i+2])+k)%26)])
t=t+(alpha[((alpha.index(n[i+3])+k)%26)])
t=t+(alpha[((alpha.index(n[i+4])+k)%26)])
t=t+(alpha[((alpha.index(n[i+5])+k)%26)])
print(t)
