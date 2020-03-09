import clr
from tools import workset
from Autodesk.Revit.DB import FilteredElementCollector, Grid

def Grids(document):

	def processGrid( object):
		Name = object.Name
		Workset = workset(object)
		IsPinned = object.Pinned
		Monitor = object.IsMonitoringLinkElement()
		return {"Name":Name,
		"Workset":Workset,
		"IsPinned":IsPinned,
		"IsMonitor":Monitor}

	grids = FilteredElementCollector(document).OfClass(Grid)
	return [processGrid(g) for g in grids]