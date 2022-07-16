# -*- coding: utf-8 -*-

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

import pandas as pd
import os
from Enums import *
from Constants import *
from Globals import *

"""
##################################################
#
# Questions 3: bring in the dataset
# 
##################################################
"""
folder = os.getcwd()
os.chdir(folder + "\\Project\\Data")
print(os.getcwd())
print(os.listdir())
df = pd.read_csv("hmda_sw.csv", delimiter=',')

df.rename(columns=COLUMN_MAPPING, inplace=True)
# print(df)

df_model_data = df.filter(COLUMN_NAMES)
# print(df_model_data)

"""
##################################################
#
# Questions 4: generate summary statistics
# 
##################################################
"""
sum_stats = df_model_data.describe(include='all')
print(f'{sum_stats}\n')

"""
##################################################
#
# Questions 5: baseline probability of an individual
# being approved for a mortgage.
# 
##################################################
"""

def is_approved(action_type: int) -> bool:
    if (action_type == ActionTypes.LOAN_ORIGINATED or action_type == ActionTypes.APP_APPROVED_NOT_ACCEPTED):
        return True
    elif (action_type == ActionTypes.APP_DENIED):
        return False
    print(f"Not sure if approved or not: {action_type}")

def update_totals(race: Races, row):
    totals[race] += 1

    approved = is_approved(row[Columns.TYPE_OF_ACTION])   
    if (approved):
        total_approved[race] += 1
    else:
        total_not_approved[race] += 1

def create_output_dataframe() -> pd.DataFrame:
    list = []
    for race in Races:
        list.append([RACES_MAPPING[race],total_approved[race],total_not_approved[race],totals[race]])
    list.append(['Total',sum(total_approved.values()),sum(total_not_approved.values()),sum(totals.values())])

    df = pd.DataFrame.from_records(list)
    df.columns = COLUMN_NAMES_OUTPUT
    return df

for idx, row in df_model_data.iterrows():
    race = row[COLUMN_NAMES[Columns.RACE]]    
    update_totals(race, row)

prob_of_approved_overall = sum(total_approved.values())/sum(totals.values())
print(f'P(Approved|Overall) = {prob_of_approved_overall}\n')

"""
##################################################
#
# Questions 6: create table  
# 
##################################################
"""

output_df = create_output_dataframe()
print(f'{output_df.to_string(index=False)}\n')


"""
##################################################
#
# Questions 7: calculate probabilities
# 
##################################################
"""

prob_of_approved_white = output_df.loc[Races.WHITE-1, 'Approved']/output_df.loc[Races.WHITE-1, 'Total']
print(f'P(Approved|White) = {prob_of_approved_white}')

prob_of_approved_black = output_df.loc[Races.BLACK-1, 'Approved']/output_df.loc[Races.BLACK-1, 'Total']
print(f'P(Approved|Black) = {prob_of_approved_black}')


