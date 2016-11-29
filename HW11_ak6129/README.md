
HW 11

Assignment 1 
For this assignment I uploaded nycb2010.shp shape file from nyc.gov. 
Then extracted Brooklyn shape polygon and converted coordinates to lan/lot.
After that I found CUSP coordinated from http://www.gps-coordinates.net/ and created Point shapely geometry with the coordinates of CUSP
Loop over the Brookly polygons. Found in which geometry the polygon is contained.
Ploted CUSP point.

Assignment 2
Downloaded Census Business data for period from 1993 to 2015 and geojson file from the github repo. 
Merged 2 data sets to prepare the data for clustering.
Cluster the NUMBER OF ESTABLISHMENTS time series with K-means. Used elbow method to identify number of clusters. 
The elbow method shows 2 clusters. Choosed 5 as number of cluster as per instructions.
Plot cluster centeres that shows that all clusters have different trends.
Used another clustering algorithm and plot dendrogram.
Merged nyc_shape with k-means and hierarchical labels and plot kmeans cluster and hierarchical cluster on NYC Map.
Compared results. 

Group: I received help and instructions for both assignments from Mona. 




