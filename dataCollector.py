from GlassdorScraper import GetInfo
import pandas as pd
print("Scaning...")
df = GetInfo("Software engineer",200)
df.to_excel("output.xlsx")
