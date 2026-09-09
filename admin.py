import xml.etree.ElementTree as ET
import numpy as np

# parses xml doc into memory as a tree
tree = ET.parse('adminSalary.xml')
root = tree.getroot()

# stupid. to be made better later
names = []
titles = []

for officer in root.iter('{http://www.irs.gov/efile}RltdOrgOfficerTrstKeyEmplGrp'):
    for name in officer.findall('{http://www.irs.gov/efile}PersonNm'):
        names.append(name.text)
    for title in officer.findall('{http://www.irs.gov/efile}TitleTxt'):
        titles.append(title.text)
officers = np.array([names, titles])

print(officers)
