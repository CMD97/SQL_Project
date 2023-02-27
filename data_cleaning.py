from data_extraction import DataExtractor

class DataCleaning:
    def __init__(self):
        de = DataExtractor()
        self.table = de.read_rds_table(de.table_names)
        self.cleandata = self.clean_user_data()
        print(self.table)

    def clean_user_data(self):
        # return cleandata
        pass

DataCleaning()