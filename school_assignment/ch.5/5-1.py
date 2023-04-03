units = ['cm', 'm', 'inch', 'ft']

def converUnit(len, unit):
    if unit == units[0]:
        result = float(len) * 0.1
        print(result, unit)
    elif unit == units[1]:
        result = float(len) * 0.01
        print(result, unit)
    elif unit == units[2]:
        result = float(len) * 0.03937
        print(result, unit)
    elif unit == units[3]:
        result = float(len) * 0.00328
        print(result, unit)
    

converUnit(1, "inch")
