import clr
import math
from Autodesk.Revit.DB import FilteredElementCollector, GroupType, Group

def Groups(document):
	
	def GetType(object):
		collector = FilteredElementCollector(object).OfClass(GroupType)

		return collector

	def GetInstance(object):
		collector = FilteredElementCollector(object).OfClass(Group)

		return collector

	types = [g for g in GetType(document)]
	instances = [g for g in GetInstance(document)]
	instancesTypes = [i.GetTypeId() for i in instances]
	notUsedTypes = [g for g in types if g.Id not in instancesTypes]
	return {"Group Instances": len(instances), "Group types":len(types), "Not used types": len(notUsedTypes)}