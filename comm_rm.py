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
        sType = None
        inBackslash = False
        quoteCount = 0
        for line in file:
            if not inQ: # checks if line is currently being considered a comment
                if line.strip().endswith("\\") :
                    inBackslash = True
                elif (line.strip().endswith("'''") or line.strip().endswith('"""'))  and inBackslash:
                    quoteCount += 1
                    if quoteCount == 2 :
                        inBackslash = False
                        quoteCount = 0
                elif line.strip().startswith("'''") or line.strip().startswith('"""') and not inBackslash:    # checks if the the line starts with quotes making it a comment
                    inQ = True
                    qType = line.strip()[:3]
                    if line.count(qType) == 2 :     # checks if there are multiple instaces of the quote type ending the comment
                        inQ = False
                    continue

                startQ = -1
                endQ = -1
                sinQIndex = line.strip().find("'")
                doubQIndex = line.strip().find('"')
                commentIndex = line.find("#")       # Used to see if an in line comment is present

                if 1 <= sinQIndex < doubQIndex or doubQIndex == -1 :
                    sType = "'"
                    startQ = sinQIndex
                elif 1 <= doubQIndex < sinQIndex or sinQIndex == -1 :
                    sType = '"'
                    startQ = doubQIndex

                if startQ != -1 :
                    endQ = line.strip().find(sType, startQ + 1)

                if commentIndex != -1 :             # if the find method can't find the instance, it returns -1
                    if startQ != 1 and endQ != 1 :
                        if endQ < commentIndex or commentIndex < startQ :
                            line = line[:commentIndex]  # removes the comment up until the # symbol
                    elif commentIndex == 0 or (line[commentIndex - 1] in " \t"):
                        line = line[:commentIndex]  # removes the comment up until the # symbol

            else:
                if line.strip().startswith("\\", 0) :
                    if " " in line.strip() :
                        inQ = False
                    else :
                        continue
                else :
                    if line.strip().endswith(qType) :
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