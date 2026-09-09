import xml.etree.ElementTree as ET
import numpy as np

# parses xml doc into memory as a tree
tree = ET.parse('adminSalary.xml')
root = tree.getroot()


officerList = np.array([],[])

for officer in root.iter('{http://www.irs.gov/efile}RltdOrgOfficerTrstKeyEmplGrp'):
    for field in officer.findall('*'):
        officerList = officerList.append(field.find('{http://www.irs.gov/efile}PersonNm'))

        

