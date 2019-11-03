#######################################################
## Assembler - MIPS_32bits. Made By: Tarlison Sander ##
#######################################################

#######################################################
     # Dictionaries with Opcode and Registers#
#######################################################
#Opcode + rs + rt + rd + Offset
Memory_Acess = {
    'LB': '100000', 'LBU': '100100', 'LH': '100001', 'LBU': '100101',
    'LW': '100011', 'SB' : '101000', 'SH': '101001', 'SW' : '101011'
}
#Opcode + rs + rt + rd + Shamt + Funct
Arithmetic_and_Shifter = {
    'ADD' : '000000', 'ADDU': '000000', 'AND' : '000000', 'NOR' : '000000',
    'OR'  : '000000', 'SLT' : '000000', 'SLTU': '000000', 'SUB' : '000000',
    'SUBU': '000000', 'XOR' : '000000', 'SLLV': '000000', 'SRAV': '000000',
    'SRLV': '000000', 'SLL' : '000000', 'SRA' : '000000', 'SRL' : '000000'
}
#Opcode + rs + rt + Immediate
Arithmetic_and_Shifter_with_Immediate = {
    'ADDI': '001000', 'ADDIU': '001001', 'ANDI' : '001100', 'LUI' : '001111',
    'ORI' : '001101', 'SLTI' : '001010', 'STLIU': '001011', 'XORI': '001110'
}
#Opcode + rs + rt + Offset
Branches = {
    'BEQ' : '000100', 'BGEZ': '000001', 'BGEZAL': '000001', 'BGTZ': '000111',
    'BLEZ': '000110', 'BLTZ': '000001', 'BLTZAL': '000001', 'BNE' : '000101'
}
#No repetitive pattern
Jumps_Div_Mult_And_System = {
    'DIV'  : '000000', 'DIVU': '000000', 'MFHI': '000000', 'MFLO'   : '000000',
    'MTHI' : '000000', 'MTLO': '000000', 'MULT': '000000', 'MULTU'  : '000000',
    'BREAK': '000000', 'J'   : '000010', 'JAL' : '000011', 'JALR'   : '000000',
    'JR'   : '000000', 'MFC0': '010000', 'MTC0': '010000', 'SYSCALL': '00000000000000000000000000001100'
}
#Registers 0 - 31
Registers = {
    '$ZERO': '00000', '$AT': '00001', '$V0': '00010', '$V1': '00011', '$A0': '00100', '$A1': '00101', '$A3': '00110', '$A4': '00111',
    '$T0'  : '01000', '$T1': '01001', '$T2': '01010', '$T3': '01011', '$T4': '01100', '$T5': '01101', '$T6': '01110', '$T7': '01111',
    '$S0'  : '10000', '$S1': '10001', '$S2': '10010', '$S3': '10011', '$S4': '10100', '$S5': '10101', '$S6': '10110', '$S7': '10111',
    '$T8'  : '11000', '$T9': '11001', '$K0': '11010', '$K1': '11011', '$GP': '11100', '$SP': '11101', '$FP': '11110', '$RA': '11111',
}

#######################################################
def Add_Memory_Acess(code_without_comments, binary_file, i):
    try:
        for iterator in range(0, len(code_without_comments[i])):
            data = Memory_Acess.get(code_without_comments[i][iterator])
            if (data):
                binary_file.write(data)
            else:
                data = code_without_comments[i][iterator]
                if '(' in data:
                    aux = code_without_comments[i][iterator].replace('(', ' ')
                    data = aux.replace(')', '')
                    data = data.split()
                    v1 = int(data[0])
                    v1 = format(v1, '016b')  #convert to bin, with 16bits
                    binary_file.write(v1)
                    binary_file.write(Registers.get(data[1]))  #write the register
                else:
                    data = Registers.get(code_without_comments[i][iterator])
                    binary_file.write(data)
    except (AttributeError, TypeError) as e:
        print("Error occurred:", e) 
#######################################################
def write_registers_shamt_funct(binary_file, shamt, funct, i):
    try:
        for iterator in range(1, len(code_without_comments[i])):
            data = Registers.get(code_without_comments[i][iterator])
            binary_file.write(data)
        binary_file.write(shamt)
        binary_file.write(funct)
    except (AttributeError, TypeError) as e:
        print("Error occurred:", e) 
#######################################################
def Add_Arithmetic_and_Shifter(code_without_comments, binary_file, i):
    try:
        shamt = '00000'
        if code_without_comments[i][0] == 'ADD':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '100000'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'ADDU':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '100001'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'AND':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '100100'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'NOR':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '100111'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'OR':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '100101'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'SLT':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '101010'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'SLTU':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '101011'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'SUB':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '100010'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'SUBU':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '100011'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'XOR':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '100110'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'SLLV':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '000100'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'SRAV':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '000111'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        if code_without_comments[i][0] == 'SRLV':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            funct = '000110'
            write_registers_shamt_funct(binary_file, shamt, funct, i)

        #From here, operations occur a little differently
        if code_without_comments[i][0] == 'SLL':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            binary_file.write('00000')
            binary_file.write(Registers.get(code_without_comments[i][1]))
            binary_file.write(Registers.get(code_without_comments[i][2]))
            binary_file.write(format(int(code_without_comments[i][3]), '05b'))
            binary_file.write('000000')

        if code_without_comments[i][0] == 'SRA':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            binary_file.write('00000')
            binary_file.write(Registers.get(code_without_comments[i][1]))
            binary_file.write(Registers.get(code_without_comments[i][2]))
            binary_file.write(format(int(code_without_comments[i][3]), '05b'))
            binary_file.write('000011')

        if code_without_comments[i][0] == 'SRL':
            binary_file.write(Arithmetic_and_Shifter.get(code_without_comments[i][0]))
            binary_file.write('00000')
            binary_file.write(Registers.get(code_without_comments[i][1]))
            binary_file.write(Registers.get(code_without_comments[i][2]))
            binary_file.write(format(int(code_without_comments[i][3]), '05b'))
            binary_file.write('000010')
    except (AttributeError, TypeError) as e:
        print("Error occurred:", e) 
#######################################################
def Add_Arithmetic_and_Shifter_with_Immediate(code_without_comments, binary_file, i):
    try:
        binary_file.write(Arithmetic_and_Shifter_with_Immediate.get(code_without_comments[i][0]))  #Opcode
        binary_file.write(Registers.get(code_without_comments[i][1]))  #rs
        binary_file.write(Registers.get(code_without_comments[i][2]))  #rt
        binary_file.write(format(int(code_without_comments[i][3]),'016b'))  #Immediate
    except (AttributeError, TypeError) as e:
        print("Error occurred:", e) 
#######################################################
def Add_Branches(code_without_comments, binary_file, labels, i):
    try:
        if code_without_comments[i][0] == 'BNE' or code_without_comments[i][0] == 'BEQ':
            binary_file.write(Branches.get(code_without_comments[i][0]))  #Opcode
            binary_file.write(Registers.get(code_without_comments[i][1]))  #rs
            binary_file.write(Registers.get(code_without_comments[i][2]))  #rt
            for x in range(0, len(labels)):
                if code_without_comments[i][3] == labels[x]:
                    data = labels[x + 1]
                    binary_file.write(format(data, '016b'))
        else:  #Here, every instruction have a own rt

            if code_without_comments[i][0] == 'BGEZ':
                binary_file.write(Branches.get(code_without_comments[i][0]))  #Opcode
                binary_file.write(Registers.get(code_without_comments[i][1]))  #rs
                binary_file.write('00001')  #rt == 00000
                for x in range(0, len(labels)):
                    if code_without_comments[i][2] == labels[x]:
                        data = labels[x + 1]
                        binary_file.write(format(data, '016b'))

            if code_without_comments[i][0] == 'BGEZAL':
                binary_file.write(Branches.get(code_without_comments[i][0]))  #Opcode
                binary_file.write(Registers.get(code_without_comments[i][1]))  #rs
                binary_file.write('10001')  #rt == 00000
                for x in range(0, len(labels)):
                    if code_without_comments[i][2] == labels[x]:
                        data = labels[x + 1]
                        binary_file.write(format(data, '016b'))

            if code_without_comments[i][0] == 'BGTZ' or code_without_comments[i][0] == 'BLEZ' or code_without_comments[i][0] == 'BLTZ':
                binary_file.write(Branches.get(code_without_comments[i][0]))  #Opcode
                binary_file.write(Registers.get(code_without_comments[i][1]))  #rs
                binary_file.write('00000')  #rt == 00000
                for x in range(0, len(labels)):
                    if code_without_comments[i][2] == labels[x]:
                        data = labels[x + 1]
                        binary_file.write(format(data, '016b'))

            if code_without_comments[i][0] == 'BLTZAL':
                binary_file.write(Branches.get(code_without_comments[i][0]))  #Opcode
                binary_file.write(Registers.get(code_without_comments[i][1]))  #rs
                binary_file.write('10000')  #rt == 00000
                for x in range(0, len(labels)):
                    if code_without_comments[i][2] == labels[x]:
                        data = labels[x + 1]
                        binary_file.write(format(data, '016b'))
    except (AttributeError, TypeError) as e:
        print("Error occurred:", e) 
#######################################################
def Add_Jumps_Div_Mult_And_System(code_without_comments, binary_file, labels, i):
    try:
        if code_without_comments[i][0] == 'DIV' or code_without_comments[i][0] == 'DIVU':
            binary_file.write(Jumps_Div_Mult_And_System.get(code_without_comments[i][0])) #Opcode
            binary_file.write(Registers.get(code_without_comments[i][1])) #rs
            binary_file.write(Registers.get(code_without_comments[i][2])) #rt
            if code_without_comments[i][0] == 'DIV':
                binary_file.write('0000000000011010') #shamt + funct
            else:
                binary_file.write('0000000000011011') #shamt + funct

        if code_without_comments[i][0] == 'MFHI' or code_without_comments[i][0] == 'MFLO':
            if code_without_comments[i][0] == 'MFHI':
                binary_file.write('0000000000000000') #opcode + rs
                binary_file.write(Registers.get(code_without_comments[i][1])) #rd
                binary_file.write('00000010000') #shamt + funct
            else:
                binary_file.write('0000000000000000') #opcode + rs
                binary_file.write(Registers.get(code_without_comments[i][1])) #rd
                binary_file.write('00000010010') #shamt + funct

        if code_without_comments[i][0] == 'MTHI' or code_without_comments[i][0] == 'MTLO':
            if code_without_comments[i][0] == 'MTHI':
                binary_file.write('000000') #opcode 
                binary_file.write(Registers.get(code_without_comments[i][1])) #rs
                binary_file.write('000000000000000010001') #shamt + funct
            else:
                binary_file.write('0000000000000000') #opcode 
                binary_file.write(Registers.get(code_without_comments[i][1])) #rs
                binary_file.write('000000000000000010011') #shamt + funct

        if code_without_comments[i][0] == 'MULT' or code_without_comments[i][0] == 'MULTU':
            binary_file.write('000000') #opcode 
            if code_without_comments[i][0] == 'MULT':
                binary_file.write(Registers.get(code_without_comments[i][1])) #rs
                binary_file.write(Registers.get(code_without_comments[i][2])) #rt
                binary_file.write('0000000000011000') #shamt + funct
            else:
                binary_file.write(Registers.get(code_without_comments[i][1])) #rs
                binary_file.write(Registers.get(code_without_comments[i][2])) #rt
                binary_file.write('0000000000011001') #shamt + funct
        
        if code_without_comments[i][0] == 'BREAK':
            binary_file.write('000000') #Opcode
            binary_file.write(format(i, '026b')) # 'i' is the current line
            binary_file.write('001101') #funct
        
        if code_without_comments[i][0] == 'J' or code_without_comments[i][0] == 'JAL':
            if code_without_comments[i][0] == 'J':
                binary_file.write('000010') #Opcode
                for x in range(0, len(labels)):
                    if code_without_comments[i][1] == labels[x]:
                        data = labels[x + 1]
                        binary_file.write(format(data, '026b')) #target
            else:
                binary_file.write('000011') #Opcode
                for x in range(0, len(labels)):
                    if code_without_comments[i][1] == labels[x]:
                        data = labels[x + 1]
                        binary_file.write(format(data, '026b')) #target

        if code_without_comments[i][0] == 'JALR' or code_without_comments[i][0] == 'JR':
            binary_file.write('000000') #Opcode
            if code_without_comments[i][0] == 'JALR':
                binary_file.write(Registers.get(code_without_comments[i][1])) #rs
                binary_file.write('000000000000000') #addres
                binary_file.write('001001') #funct
            else:
                binary_file.write(Registers.get(code_without_comments[i][1])) #rs
                binary_file.write('000000000000000') #addres
                binary_file.write('001000') #funct

        if code_without_comments[i][0] == 'MFC0' or  code_without_comments[i][0] == 'MTC0':
            if code_without_comments[i][0] == 'MFC0':
                binary_file.write('01000000000') #opcode
                binary_file.write(Registers.get(code_without_comments[i][1])) #rt
                binary_file.write(Registers.get(code_without_comments[i][2])) #rd
                binary_file.write('00000000000') #funct
            else:
                binary_file.write('01000000100') #opcode
                binary_file.write(Registers.get(code_without_comments[i][1])) #rt
                binary_file.write(Registers.get(code_without_comments[i][2])) #rd
                binary_file.write('00000000000') #funct
        
        if code_without_comments[i][0] == 'SYSCALL':
            binary_file.write('00000000000000000000000000001100') # code
    except (AttributeError, TypeError) as e:
        print("Error occurred:", e)    
#######################################################

#Open the file
file = open("teste1.asm", "r")
lines = file.readlines()
code = []
labels = []
cont_lines = 0
#Split the lines, save code and labels
for x in lines:
    cont_lines += 1
    if ':' in x:
        x = x.split()
        labels.append(x)
        labels.append(cont_lines)
    else:
        code.append(x.split())
#removing ':' from the labels 
for y in range(0, len(labels),2):
    labels[y] = labels[y][0].replace(':','')
    labels[y] = labels[y].upper()
#Removing the comments of the code and commas
for i in range(0, len(code)):
    for j in range(0, len(code[i])):
        if (j < len(code[i])):
            if (code[i][j] == '#'):
                for x in range(j, len(code[i])):
                    if (x < len(code[i])):
                        code[i][x] = ' '
code_without_comments = []
for i in range(0, len(code)):
    aux_for_append = []
    for j in range(0, len(code[i])):
        if (code[i][j] != ' '):
            aux_for_append.append(code[i][j].upper())
    code_without_comments.append(aux_for_append)

for i in range(0, len(code_without_comments)):
    for j in range(0, len(code_without_comments[i])):
        if ',' in code_without_comments[i][j]:
            for y in range(0, len(code_without_comments[i][j])):
                if code_without_comments[i][j][y] == ',':
                    code_without_comments[i][j] = code_without_comments[i][j].replace(',', '')
# remove empty list inside of code_without_comments
x = 0
for i in code_without_comments:
    if (i == []):
        del code_without_comments[x]
    x += 1
#######################################################
#Starting to mount the binary file here
binary_file = open("binary_file.txt", "w+")

for i in range(0, len(code_without_comments)):
    if code_without_comments[i][0] in Memory_Acess:
        Add_Memory_Acess(code_without_comments, binary_file, i)

    elif code_without_comments[i][0] in Arithmetic_and_Shifter:
        Add_Arithmetic_and_Shifter(code_without_comments, binary_file, i)

    elif code_without_comments[i][0] in Arithmetic_and_Shifter_with_Immediate:
        Add_Arithmetic_and_Shifter_with_Immediate(code_without_comments,binary_file, i)

    elif code_without_comments[i][0] in Branches:
        Add_Branches(code_without_comments, binary_file, labels, i)

    elif code_without_comments[i][0] in Jumps_Div_Mult_And_System:
        Add_Jumps_Div_Mult_And_System(code_without_comments, binary_file, labels, i)
    else:
        print('Error, command not recognized')
        break
    binary_file.write('\n')
file.close()
binary_file.close()