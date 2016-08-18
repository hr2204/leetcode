

fileName = "     58. Length of Last Word  "
fileName = fileName.strip()
fileName = fileName.replace(" ","_")
fileName = fileName.replace(".","")
fileName = "../solutions/" + fileName + ".py"
open(fileName, 'w')
print fileName