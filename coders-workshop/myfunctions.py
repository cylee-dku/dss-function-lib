import dataiku

def create_target(row, v):
    revenue = row['revenue']
    if revenue >= v:
        target = 1
    elif revenue < v:
        target = 0
    else:
        target = revenue
    return target
