

fileName = "      17 Letter Combinations of a Phone Number         "
fileName = fileName.strip()
fileName = fileName.replace(" ","_")
fileName = fileName.replace(".","")
fileName = "../solutions_by_company/google/" + fileName + ".py"
open(fileName, 'w')
print fileName