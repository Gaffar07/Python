import os
my_file = 'D:\Torrentzz\office.rar'
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.exe')