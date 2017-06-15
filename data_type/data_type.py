def data_type(data):
    if type(data) == str:
        return len(data)
    if data is None:
        return 'no value'
    elif type(data) == bool:
        return data
    if type(data) == int:
        if data < 100:
            return "less than 100"
        if data > 100:
            return "more than 100"
        if data == 100:
            return 'equal to 100'
    if type(data) == list:
        if len(data) < 3:
            return None
        else:
            return data[2]