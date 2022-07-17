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
import numpy as np
import os
from Enums import *
from Constants import *
from Globals import *
import matplotlib.pyplot as plt

"""
##################################################
#
# Step 3: bring in the dataset
# 
##################################################
"""
folder = os.getcwd()
git_path = 'C:\\Users\\fsurroca\\Documents\\GitHub\\ECO5445SU22'
os.chdir(git_path + "\\Project\\Data")
df = pd.read_csv("hmda_sw.csv", delimiter=',')

df.rename(columns=COLUMN_MAPPING, inplace=True)
# print(df)

df_model_data = df.filter(COLUMN_NAMES)
# print(df_model_data)

"""
##################################################
#
# Step 4: generate summary statistics, histograms
# 
##################################################
"""
# clean the data before interpretation

# set all MISSING_OBSERVATION values to 0 to make data easier to work with
df_model_data.loc[df_model_data[COLUMN_NAMES[Columns.YEARS_OF_ED]] == MISSING_OBSERVATION, COLUMN_NAMES[Columns.YEARS_OF_ED]] = 0

# set type of action to either just approved/not approved
df_model_data.loc[df_model_data[COLUMN_NAMES[Columns.TYPE_OF_ACTION]] > ActionTypes.APP_APPROVED_NOT_ACCEPTED, COLUMN_NAMES[Columns.TYPE_OF_ACTION]] = 0
df_model_data.loc[df_model_data[COLUMN_NAMES[Columns.TYPE_OF_ACTION]] <= ActionTypes.APP_APPROVED_NOT_ACCEPTED, COLUMN_NAMES[Columns.TYPE_OF_ACTION]] = 1

# convert marital status to float data type
df_model_data.loc[df_model_data[COLUMN_NAMES[Columns.MARITAL_STATUS]] == 'M', COLUMN_NAMES[Columns.MARITAL_STATUS]] = 1
df_model_data.loc[df_model_data[COLUMN_NAMES[Columns.MARITAL_STATUS]] == 'U', COLUMN_NAMES[Columns.MARITAL_STATUS]] = 0
df_model_data.loc[df_model_data[COLUMN_NAMES[Columns.MARITAL_STATUS]] == 'S', COLUMN_NAMES[Columns.MARITAL_STATUS]] = 2
df_model_data.loc[df_model_data[COLUMN_NAMES[Columns.MARITAL_STATUS]] == 'NA', COLUMN_NAMES[Columns.MARITAL_STATUS]] = -1
df_model_data = df_model_data.astype({COLUMN_NAMES[Columns.MARITAL_STATUS]:float})

# get rid of huge outliers in dept to income

df_model_data.loc[df_model_data[COLUMN_NAMES[Columns.DEPT_TO_INC]] > 100.0, COLUMN_NAMES[Columns.DEPT_TO_INC]] = df_model_data[COLUMN_NAMES[Columns.DEPT_TO_INC]].mean()

# get and display summary statistics
sum_stats = df_model_data.describe()
print(f'{sum_stats}\n')

# generate default histograms
df_model_data.hist()

# investigate data grouped by race
grouped_by_race = df_model_data.groupby(COLUMN_NAMES[Columns.RACE])
print(grouped_by_race.describe())
grouped_by_race.hist()

# investigate correlations between race and all other variables
for col in COLUMN_NAMES:
    print(f"Correlation between Race and {col}\n {np.corrcoef(df_model_data[COLUMN_NAMES[Columns.RACE]], df_model_data[col])}")

# visualize some relationships plotted together on same graph
black = df_model_data[COLUMN_NAMES[Columns.RACE]] == Races.BLACK
white = df_model_data[COLUMN_NAMES[Columns.RACE]] == Races.WHITE
for idx, col in enumerate(COLUMN_NAMES):
    plt.figure(idx+10)
    plt.style.use('ggplot')
    plt.title(col)
    plt.hist(df_model_data[col][white], edgecolor='black',color='blue',label=RACES_MAPPING[Races.WHITE])
    plt.hist(df_model_data[col][black], edgecolor='black',color='brown',label=RACES_MAPPING[Races.BLACK])
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

"""
##################################################
#
# Step 5: baseline probability of an individual
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

for idx, row in df_model_data.iterrows():
    race = row[COLUMN_NAMES[Columns.RACE]]    
    update_totals(race, row)

prob_of_approved_overall = sum(total_approved.values())/sum(totals.values())
print(f'P(Approved|Overall) = {prob_of_approved_overall}\n')

"""
##################################################
#
# Step 6: create table  
# 
##################################################
"""

def create_output_dataframe() -> pd.DataFrame:
    list = []
    for race in Races:
        list.append([RACES_MAPPING[race],total_approved[race],total_not_approved[race],totals[race]])
    list.append(['Total',sum(total_approved.values()),sum(total_not_approved.values()),sum(totals.values())])

    df = pd.DataFrame.from_records(list)
    df.columns = COLUMN_NAMES_OUTPUT
    return df

output_df = create_output_dataframe()
print(f'{output_df.to_string(index=False)}\n')

"""
##################################################
#
# Step 7: calculate probabilities
# 
##################################################
"""

prob_of_approved_white = output_df.loc[Races.WHITE-1, 'Approved']/output_df.loc[Races.WHITE-1, 'Total']
print(f'P(Approved|White) = {prob_of_approved_white}')

prob_of_approved_black = output_df.loc[Races.BLACK-1, 'Approved']/output_df.loc[Races.BLACK-1, 'Total']
print(f'P(Approved|Black) = {prob_of_approved_black}')


