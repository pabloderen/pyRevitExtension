import clr
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInParameter, View



def Views(document):

	def template( object):
		
		_viewTemplateId = object.ViewTemplateId
		if _viewTemplateId.IntegerValue > -1:
			return True
		else:
			return False


	def processViews (object):
		Name = object.Name
		HasTemplate = template(object)
		IsTemplate = object.IsTemplate
		ViewType = object.ViewType.ToString()
		Sheet = object.get_Parameter(BuiltInParameter.VIEWPORT_SHEET_NUMBER).AsString()

		return {"Name": Name, 
		"HasTemplate":HasTemplate, 
		"IsTemplate":IsTemplate, 
		"ViewType":ViewType,
		"Sheet":Sheet}
		
	views = FilteredElementCollector(document).OfClass(View).WhereElementIsNotElementType() 
	return [processViews(v) for v in views if v.AllowsAnalysisDisplay()]