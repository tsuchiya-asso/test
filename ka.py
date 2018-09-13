import pandas as pd

'''
etf_list = [
1309,#上海株式指数・上証50連動型上場投資信託
1313,#サムスンKODEX200証券上場指数投資信託
1314,#上場インデックスファンドS&P日本新興株100
1322,#上場インデックスファンド中国A株（パンダ）CSI300
1326,#SPDRゴールド・シェア
1343,#NEXT FUNDS 東証REIT指数連動型上場投信
1543,#純パラジウム上場信託（現物国内保管型）
#1548,#上場インデックスファンド中国H株（ハンセン中国企業株）
1551,#JASDAQ-TOP20上場投信
1633,#NEXT FUNDS 不動産（TOPIX-17）上場投信
1673,#ETFS 銀上場投資信託
1678,#NEXT FUNDS インド株式指数・Nifty 50連動型上場投信
1681,#上場インデックスファンド海外新興国株式（MSCIエマージング）
1682,#NEXT FUNDS 日経・東商取白金指数連動型上場投信
1698,#上場インデックスファンド日本高配当（東証配当フォーカス100）
]
'''
etf_list = [
1309,#上海株式指数・上証50連動型上場投資信託
1313,#サムスンKODEX200証券上場指数投資信託
1314,#上場インデックスファンドS&P日本新興株100
1322,#上場インデックスファンド中国A株（パンダ）CSI300
1326,#SPDRゴールド・シェア
1343,#NEXT FUNDS 東証REIT指数連動型上場投信
1543,#純パラジウム上場信託（現物国内保管型）
1548,#上場インデックスファンド中国H株（ハンセン中国企業株）
1551,#JASDAQ-TOP20上場投信
1633,#NEXT FUNDS 不動産（TOPIX-17）上場投信
1673,#ETFS 銀上場投資信託
1678,#NEXT FUNDS インド株式指数・Nifty 50連動型上場投信
1681,#上場インデックスファンド海外新興国株式（MSCIエマージング）
1682,#NEXT FUNDS 日経・東商取白金指数連動型上場投信
1698,#上場インデックスファンド日本高配当（東証配当フォーカス100）
]























df = pd.read_excel("kabu.xls", sheet_name='s6301', header=0, skiprows=[1])
df.columns=["Date", "Open", "High", "Low", "Close", "Volume", "Final"]
df["index"] = [i for i in range(len(df))]
print(df.head(10))


for etf in etf_list:
	#df_etf = pd.read_csv("etf_" + str(etf) + ".csv", header=0)
	df_etf = pd.read_excel("kabu.xls", sheet_name='s' + str(etf), header=0, skiprows=[1])
	df_etf.columns=["Date", "Open", "High", "Low", "Close", "Volume", "Final"]
	dates = []
	closeis = []
#	print(df_etf.head(10))
	for d in df["Date"]:
		d2 = str(d)[0:10]
		#print(d2)
		#if(df_etf.Date == d2)
		#print(df_etf.loc[(df_etf.Date == d2), "Date"])
		date = df_etf.loc[(df_etf.Date == d2), "Date"]#野村総合研究所の日付をETFファイルから検索
		#print("##############")
		#print(date)
		#print("#########")
		#print(df_etf.Date)
		#yesterday_date = date.values[0]
		#print(yesterday_date)
		if len(date)!=0:
			dates.append(date.values[0])#日付をデータセットに追加
		close = df_etf.loc[(df_etf.Date == d), "Close"]#日付が一致した日のETFのCloseのデータを取り出す
		#print(close.values[0])
		if len(close)!=0:
			if str(close.values[0]) != str("nan"):#取り出したCloseがnanでないかを判断
				yesterday_close = close.values[0]
				closeis.append(close.values[0])

			else:
				closeis.append(yesterday_close)

	df_etf2 = pd.DataFrame({"Date_" + str(etf) : dates, "Close_" + str(etf) : closeis})#新しくデータフレームを作成
	df = pd.concat([df, df_etf2], axis=1)#野村総合研究所のデータとETFデータを統合

print(df.head(10))
