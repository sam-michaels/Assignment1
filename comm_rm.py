# This function reads an imput file and removes all the comments
'''It will remove comments like this:'''
"""This is an example"""
# Like this
'''
And Like this
'''
def removeComments(intputFile) :

    noComments = []     # list used to have all the lines of the files with no comments 
    with open (intputFile, "r") as file:
        inQ = False
        qType = None
        for line in file:
            if not inQ: # checks if line is currently being considered a comment
                if line.strip().startswith("'''") or line.strip().startswith('"""'):    # checks if the the line starts with quotes making it a comment
                    inQ = True
                    qType = line.strip()[:3]
                    if line.count(qType) == 2 :     # checks if there are multiple instaces of the quote type ending the comment
                        inQ = False
                    continue
                commentIndex = line.find("#")       # Used to see if an in line comment is present
                if commentIndex != -1 :             # if the find method can't find the instance, it returns -1
                    if commentIndex == 0 or (line[commentIndex - 1] in " \t"):
                        line = line[:commentIndex]  # removes the comment up until the # symbol

            else:               
                if line.strip().endswith(qType) :   # if already in quotes, checks if the end of the line has quotes ending the comment
                    # if the line only consists of the quotes, checking the end also checks the start
                    inQ = False
                continue

            if line.strip() :                       # Checks if the line is not empty
                noComments.append(line.rstrip())
            else :
                noComments.append("")               # Adds an empty string to the array that will be an empty line

    return "\n".join(noComments)                    # joins all the items into a string sepearating by new line characters

def createOutFile(outfile, noCommentCode) :

    with open (outfile, "w") as file:
        file.write(noCommentCode)                   # Writes all the code with no comments into a new file

    print("Comments have been removed in new output file")
    
    return

def main() :

    noCommentsArr = removeComments("inputFile.py")
    createOutFile("outputFile.py", noCommentsArr)

main()