import pandas as pd
import datetime

class DATA:
    def __init__ (self,fname, tags_file):
        self.fname = fname    
        self.df = pd.read_csv(self.fname)
        self.tags_file = tags_file
        self.tags_dict = None
        self.bats_activity = None

    def read_tags_dict(self):
        """ reads tags-bats csv file into tags_dict
            input: tags-bats csv file
            output: tags_dict  """
        pass

    def time_index(self):
        """ adds headers and convert time to datetimeIndex
            input: self.df
            output: self.df """

        self.df.columns = ["A", "B", "TAG", "D", "db", "F", "time", "H", "ANTENNA", "J"]
        self.df['TIME'] = pd.to_datetime(self.df['time'])
        self.df = self.df.set_index(['TIME'])
        self.df.pop('time')

    def export_csv(self):
        """ saves bats_activity into csv file
            input:  self.bats_activity
            output: {date}.bats_activity.csv """
        
        pass

    









if __name__ == "__main__":
    # fname = 'test_19-01-20.csv'
    # data = DATA(fname)
    # data.run()