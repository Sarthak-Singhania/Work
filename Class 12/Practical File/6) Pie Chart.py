import matplotlib.pyplot as plt
labels=[]
sizes=[]
for i in range(1,11):
    print('Entry number',i)
    labels.append(input('Enter the name of the country:'))
    sizes.append(int(input('Enter the population:')))
fig1,ax1=plt.subplots()
ax1.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()
