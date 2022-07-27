def get_table(name, connection, columns):
    query = ' SELECT * FROM {}; '.format(name)
    return pd.DataFrame(execute_query(connection, query), columns=columns)


class LibraryTable:
    def __init__(self, name, df):
        self.name = name
        self.df = df

    def span(self, period, column):
        self.df = self.df[(self.df[column] > period[0]) & (self.df[column] < period[1])]
        return self.df

    def name_check(self, columns, name):
        if len(columns) == 1:
            stuff = self.df[columns[0]].apply(lambda z: z.split(' '))
            if any(stuff.apply(lambda z: name.lower() in [w.lower() for w in z])):
                self.df = self.df[stuff.apply(lambda z: name.lower() in [w.lower() for w in z] + [''])]
                return self.df
        stuff = self.df[columns].apply(lambda z: z.apply(lambda y: y.split(' ')))
        stuff_bool = stuff.apply(lambda z: z.apply(lambda y: name.lower() in [w.lower() for w in y] + ['']))
        if any(stuff_bool):
            self.df = self.df[stuff_bool.T.apply(lambda z: any(z))]
            return self.df
