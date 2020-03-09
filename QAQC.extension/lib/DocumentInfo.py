import clr
import os
from Autodesk.Revit.DB import UnitType



def DocumentInfo(object):

	def GetDocumentAccuracy( doc):
		''''Returns Document unit accuracy, PBP location and SiteBenchmark'''
		_unitFormat = doc.GetUnits().GetFormatOptions(UnitType.UT_Length)
		_accuracy = _unitFormat.Accuracy
		d = format(float(_accuracy), '.20g')

		return d

	info = {}
	info["Accuracy"] = GetDocumentAccuracy(object)
	
	info["FileName"] = object.Title
	info["FilePath"] =object.PathName
	info["UnitSystem"] = object.DisplayUnitSystem.ToString()
	info["RevitVersion"] = object.Application.VersionName
	try:
		filePath =os.path.basename( object.PathName)
		info["FileSize"] = os.path.getsize( filePath)/1000000
	except:
		info["FileSize"] = "Revit document not saved or Cloud"



	return info
