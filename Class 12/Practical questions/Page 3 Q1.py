import matplotlib.pyplot as plt
lang=['Java','Python','PHP','Java Script','C#','C++']
pop=[22.2,17.6,8.8,8,7.7,6.7]
plt.bar(lang,pop)
fig1,ax1=plt.subplots()
ax1.pie(pop,labels=lang,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()