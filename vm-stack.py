import re

def Constructer():#reads the vm file

    with open('VM-files/BasicTest.vm') as VM_code:
        code = VM_code.readlines()

    code = [line.replace('\n','') for line in code] #remove newline
    return code







if __name__ == '__main__':
    code = Constructer()
    print(code)
