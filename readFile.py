
txtFile =open("file.txt","a+")
txtFile.write("\nKya Bawasir Banaya Hai")
txtFile.seek(0)
print(txtFile.readlines())
txtFile.close()  