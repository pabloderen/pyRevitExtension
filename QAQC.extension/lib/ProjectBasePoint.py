
import clr
import math
from Autodesk.Revit.DB import FilteredElementCollector,  BasePoint, BuiltInParameter, Options


def ProjectBasePoint(document):
	
	def GetProjectBasepoint(object):
		collector = FilteredElementCollector(object).OfClass(BasePoint).WhereElementIsNotElementType()
		for p in collector:
			if not p.IsShared:
				return p
		return None

	def getCoordinates( pbp, document):
		option = Options()
		option.ComputeReferences = True
		#PBP location as per revit center
		return pbp.get_BoundingBox(document.ActiveView).Min

	def getGeoCoord(i):
		
		EW = i.get_Parameter(BuiltInParameter.BASEPOINT_EASTWEST_PARAM).AsDouble()
		NS = i.get_Parameter(BuiltInParameter.BASEPOINT_NORTHSOUTH_PARAM).AsDouble()
		EL = i.get_Parameter(BuiltInParameter.BASEPOINT_ELEVATION_PARAM).AsDouble()
		RO = i.get_Parameter(BuiltInParameter.BASEPOINT_ANGLETON_PARAM).AsDouble()
		#Convert rotation from rad to degrees
		RO = 0 if (360 - math.degrees(RO)) ==360 else 360 - math.degrees(RO)
		
		return {"NorthSouth": format(NS, "10f"), "EastWest":format(EW, "10f"), "Elevation": format(EL, "10f"), "Rotation":format(RO, "10f") }

	element = GetProjectBasepoint(document)
	coord = getCoordinates(element,document)
	IsPinned = element.Pinned
	Coordinates = {"x": format(coord.X, "10f"), "y":format(coord.X, "10f"), "z": format(coord.X, "10f")}
	Site = getGeoCoord(element)
	GUID = document.SiteLocation.UniqueId

	return {"IsPinned":IsPinned, "Coordinates":Coordinates, "Site":Site, "GUID":GUID }

