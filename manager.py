def read_file(filename):
    data = []
    content = [rows.rstrip('\n') for rows in open(filename)]
    for rows in content:
        row = map(str, rows.split())
        data.append(row)

    return data


def parse_data(row, column):
    try:
        data = int(row[column])
    except:
        for i in row[column]:
            if not i.isdigit():
                data = row[column].replace(i, "")
        data = int(data)

    return data
