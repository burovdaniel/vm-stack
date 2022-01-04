import re

def Constructer():#reads the vm file

    with open('VM-files/BasicTest.vm') as VM_code:
        code = VM_code.readlines()

    code = [line.replace('\n','') for line in code] #remove newline
    code = [line for line in code if not line.startswith('//')]#removes comments
    code = [line for line in code if not line is  '']
    return code


class Parser:

    def __init__(self,line):

        #dict for the command type
        command_type_dict = {'pop':'C_POP','push':'C_PUSH'}
        command_type_dict.update(dict.fromkeys(['eq','sub','neg','add','gt','lt','and','or','not'],'C_ARITHMATIC'))

        self.command_type = command_type_dict[line.split()[0]]

if __name__ == '__main__':
    code = Constructer()
    for line in code:
        line = Parser(line)
        print(line.command_type)
