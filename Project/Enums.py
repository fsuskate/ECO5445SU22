from enum import IntEnum

class Columns(IntEnum): 
    RACE = 0
    MARITAL_STATUS = 1
    SELF_EMPLOYED = 2
    DEPT_TO_INC = 3
    YEARS_OF_ED = 4
    TYPE_OF_ACTION = 5

class Races(IntEnum):
    AMER_IND = 1,
    ASIAN = 2,
    BLACK = 3,
    HISP = 4,
    WHITE = 5

class ActionTypes(IntEnum):
    LOAN_ORIGINATED = 1
    APP_APPROVED_NOT_ACCEPTED = 2
    APP_DENIED = 3
    APP_WITHDRAWN = 4
    FILE_CLOSED = 5
    LOAN_PURCHASED = 6

