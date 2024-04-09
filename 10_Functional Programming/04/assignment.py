try:
    stream = open(
        "C:\\Users\\harliant001\\POC_Sem2_Assignments\\10_Functional Programming\\04\\assignment.py")
    stream.write('This is the first sentence\n')
    stream.close()
except Exception as e:
    print('An error occurred:', e)
    