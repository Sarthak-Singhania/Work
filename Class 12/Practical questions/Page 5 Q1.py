import matplotlib.pyplot as plt
'''labels=[]
sizes=[]
for i in range(1,11):
    print('Entry number',i)
    labels.append(input('Enter the name of the state:'))
    sizes.append(int(input('Enter the population:')))'''

labels=['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand']
sizes=[20,15,5,20,15,15,20,30,10,5]
fig1,ax1=plt.subplots()
ax1.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
ax1.axis('equal')
plt.show()
