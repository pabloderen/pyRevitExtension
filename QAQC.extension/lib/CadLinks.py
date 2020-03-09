import clr
import math
from tools import workset
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInParameter, ImportInstance,\
	 FilteredWorksetCollector, WorksetKind


def CadLinks(document):

	def processCad(cad):
		Name = "Error"
		try:
			Name = cad.get_Parameter(BuiltInParameter.IMPORT_SYMBOL_NAME).AsString()
		except:
			pass
		
		link = cad.Document.GetElement(cad.GetTypeId())
		Workset = workset(cad)
		CadTypeWorkset = workset(link)
		IsPinned = cad.Pinned
		Linked = cad.IsLinked

		return { "Name":Name,
		"Workset":Workset, 
		"CadTypeWorkset":CadTypeWorkset, 
		"IsPinned": IsPinned, 
		"Linked":Linked }

	cadlinks = FilteredElementCollector(document).OfClass(ImportInstance)
	return [processCad(c) for c in cadlinks]