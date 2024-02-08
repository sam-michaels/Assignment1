
def removeComments(intputFile) :

    noComments = []
    with open (intputFile, "r") as file:
        inQ = False
        qType = None
        for line in file:
            if not inQ:
                if line.strip().startswith("'''") or line.strip().startswith('"""'):
                    inQ = True
                    qType = line.strip()[:3]
                    if line.count(qType) == 2 :
                        inQ = False
                    continue
                commentIndex = line.find("#")
                if commentIndex != -1 :
                    if commentIndex == 0 or (line[commentIndex - 1] in " \t"):
                        line = line[:commentIndex]

            else:
                if line.strip().endswith(qType) :
                    inQ = False
                    continue
                elif line.strip().startswith(qType) :
                    inQ = False
                    continue
                else :
                    continue
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