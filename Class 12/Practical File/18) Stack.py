a=input('Enter a list of diameters:')
if ' ' in a:
    l=list(map(int,a.split()))
elif ',' in a:
    l=list(map(int,a.split(',')))
elif ', ' in a:
    l=list(map(int,a.split(', ')))
tmpl=[]
while len(l)!=0: 
    tmp=l[-1]
    l.pop()
    while len(tmpl)!=0 and tmpl[-1]>tmp: 
        l.append(tmpl[-1])
        tmpl.pop()
    tmpl.append(tmp)
print(tmpl)
