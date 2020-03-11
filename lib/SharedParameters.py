import clr
from Autodesk.Revit.DB import FilteredElementCollector, SharedParameterElement

def SharedParameters(document):
	"""Retrieves list of shared parameters in document

	Input: Document 

	Return: {"Name", "Guid"}
	"""
	collector = FilteredElementCollector(document).OfClass(SharedParameterElement)
	output = []
	for sp in collector:
		definition = sp.GetDefinition()
		guid = sp.GuidValue.ToString()
		output.append( {"Name": definition.Name, "Guid":guid})
	return output
