import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd

# parses xml doc into memory as a tree
tree = ET.parse('adminSalary.xml')
root = tree.getroot()

# stupid. to be made better later
names = []
titles = []
salaries = []

for officer in root.iter('{http://www.irs.gov/efile}RltdOrgOfficerTrstKeyEmplGrp'):
    for name in officer.findall('{http://www.irs.gov/efile}PersonNm'):
        names.append(name.text)
    for title in officer.findall('{http://www.irs.gov/efile}TitleTxt'):
        titles.append(title.text)
    for salary in officer.findall('{http://www.irs.gov/efile}TotalCompensationFilingOrgAmt'):
        salaries.append(salary.text)

officers = np.array([names, titles, salaries])

table = pd.DataFrame(officers)

table.to_csv("admin_out.csv")
