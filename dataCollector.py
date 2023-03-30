from GlassdorScraper import GetInfo
import pandas as pd
print("Scaning...")
df = GetInfo('data scientist',1000)
df.to_excel("output.xlsx")

