import os
import time

print(os.getcwd())
os.chdir('E:\\Projekty\\python_wyklad\\exercise')
print(os.getcwd())
os.mkdir('new_folder')
time.sleep(2)
os.rename('new_folder', 'new_folder2')
time.sleep(2)
os.rmdir('new_folder2')