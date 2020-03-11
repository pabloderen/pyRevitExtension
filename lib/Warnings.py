import clr
from tools import CountFrequency


def Warnings(doc):
	"""Get warnings from document"""
	warnings = doc.GetWarnings()
	warningMessages =[w.GetDescriptionText() for w in warnings]
	countOfWarnings = CountFrequency(warningMessages)
	allwarnings = [{"Description": key, "Count": value} for key, value in countOfWarnings.items()]
	if len(allwarnings) < 1:
		allwarnings.append({"Description": "", "Count": 0} )
	return allwarnings