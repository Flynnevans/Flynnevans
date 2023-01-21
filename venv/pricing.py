
import pandas as pd

def concrete_price(t,v):
    df = pd.read_csv("concrete.csv")

    v = round(v * 4)
    v = (v/4)
    x = list(df[t])[int(v//0.25)-1]


    return (x)

