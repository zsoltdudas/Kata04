class file_handling(object):

    def read_file(self, filename):
        data = []
        content = [rows.rstrip('\n') for rows in open(filename)]
        for rows in content:
            row = map(str, rows.split())
            if row and row[0][0].isdigit():
                data.append(row)

        return data

    def parse_data(self, row, column):
        try:
            data = int(row[column])
        except:
            for i in row[column]:
                if not i.isdigit():
                    data = row[column].replace(i, "")
            data = int(data)

        return data

    def smallest_difference(self, content, column1, column2):
        for row in content:
            high = self.parse_data(row, column1)
            low = self.parse_data(row, column2)
            difference = abs(high - low)
            self.spread.append(difference)

        smallest = self.spread.index(min(self.spread))

        return smallest
