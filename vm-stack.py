import re
import sys
#File_path = sys.argv[1]#when run script can give vm file
#do later auto make file for asm

def Constructer():#reads the vm file

    with open('VM-files/BasicTest.vm', 'r') as VM_code:
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

        self.command_type = command_type_dict[line.split()[0]] #gives the cammand type

        #gives the argmunets of the command
        if self.command_type is 'C_ARITHMATIC':
            self.arg1 = str(line.split()[0])
            self.arg2 = 'None'
        else:
            self.arg1 = str(line.split()[1])
            self.arg2 = int(line.split()[2])

class Code_writer:

    def open_file():
        asm_file =  open('BasicTest.asm','x')

    def write_arithmetic(command):
        arithmetic=[]

        same_for_all = ['@SP',
                        '@M=M-1',
                        'A=M']
        arithmetic.extend(same_for_all)

        asm_dict = {'not':'M=!M','neg':'M=-M'} #dic for small commands

        else_A = ['D=M',
                  '@SP',
                  'A=M-1']

        add_A=['M=M+D']
        sub_A=['M=M-D']
        or_A =['M=M|D']
        and_A=['M=M&D']

        rest_A=['D=M-D',
                '@true',
                'D;XXX',
                '@SP',
                '@A=M-1',
                '@M=-1',
                '@over',
                '@0;JMP',
                '(true)',
                '@SP',
                'A=M-1',
                'M=0',
                '(over)']

        eq_A=[A.replace('XXX','JEQ') for A in rest_A]
        lt_A=[A.replace('XXX','JLT') for A in rest_A]#check if corect comp <0
        gt_A=[A.replace('XXX','JGT') for A in rest_A]#comp>0

        if command in asm_dict:#doing the easy commands
            arithmetic.append(asm_dict[command])

        else:#doing hard commands
            arithmetic.extend(else_A)
            asm_dict.update({'add':add_A,'sub':sub_A,'or':or_A,'and':and_A,'eq':eq_A,'lt':lt_A,'gt':gt_A})
            arithmetic.extend(asm_dict[command])

        arithmetic = [line + ' \n' for line in arithmetic] #adding newline to each line
        return arithmetic

if __name__ == '__main__':
    code = Constructer()
    art=Code_writer.write_arithmetic('eq')
    print(art)
