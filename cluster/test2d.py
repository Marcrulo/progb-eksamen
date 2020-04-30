from pandas import DataFrame, read_csv, to_numeric
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

months = ['januar', 'februar', 'marts','april','maj','juni','juli','august','september','oktober','november','december']
categories = ["date","driving","drugs","lethal","other","stealing","violence"]

df = read_csv("../csv/crime.csv", sep=";", names=categories)
for item in categories[1:]:
	df[item] = df[item].str.replace('\'','').astype(int)

for i in range(len(df['date'])):
	for month in months:
		if month in str(df['date'][i]):
			df['date'][i] = months.index(month)+1 

print(df['date'])

kmeans = KMeans(n_clusters=2).fit(df[["driving","date"]])
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['driving'], df['date'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()