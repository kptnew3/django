try:
    f = open("simple.txt", 'r')
    f.write("Back to writing to the file")

except Exception as e:
    print(str(e.errno))
    print(str(e.strerror))
    print("IO Error Occurred. Either file is not found or not allowed to write into it")
else:
    print("File Successfully Written")

# finally:
#     print("I always run regardless")
