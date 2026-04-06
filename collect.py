# %%
import pandas as pd
pd.set_option('display.max_columns', None)
import fastf1
import time
import argparse
<<<<<<< HEAD
=======

#%%
#df = pd.read_parquet("data/2019_01_R.parquet")
#df
>>>>>>> 8641fe4 (Adicionado o envio dos dados para nuvem)
#%%

class CollectResults:
    def __init__(self, years=[2021,2022,2023], modes=["R","S"]):
        self.years = years
        self.modes = modes
    
    def get_data(self, year, gp, mode)->pd.DataFrame:
        try:
            session = fastf1.get_session(year, gp, mode)
        
        except ValueError as err:
            return pd.DataFrame()
        
        session._load_drivers_results()
<<<<<<< HEAD

        df = session.results
        df["Mode"] = mode

        return df
    
    def save_data(self,df,year,gp,mode):
        df.to_parquet(f"data/{year}_{gp:02}_{mode}.parquet")
=======
        df = session.results

        df["Year"] = session.date.year
        df["Date"] = session.date
        df["Mode"] = session.name
        df["RoundNumber"] = session.event["RoundNumber"]
        df["OfficialEventName"]=session.event["OfficialEventName"]
        df["Country"]=session.event["Country"]
        df["Location"]=session.event["Location"]

        return df

    
    def save_data(self,df:pd.DataFrame,year:int,gp:int,mode:str):
        filename = f"data/{year}_{gp:02}_{mode}.parquet"
        df.to_parquet(filename, index=False)
>>>>>>> 8641fe4 (Adicionado o envio dos dados para nuvem)

    def process(self,year, gp, mode):
        df = self.get_data(year, gp, mode)
        if df.empty:
            return False
        self.save_data(df,year,gp, mode)
<<<<<<< HEAD
=======
        time.sleep(1)
>>>>>>> 8641fe4 (Adicionado o envio dos dados para nuvem)
        return True

    def process_year_modes(self,year):
        for i in range(1,50):
            for mode in self.modes:
                if not self.process(year,i,mode) and mode=="R":
                    return
                
    def process_years(self):
        for year in self.years:
            print(f"Coletando dados do ano {year}")
            self.process_year_modes(year)
            time.sleep(10)
# %%

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
<<<<<<< HEAD
    parser.add_argument("--years","-y",nargs="+", type=int)
    parser.add_argument("--modes","-m",nargs="+")

    args = parser.parse_args()

    collect = CollectResults(args.years,args.modes)
=======

    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int, default=0)
    parser.add_argument("--years","-y",nargs="+", type=int)
    parser.add_argument("--modes","-m",nargs="+")
    args = parser.parse_args()

    if args.years:
        collect = CollectResults(args.years, args.modes)
    elif args.start !=0 and  args.stop !=0:
        years = [i for i in range(args.start, args.stop+1)]
        collect = CollectResults(years, args.modes)
>>>>>>> 8641fe4 (Adicionado o envio dos dados para nuvem)
    collect.process_years()
# %%