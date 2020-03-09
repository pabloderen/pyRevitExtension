import clr
from tools import workset
from Autodesk.Revit.DB import FilteredElementCollector, Level



def Levels(document):

	def processLevels(object):
		Name = object.Name
		Workset = workset(object)
		IsPinned = object.Pinned
		Monitor = object.IsMonitoringLinkElement()
		Elevation = object.Elevation
		return {"Name":Name,
		"Workset":Workset,
		"IsPinned":IsPinned,
		"IsMonitor":Monitor,
		"Elevation":Elevation
		}
	levels = FilteredElementCollector(document).OfClass(Level)
	return [processLevels(g) for g in levels]