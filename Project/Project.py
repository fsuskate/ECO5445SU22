# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os
from enum import IntEnum

"""
##################################################
#
# ECO 5445: Project Stage 01
#
# Francis Surroca
#
# Due July 17, 2022
# 
##################################################
"""
folder = os.getcwd()
os.chdir(folder + "\\Project")
print(os.getcwd())
print(os.listdir())
df = pd.read_csv("hmda_sw.csv", delimiter=',')

class Columns(IntEnum): 
    RACE = 0
    MARITAL_STATUS = 1
    SELF_EMPLOYED = 2
    DEPT_TO_INC = 3
    YEARS_OF_ED = 4
    TYPE_OF_ACTION = 5

column_names = [
    'Race', 
    'Marital Status', 
    'Self Employed', 
    'Dept to Income', 
    'Years of Education',
    'Type of Action Taken'
]

column_mapping = {
    's13':column_names[Columns.RACE], 
    's23a':column_names[Columns.MARITAL_STATUS], 
    's27a':column_names[Columns.SELF_EMPLOYED], 
    's45':column_names[Columns.DEPT_TO_INC],
    'school':column_names[Columns.YEARS_OF_ED],
    's7':column_names[Columns.TYPE_OF_ACTION],
}

df.rename(columns=column_mapping, inplace=True)

print(df)

df_model_data = df.filter(column_names)

print(df_model_data)

sum_stats = df_model_data.describe(include='all')

# columns have representative values so, need to interpret them first
print(sum_stats)

column_names_output = [
    'Applicant Race', 
    'Approved', 
    'Not Approved', 
    'Total'
]

class Races(IntEnum):
    AMER_IND = 1,
    ASIAN = 2,
    BLACK = 3,
    HISP = 4,
    WHITE = 5

races = {
    Races.AMER_IND:'American Indian or Alaskan Native',
    Races.ASIAN:'Asian or Pacific Islander',
    Races.BLACK:'Black',
    Races.HISP:'Hispanic',
    Races.WHITE:'White',
}

totals = {
    Races.AMER_IND:0,
    Races.ASIAN:0,
    Races.BLACK:0,
    Races.HISP:0,
    Races.WHITE:0,
}

total_approved = {
    Races.AMER_IND:0,
    Races.ASIAN:0,
    Races.BLACK:0,
    Races.HISP:0,
    Races.WHITE:0,
}

total_not_approved = {
    Races.AMER_IND:0,
    Races.ASIAN:0,
    Races.BLACK:0,
    Races.HISP:0,
    Races.WHITE:0,
}

class ActionTypes(IntEnum):
    LOAN_ORIGINATED = 1
    APP_APPROVED_NOT_ACCEPTED = 2
    APP_DENIED = 3
    APP_WITHDRAWN = 4
    FILE_CLOSED = 5
    LOAN_PURCHASED = 6

def is_approved(action_type: int) -> bool:
    if (action_type == ActionTypes.LOAN_ORIGINATED or action_type == ActionTypes.APP_APPROVED_NOT_ACCEPTED):
        return True
    elif (action_type == ActionTypes.APP_DENIED):
        return False
    print(f"Not sure if approved or not: {action_type}")

for idx, row in df_model_data.iterrows():
    race = row[column_names[Columns.RACE]]
    totals[race] += 1

    if (race == Races.BLACK):
        approved = is_approved(row[Columns.TYPE_OF_ACTION])   
        if (approved):
            total_approved[Races.BLACK] += 1
        else:
            total_not_approved[Races.BLACK] += 1
    elif (race == Races.WHITE):
        approved = is_approved(row[Columns.TYPE_OF_ACTION])   
        if (approved):
            total_approved[Races.WHITE] += 1
        else:
            total_not_approved[Races.WHITE] += 1

print(totals)

output_df = pd.DataFrame(columns=column_names_output)
output_df.append({})
