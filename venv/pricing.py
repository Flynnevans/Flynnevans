
import pandas as pd

def concrete_price(t,v):
    df = pd.read_csv("concrete.csv")


    x = list(df[t])[int(v//0.25)-1]

    print(x)
    return (x)

