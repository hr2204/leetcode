

fileName = "      54 Spiral Matrix          "
fileName = fileName.strip()
fileName = fileName.replace(" ","_")
fileName = fileName.replace(".","")
fileName = "../solutions_by_company/google/" + fileName + ".py"
open(fileName, 'w')
print fileName