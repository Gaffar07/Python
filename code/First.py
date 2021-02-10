import matplotlib.pyplot as plt

values=[10,20,40,50]
languages=["java","C++","Scala","GO"]

plt.bar(range(4),values)
plt.xticks(range(4),languages)
plt.title("programming geeks")
plt.show()