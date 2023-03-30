from GlassdorScraper import GetInfo
import pandas as pd
print("Scaning...")
df = GetInfo("Data scientist",100)
df.to_excel("output2.xlsx")

