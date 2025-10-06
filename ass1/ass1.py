import pandas as pd
import os
script_dir = os.path.dirname(__file__)
eng_path = os.path.join(script_dir, "dataset", "eng.txt")
hin_path = os.path.join(script_dir, "dataset", "hin.txt")
eng = open(eng_path, encoding="utf-8").read().splitlines()
hin = open(hin_path, encoding="utf-8").read().splitlines()
df=pd.DataFrame({"English":eng,"Hindi":hin})
df=df.dropna()
df["Word_Count_English"]=df["English"].apply(lambda x:len(x.split()))
df["Word_Count_Hindi"]=df["Hindi"].apply(lambda x:len(x.split()))
df=df[(df["Word_Count_English"].between(5,50))&(df["Word_Count_Hindi"].between(5,50))]
df["Difference"]=df["Word_Count_English"]-df["Word_Count_Hindi"]
df=df[df["Difference"].between(-10,10)]
df.to_excel("cleandat.xlsx",index=False)
