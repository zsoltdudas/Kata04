def read_file(filename):
    data = []
    content = [rows.rstrip('\n') for rows in open(filename)]
    for rows in content:
        row = map(str, rows.split())
        data.append(row)

    return data


def parse_data(row, column1, column2):
    try:
        temp_max = int(row[column1])
    except:
        for i in row[column1]:
            if not i.isdigit():
                temp_max = row[column1].replace(i, "")
        temp_max = int(temp_max)

    try:
        temp_min = int(row[column2])
    except:
        for i in row[column2]:
            if not i.isdigit():
                temp_min = row[column2].replace(i, "")
        temp_min = int(temp_min)

    difference = temp_max - temp_min

    return abs(difference)
