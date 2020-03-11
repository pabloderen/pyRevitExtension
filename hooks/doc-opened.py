
import clr
import math
import sys
import os
import json
import time
from System.Collections.Generic import List
from pyrevit import script
from pyrevit import script, EXEC_PARAMS

#QAQC libraries
from ProjectBasePoint import ProjectBasePoint
from CadLinks import CadLinks
from Groups import Groups
from Levels import Levels
from Views import Views
from DocumentInfo import DocumentInfo
from Worksets import Worksets
from Warnings import Warnings
from SharedParameters import SharedParameters
from Grids import Grids
from Families import Families
from RevitLinks import RevitLinks


from Autodesk.Revit.DB import FilteredElementCollector, ElementId, CategoryType, ElementCategoryFilter,\
	BuiltInCategory, DimensionType, BasePoint , UnitType, ElementFilter, LogicalOrFilter, Options ,\
	BuiltInParameter, FilteredWorksetCollector, WorksetKind,GroupType, Group ,SharedParameterElement, \
	RevitLinkInstance, ImportInstance, View, Level, Grid

#if is event trigger we get the document from the event
doc =EXEC_PARAMS.event_args.Document
#if is button trigger
# doc = __revit__.ActiveUIDocument.Document


def Complete(document):
	now = int(time.time())
	

	output = {
		"Timestamp":now,
		"Document": DocumentInfo(document),
		"Families": Families(document),
		"Shared Parameters": SharedParameters(document),
		"Warnings": Warnings(document),
		"ProjectBasePoint": ProjectBasePoint(document),
		"RevitWorksets": Worksets( document),
		"RevitView": Views(document),
		"RevitLevel": Levels(document),
		"RevitGrid": Grids(document),
		"CadLinks":CadLinks(document),
		"RevitLinks":RevitLinks(document),
		"Groups": Groups(document),
	}
	return output

processDocument = Complete(doc)
results = script.get_results()
results.QAQC = json.dumps(processDocument,  ensure_ascii=False)



