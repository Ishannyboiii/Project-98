def swapFileData():
    i1 = input("What is the name of file 1? ")
    i2 = input("What is the name of file 2? ")
    file1 = open(i1)
    file2 = open(i2)
    data_a = file1.read()
    data_b = file2.read()
    with open(i1,"w") as file1:
        file1.write(data_b)
    with open(i2,"w") as file2:
        file2.write(data_a)
swapFileData()
