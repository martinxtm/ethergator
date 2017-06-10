from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from geopy.geocoders import Nominatim
import math


players = []
players.append({})
players[0]['player_name'] = "dembele"
players[0]['player_networth'] = 28
players[0]['player_nation'] = "france"
players[0]['player_transfers'] = {"from_country" : "france", "to_country" : "germany", "abloese" : 15}

players.append({})
players[1]['player_name'] = "kroos"
players[1]['player_networth'] = 50
players[1]['player_nation'] = "germany"
players[1]['player_transfers'] = {"from_country" : "germany", "to_country" : "spain", "abloese" : 30}

players.append({})
players[2]['player_name'] = "aubameyang"
players[2]['player_networth'] = 75
players[2]['player_nation'] = "france"
players[2]['player_transfers'] = {"from_country" : "germany", "to_country" : "france", "abloese" : 75}

def FindOutgoingTransfersPerCountry():
    countries = {}
    for Player in players:
        from_country = Player['player_transfers']['from_country']
        to_country = Player['player_transfers']['to_country']
        abloese = Player['player_transfers']['abloese']
        growth_after_transfer = Player['player_networth'] - abloese
        if not countries.__contains__(from_country):
            countries[from_country] = {}
            countries[from_country][to_country] = {}
            countries[from_country][to_country]['transfer_sum'] = abloese
            countries[from_country][to_country]['growth_after_transfer'] = growth_after_transfer
        else:
            if not countries[from_country].__contains__(to_country):
                countries[from_country][to_country] = {}
                countries[from_country][to_country]['transfer_sum'] = abloese
                countries[from_country][to_country]['growth_after_transfer'] = growth_after_transfer
            else:
                countries[from_country][to_country]['transfer_sum'] = countries[from_country][to_country]['transfer_sum'] + abloese
                countries[from_country][to_country]['growth_after_transfer'] = countries[from_country][to_country]['growth_after_transfer'] + growth_after_transfer
    return countries

transfers_per_country = FindOutgoingTransfersPerCountry()
print(transfers_per_country)


'''
# set up orthographic map projection with
# perspective of satellite looking down at 50N, 100W.
# use low resolution coastlines.
map = Basemap(projection='ortho',lat_0=45,lon_0=0,resolution='l')
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.fillcontinents(color='coral',lake_color='aqua')
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='aqua')
# draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
# make up some data on a regular lat/lon grid.
#nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
#lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
#lons = (delta*np.indices((nlats,nlons))[1,:,:])
#wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
#mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
# compute native map projection coordinates of lat/lon grid.
#x, y = map(lons*180./np.pi, lats*180./np.pi)
# contour data over the map.
#cs = map.contour(x,y,wave+mean,15,linewidths=1.5)
plt.title('Transfers')
#plt.show()



# create new figure, axes instances.
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
m = Basemap(llcrnrlon=-100.,llcrnrlat=20.,urcrnrlon=20.,urcrnrlat=60.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=40.,lon_0=-20.,lat_ts=20.)
# nylat, nylon are lat/lon of New York
nylat = 40.78; nylon = -73.98
# lonlat, lonlon are lat/lon of London.
lonlat = 51.53; lonlon = 0.08
# draw great circle route between NY and London
m.drawgreatcircle(nylon,nylat,lonlon,lonlat,linewidth=2,color='b')
m.drawcoastlines()
m.fillcontinents()
# draw parallels
m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
# draw meridians
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
ax.set_title('Great Circle from New York to London')
#plt.show()



# miller projection
map = Basemap(projection='mill',lon_0=180)
# plot coastlines, draw label meridians and parallels.
map.drawcoastlines()
map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
# fill continents 'coral' (with zorder=0), color wet areas 'aqua'
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawgreatcircle(nylon,nylat,lonlon,lonlat,linewidth=20,color='b')
plt.title('Transfers')
#plt.show()
'''



cities = [["Chicago",10],
          ["Boston",10],
          ["New York",5],
          ["San Francisco",25]]
scale = 0.1

#map = Basemap(llcrnrx=45,llcrnry=100,urcrnrx=45,urcrnry=100)
#map = Basemap(llcrnrlon=-145.5,llcrnrlat=1.,urcrnrlon=-2.566,urcrnrlat=46.352,\
            #rsphere=(6378137.00,6356752.3142),\
            #resolution='l',area_thresh=1000.,projection='lcc',\
            #lat_1=50.,lon_0=-107.)
map = Basemap(projection='mill',lon_0=0)



map.drawcoastlines()
map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
# fill continents 'coral' (with zorder=0), color wet areas 'aqua'
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')

# load the shapefile, use the name 'states'
#map.readshapefile('st99_d00', name='states', drawbounds=True)

# Get the location of each city and plot it
geolocator = Nominatim()



for starting_country, target_countries in transfers_per_country.iteritems():
    loc_start = geolocator.geocode(starting_country)
    x, y = map(loc_start.longitude, loc_start.latitude)
    for target_country, target_data in target_countries.iteritems():
        map.plot(x,y,marker='o',color='Red',markersize=5)
        loc_target = geolocator.geocode(target_country)
        map.drawgreatcircle(loc_start.longitude, loc_start.latitude, loc_target.longitude, loc_target.latitude, linewidth=target_data['transfer_sum']*scale, color='b')
    #plot markers
    plt.annotate(starting_country, xy=(x, y), xycoords='data',
                 xytext=(x, y), textcoords='offset points',
                 color='r',
                 arrowprops=dict(arrowstyle="fancy", color='g')
                 )
plt.show()



# shade the night areas, with alpha transparency so the
# map shows through. Use current time in UTC.
#date = datetime.utcnow()
#CS=map.nightshade(date)
