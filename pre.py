import pandas as pd

deb = 0
length = 30

name_df = "/Users/noahbensoussen/Desktop/archive/trade_prices/01.csv"

#df = pd.read_csv(name_df, skiprows=range(0, deb), nrows=length)
df = pd.read_csv(name_df)

df = df.drop(columns = ["No","Type","Region","MunicipalityCode","TimeToNearestStation","FloorPlan","AreaIsGreaterFlag","UnitPrice","PricePerTsubo","LandShape","FrontageIsGreaterFlag","TotalFloorArea","TotalFloorAreaIsGreaterFlag","PrewarBuilding","Use","Purpose","Classification","Breadth","CityPlanning","CoverageRatio","FloorAreaRatio","Period","Renovation","Remarks"])

df = df.dropna()

for i in range(2,48) :
	print(str(i), end='\r')

	if i<=9 :
		name_df_temp = "/Users/noahbensoussen/Desktop/archive/trade_prices/" + "0" + str(i) + ".csv"
	else :
		name_df_temp = "/Users/noahbensoussen/Desktop/archive/trade_prices/" + str(i) + ".csv"

	df_temp = pd.read_csv(name_df_temp)

	df_temp = df_temp.drop(columns = ["No","Type","Region","MunicipalityCode","TimeToNearestStation","FloorPlan","AreaIsGreaterFlag","UnitPrice","PricePerTsubo","LandShape","FrontageIsGreaterFlag","TotalFloorArea","TotalFloorAreaIsGreaterFlag","PrewarBuilding","Use","Purpose","Classification","Breadth","CityPlanning","CoverageRatio","FloorAreaRatio","Period","Renovation","Remarks"])

	df_temp = df_temp.dropna()

	df = pd.concat([df, df_temp]).reset_index(drop=True)

df.to_csv("data.csv", index=False)