

fileName = "     120. Triangle      "
fileName = fileName.strip()
fileName = fileName.replace(" ","_")
fileName = fileName.replace(".","")
fileName = "../solutions/" + fileName + ".py"
open(fileName, 'w')
print fileName