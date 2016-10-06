

fileName = "  268. Missing Number    "
fileName = fileName.strip()
fileName = fileName.replace(" ","_")
fileName = fileName.replace(".","")
fileName = "../solutions/" + fileName + ".py"
open(fileName, 'w')
print fileName