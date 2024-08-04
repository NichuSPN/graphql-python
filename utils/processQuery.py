from utils.postgres import get_all_rows, get_one_row


def row_mapper(columns, row, mapper=None):
    row_dict = {}
    for i, col in enumerate(columns):
        v = row[i]
        if mapper and col in mapper.keys():
            row_dict[mapper[col]] = v
        else:
            row_dict[col] = v
    return row_dict


def singleRowQueryAndMap(query, columns, mapper=None):
    success, data = get_one_row(query)
    if not success:
        print("Error in a Query ", data)
        return None
    return row_mapper(columns, data, mapper)


def singleRowQueryAndTransform(query, columns, transformClass, mapper=None):
    data = singleRowQueryAndMap(query, columns, mapper)
    print(data)
    if not data:
        return None
    return transformClass(data)


def multiRowQueryAndTransform(query, columns, transformClass, mapper=None):
    success, data = get_all_rows(query)
    if not success:
        print("Error in a Query ", data)
        return None
    transformedRows = []
    for row in data:
        mappedRow = row_mapper(columns, row, mapper)
        if mappedRow:
            transformedRows.append(transformClass(mappedRow))
    return transformedRows
