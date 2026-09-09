import xml.etree.ElementTree as ET

# parses xml doc into memory as a tree
tree = ET.parse('adminSalary.xml')
root = tree.getroot()

officerList = []

for officer in root.iter('{http://www.irs.gov/efile}RltdOrgOfficerTrstKeyEmplGrp'):
    officerList.append(officer)
print(officerList)

