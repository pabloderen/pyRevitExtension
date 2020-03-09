
import clr
import math
from tools import workset
from Autodesk.Revit.DB import FilteredElementCollector,  BasePoint, BuiltInParameter,\
    Options, RevitLinkInstance, WorksetKind, FilteredWorksetCollector



def RevitLinks(document):

	def ProcessRVTLink(linkRVT):
		
		Name = linkRVT.Name
		link = linkRVT.Document.GetElement(linkRVT.GetTypeId())
		IsPinned = linkRVT.Pinned
		RevitTypeWorkset = workset(link)
		InstanceWorkset = workset(linkRVT)
		return {"Name":Name,
		"IsPinned":IsPinned,
		"InstanceWorkset":InstanceWorkset,
		"RevitTypeWorkset":RevitTypeWorkset
		}


	revitlinks = FilteredElementCollector(document).OfClass(RevitLinkInstance).ToElements() 
	return [ProcessRVTLink(e) for e in revitlinks ]