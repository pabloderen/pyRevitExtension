
import clr
from Autodesk.Revit.DB import  BuiltInParameter


def Dimensions( document):
	"""Return dimension styles"""
	Name = document.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
	Accuracy = "Default"
	Units = "Default"

	try:
		format = document.GetUnitsFormatOptions()
		Accuracy = format.Accuracy
		Units = format.DisplayUnits.ToString()
	except:
		pass

	DimensionType = document.StyleType.ToString()

	return {"Name": Name,
	"Accuracy":Accuracy,
	"Units": Units,
	"DimensionType": DimensionType}