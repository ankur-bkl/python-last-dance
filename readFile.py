
# txtFile =open("file.txt","a+")
# txtFile.write("\nKya Bawasir Banaya Hai")
# txtFile.seek(0)
# txtFile.close()  
# print(txtFile.read())
txtFile =open("file.txt","r")
print(txtFile.readlines())
txtFile.close()