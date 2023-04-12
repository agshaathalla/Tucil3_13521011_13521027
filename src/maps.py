import gmplot


def findTengah(koordinat):
    minLat = 999999999
    minLong = 999999999
    maxLat = -999999999
    maxLong = -999999999
    
    for i in koordinat:
        if(koordinat[i][0] < minLong):
            minLong = koordinat[i][0]
        if(koordinat[i][0] > maxLong):
            maxLong = koordinat[i][0]
        if(koordinat[i][1] < minLat):
            minLat = koordinat[i][1]
        if(koordinat[i][1] > maxLat):
            maxLat = koordinat[i][1]
    return (minLat+maxLat)/2, (minLong+maxLong)/2


def showMap(koordinat, path):
    
    latitude_list = []
    longitude_list = []
    for i in path:
        latitude_list.append(koordinat[i][1])
        longitude_list.append(koordinat[i][0])

    
    lat_Tengah, long_Tengah = findTengah(koordinat)


    gmap = gmplot.GoogleMapPlotter(lat_Tengah, long_Tengah, 16, map_type='roadmap', apikey='AIzaSyDWuK0aq2_SvWoLxq-lGpRIrbWO7JBUc60')

    gmap.scatter( latitude_list, longitude_list, '#FF0000',size = 40, marker = False )
    gmap.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width = 2.5)

    gmap.draw('bin/maps.html')
