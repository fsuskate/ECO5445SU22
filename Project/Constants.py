from Enums import Columns
from Enums import Races

COLUMN_NAMES = [
    'Race', 
    'Marital Status', 
    'Self Employed', 
    'Dept to Income', 
    'Years of Education',
    'Type of Action Taken'
]

COLUMN_MAPPING = {
    's13':COLUMN_NAMES[Columns.RACE], 
    's23a':COLUMN_NAMES[Columns.MARITAL_STATUS], 
    's27a':COLUMN_NAMES[Columns.SELF_EMPLOYED], 
    's45':COLUMN_NAMES[Columns.DEPT_TO_INC],
    'school':COLUMN_NAMES[Columns.YEARS_OF_ED],
    's7':COLUMN_NAMES[Columns.TYPE_OF_ACTION],
}

COLUMN_NAMES_OUTPUT = [
    'Applicant Race', 
    'Approved', 
    'Not Approved', 
    'Total'
]

RACES_MAPPING = {
    Races.AMER_IND:'American Indian or Alaskan Native',
    Races.ASIAN:'Asian or Pacific Islander',
    Races.BLACK:'Black',
    Races.HISP:'Hispanic',
    Races.WHITE:'White',
}
