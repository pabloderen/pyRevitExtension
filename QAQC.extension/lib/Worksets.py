import clr
from Autodesk.Revit.DB import FilteredWorksetCollector, WorksetKind

def Worksets( document):
	"""Get document warnings"""
	worksets = FilteredWorksetCollector(document).OfKind(WorksetKind.UserWorkset).ToWorksets()
	return [{"Name" : w.Name, "Id" : w.Id.ToString()} for w in worksets]