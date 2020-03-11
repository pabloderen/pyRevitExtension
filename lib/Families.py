import clr
from tools import categoryFilter
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInParameter


def Families( document):
	"""Get available families information
	
	Input: Document

	Return: {Family, Category, Type, isInPlace, Amount}
	"""
	filters = categoryFilter(document)
	collector =  FilteredElementCollector(document).WherePasses(filters).WhereElementIsNotElementType().ToElements()
	listOfFamilies = []
	for fs in collector:
		
		if hasattr(fs, "Name"):
			category = fs.get_Parameter(BuiltInParameter.ELEM_CATEGORY_PARAM_MT).AsValueString() 
			isInPlace = False
			familyName = ""

			if hasattr(fs, "Symbol"):
				f = fs.Symbol.Family
				familyName = f.Name
				if hasattr(f, "IsInPlace"):
					isInPlace = f.IsInPlace
			
			t =  fs.Name
			ff = [x for x in listOfFamilies if x["Family"] == familyName and x["Type"] == t]

			if ff:
				amount = ff[0]["Amount"] + 1
				ff[0]["Amount"] = amount
			else:
				newFam = {}
				newFam["Category"] = category
				newFam["Family"] = familyName
				newFam["Type"] = t
				newFam["isInPlace"] = isInPlace
				newFam["Amount"] = 1
				
				listOfFamilies.append(newFam)

	return listOfFamilies
