import numpy as np
import pandas as pd
import io


data_file = "strmlit/clean_data_for_analysis.csv"
df = pd.read_csv(data_file)

type(df.info())

