import pandas as pd

def find_eco_low_calorie_products(df):
    # Code here
     return df[
        (df["eco_friendly"] == "Y") &
        (df["calories"] <= 200)
    ][["product_id", "product_name", "calories"]]