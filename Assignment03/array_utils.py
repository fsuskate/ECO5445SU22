# -*- coding: utf-8 -*-

def makeArray(rows: int, cols: int) -> list:
    curr = 0
    result = []
    for rowIndex in range(rows):
        result.append([])
        for colIndex in range(cols):
            curr += 1
            result[rowIndex].append(curr)
    return result