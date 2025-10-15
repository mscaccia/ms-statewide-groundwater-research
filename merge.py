import pandas as pd

df1 = pd.read_csv(r"C:\Users\scacc\Desktop\MS_UC\Repositories\ms-statewide-groundwater-research\WilliamsCoWells\GEO_FORM_WilliamsCo.csv")
df2 = pd.read_csv(r"C:\Users\scacc\Desktop\MS_UC\Repositories\ms-statewide-groundwater-research\WilliamsCoWells\Wells_Logs.csv")

new_df2= df2[["WELL_LOG_NO", "LAT", "LON", "Head", "RASTERVALU", "NEW_COMP_ELEV"]].copy()
print(new_df2)
