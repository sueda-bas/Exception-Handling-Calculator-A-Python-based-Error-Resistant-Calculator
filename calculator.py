import sys
#Calculates addition, subtraction, multiplication,and division of two given numbers gives results to user.
def calculator (operand1,operand2,operator,element,output_file):
    if operator=="+":
        result=float(operand1)+float(operand2)
        string_element=" ".join(element)+"\n"
        output_file.write(string_element)
        rounded_result="{:.2f}".format(result)
        result_string="="+str(rounded_result)+"\n"
        output_file.write(result_string)
    if operator=="-":
        result=float(operand1)-float(operand2)
        string_element=" ".join(element)+"\n"
        output_file.write(string_element)
        rounded_result="{:.2f}".format(result)
        result_string="="+str(rounded_result)+"\n"
        output_file.write(result_string)
    if operator=="*":
        result=float(operand1)*float(operand2)
        string_element=" ".join(element)+"\n"
        output_file.write(string_element)
        rounded_result="{:.2f}".format(result)
        result_string="="+str(rounded_result)+"\n"
        output_file.write(result_string)
    if operator=="/":
        result=float(operand1)/float(operand2)
        string_element=" ".join(element)+"\n"
        output_file.write(string_element)
        rounded_result="{:.2f}".format(result)
        result_string="="+str(rounded_result)+"\n"
        output_file.write(result_string)
#Controls edge cases and gives output to user.   
def solutions(question_lists,output_file):
    operators=["+","-","*","/"]
    for element in question_lists:
        operand1_validity=False #Checks if the operand1 is valid.
        operands_validity=False #Checks if both operand1 and operand2 are valid.
        if element==[]: #Ignores empty lines.
            continue
        if len(element)==3: #Line format is not erroneous.
            operand1=element[0]
            operator=element[1]
            operand2=element[2]
            try:
                operand1=float(operand1) #If operand1 is not a number it gives an Error.
                operand1valid=True #Verified that operand1 is a number.
                operand2=float(operand2) #If operand2 is not a number it gives an Error.
                operands_validity=True #Verified that operand1 and operand2 are numbers.
            except ValueError:
                if operand1_validity==False:
                    string_element=" ".join(element)
                    output_file.write(string_element+"\n")
                    output_file.write("ERROR: First operand is not a number!"+"\n")
                if operand1_validity==True:
                    string_element=" ".join(element)
                    output_file.write(string_element+"\n")
                    output_file.write("ERROR: Second operand is not a number!"+"\n")
            try:  
                if operands_validity==True: 
                    assert operator in operators #Checks the validity of operator's. 
                    if operands_validity==True:
                        calculator(operand1,operand2,operator,element,output_file)    
            except AssertionError:
                string_element=" ".join(element)
                output_file.write(string_element+"\n")
                output_file.write("ERROR: There is no such an operator!"+"\n")
        if len(element)!=3:
            operand1valid=False #Checks if the operand1 is valid.
            try:
                assert len(element)==3 #Checks the line format. It must include three items.
                operand1=float(operand1)
                operand2=float(operand2) 
            except AssertionError:
                string_element=" ".join(element)
                output_file.write(string_element+"\n")
                output_file.write("ERROR: Line format is erroneous!"+"\n")
            except ValueError:
                if operand1_validity==False:
                    string_element=" ".join(element)
                    output_file.write(string_element+"\n")
                    output_file.write("ERROR: First operand is not a number!"+"\n")
                if operand1_validity==True:
                    string_element=" ".join(element)
                    output_file.write(string_element+"\n")
                    output_file.write("ERROR: Second operand is not a number!"+"\n")
def main():
    try:
        expected_argv_commands=2
        input_file=open(sys.argv[1],"r")
        output_file=open(sys.argv[2],"a")
        input_file_name=sys.argv[1]
        if len(sys.argv) != expected_argv_commands+ 1:
            raise IndexError
        questions=input_file.read()
        question_lines=questions.splitlines()
        question_lists=[]
        for line in question_lines:
            question_lists.append(line.split())
        solutions(question_lists,output_file)

    except IndexError:
        print("ERROR: This program needs two command line arguments to run, where first one is the input file and the second one is the output file!")
        print("Sample run command is as follows: python3 calculator.py input.txt output.txt") 
        print("Program is going to terminate!")
    except FileNotFoundError:
        print("ERROR: There is either no such a file namely",input_file_name,"or this program does not have permission to read it!")
        print("Program is going to terminate!")
    finally:
        input_file.close()
        output_file.close()


if __name__=="__main__":
    main()
