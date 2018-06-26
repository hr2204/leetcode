

fileName = "   279. Perfect Squares        "
fileName = fileName.strip()
fileName = fileName.replace(" ","_")
fileName = fileName.replace(".","")
fileName = "../solutions_by_company/google/" + fileName + ".py"
open(fileName, 'w')
print fileName