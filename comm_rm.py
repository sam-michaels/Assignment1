
def removeComments(intputFile) :

    noComments = []
    with open (intputFile, "r") as file:
        for line in file:
            commentIndex = line.find("#")
            if commentIndex != -1 :
                if commentIndex == 0 or (line[commentIndex - 1] in " \t"):
                    line = line[:commentIndex]
            if line.strip() :
                noComments.append(line.rstrip())
            else :
                noComments.append("")

    return "\n".join(noComments)

def createOutFile(outfile, noCommentCode) :
    with open (outfile, "w") as file:
        file.write(noCommentCode)
    print("Comments have been removed in new output file")
    return

def main() :

    noCommentsArr = removeComments("/Users/sammichaels/CSClasses/3342/Assignment1/inputFile.py")
    createOutFile("/Users/sammichaels/CSClasses/3342/Assignment1/outputFile.py", noCommentsArr)

main()