import pandas as pd
import datetime
import time

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
            output: self.tags_dict  """
        
        self.tags_dict = pd.read_csv(tags_file, header=0, names = ('tag','bat_name'))
        self.tags_dict.set_index('tag', inplace=True)
        self.tags_dict = self.tags_dict.to_dict()
        # print (self.tags_dict['bat_name'])

    def time_index(self):
        """ adds headers and convert time to datetimeIndex
            input: self.df
            output: self.df """

        self.df.columns = ["A", "B", "TAG", "D", "db", "F", "time", "H", "ANTENNA", "J"]
        self.df['TIME'] = pd.to_datetime(self.df['time'])
        self.df = self.df.set_index(['TIME'])
        self.df.pop('time')
        # print (self.df)

    def find_bats(self):
        """ uses tags_dict to recognize bats (names) activity
            input: self.df, self.tag_dict
            output: self.bats_activity """

        self.bats_activity = self.df.copy()
        self.bats_activity.replace({'TAG': self.tags_dict['bat_name']}, inplace= True)
        self.bats_activity.rename(columns={"TAG": "bat"}, inplace=True)
        self.bats_activity.drop(columns=["A",'B','D','db','F','H','J'], inplace=True)
        print (self.bats_activity)
        

    def export_csv(self):
        """ saves bats_activity into csv file
            input:  self.bats_activity
            output: {date}.bats_activity.csv """

        self.bats_activity.to_csv(f"bats_activity_{pd.Timestamp.now().strftime('%Y-%m-%d')}.csv")
        

        
    def remove_duplicates (self):
        """ removes duplicates reads in a minute"""
        pass
    
    def run (self):
        """ main"""

        self.read_tags_dict()
        self.time_index()
        self.find_bats()
        print ("Working...")
        self.export_csv()
        print ('Done!')





if __name__ == "__main__":

    fname = 'test_02-06-20.csv'
    tags_file = 'mock_dict.csv'
    data = DATA(fname, tags_file)
    data.run()