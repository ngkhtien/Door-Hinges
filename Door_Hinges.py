from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction
doc = __revit__.ActiveUIDocument.Document
doors=FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors)\
                    .WhereElementIsNotElementType()\
                    .ToElements()

Hinges_side="Hinges_side"

t=Transaction(doc,'set door hinges side')
t.Start()

for door in doors:
    print(15*'-')
    print(door.Id)
    print(door.Mirrored)
    hinges_default_param= door.LookupParameter(Hinges_side)  
    if door.Mirrored:
        hinges_default_param.Set("L")
    else:
        hinges_default_param.Set("R")

t.Commit()