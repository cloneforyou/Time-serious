from datetime import datetime
import pandas as pd
import simplejson as json

#Analyse all the things

def niceNumber(n):

	if n < 1000000:
		return format(int(n), ",d")
	if n > 999999 and n < 1000000000:
		return format(int(n)/1000000, ",d") + 'm'
	if n > 999999999 and n < 1000000000000:
		return format(int(n)/1000000000, ",d") + 'bn'	

def analyseData(url,source,units,entity):
	results = {}
	results["summary"] = {}

	df = pd.read_csv(url)

	# print df
	#Year trend
	gpYear = df.groupby('datetime')
	yearSum = gpYear.sum()
	yearMean = gpYear.mean()
	# print yearSum.to_json()
	results["summary"]["yearSum"] = yearSum.to_json()
	results["summary"]["yearMean"] = yearMean.to_json()
	results["all"] = df.sort_values(by='value',ascending=False).to_json(orient='records')

	yearPctChange = yearSum.pct_change()

	currYearPctChange = round(yearPctChange.sort_index(ascending=False)["value"].iloc[0] * 100,1)
	results["summary"]["currYearPctChange"] = currYearPctChange

	print yearSum.sort(ascending=False)["value"].iloc[0]
	mostRecentYearTotal = yearSum.sort_index(ascending=False)["value"].iloc[0]
	results["summary"]["mostRecentYearTotal"] = mostRecentYearTotal
	results["summary"]["mostRecentYearTotalStr"] = niceNumber(mostRecentYearTotal)

	mostRecentYear = yearSum.sort_index(ascending=False).index[0]
	results["summary"]["mostRecentYear"] = mostRecentYear

	mostRecentYearMean = yearMean.sort_index(ascending=False)["value"].iloc[0]
	results["summary"]["mostRecentYearMean"] = mostRecentYearMean
	
	# print mostRecentYear
	biggestEntity = df.sort_values(by="value",ascending=False)["name"].iloc[0]
	
	results["summary"]["biggestEntity"] = biggestEntity

	dfnonull = df[(df["value"] != 0) & pd.notnull(df["value"])]
	# dfnonull = dfnozeros[pd.notnull(df["value"])]

	smallestEntity = dfnonull.sort_values(by="value",ascending=True)["name"].iloc[0]
	results["summary"]["smallestEntity"] = smallestEntity

	topTen = []
	for x in xrange(0,10):
		topTen.append(df[df['datetime'] == mostRecentYear].sort_values(by="value",ascending=False)["name"].iloc[x])
			
	results["summary"]["topTen"] = topTen
		
	onlynull = df[(df['datetime'] == mostRecentYear) & pd.isnull(df['value'])]
	if len(onlynull.index) > 0:
		if len(onlynull.index) == 1:
			nullSentence = "There was only one " + entity + " that did not report in " + str(mostRecentYear) + ", which was " + str(onlynull['name'].iloc[0])
		if len(onlynull.index) > 1 :
			nullSentence = "There were " + str(onlynull.index) + " " + entity + " that did not report in " + mostRecentYear 
		results['summary']['nullSentence'] = nullSentence

	# print results

	# newJson = json.dumps(jsonStr, indent=4)
	with open('allresults.json','w') as fileOut:
			fileOut.write(df.sort_values(by='value',ascending=False).to_json(orient='records'))
	with open('yearMean.json','w') as fileOut:
			fileOut.write(yearMean.to_json())
	with open('yearSum.json','w') as fileOut:
			fileOut.write(yearSum.to_json())
	with open('summary.json','w') as fileOut:
			fileOut.write(json.dumps(results["summary"]))							
			
	return results