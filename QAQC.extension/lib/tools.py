
import clr
import math
from System.Collections.Generic import List
from Autodesk.Revit.DB import FilteredElementCollector,  BasePoint, BuiltInParameter,\
    Options, RevitLinkInstance, WorksetKind, FilteredWorksetCollector, ElementCategoryFilter,\
        CategoryType, LogicalOrFilter, ElementFilter

def categoryFilter(doc):
	
	categories = doc.Settings.Categories

	cats = [ElementCategoryFilter(c.Id) for c in categories if c.CategoryType == CategoryType.Model and c.CanAddSubcategory ]
	filter = None

	if len(cats):
		try:
			filter = LogicalOrFilter(List[ElementFilter](cats))
		except Exception as ex:
			raise Exception(str(ex) + str(len(cats) ))
	
	return filter


def ConvertToList(l):
	if isinstance(l, list):
		return l
	else:
		return [l]


def CountFrequency( my_list): 
	freq = {} 
	for items in my_list: 
		freq[items] = my_list.count(items) 

	return freq

def workset(object):
	worksets = FilteredWorksetCollector(object.Document).OfKind(WorksetKind.UserWorkset).ToWorksets() 
	w = [w.Name for w in worksets if w.Id == object.WorksetId]
	if len(w) == 0:
		return "View dependent Symbol"
	else:
		return w[0]
