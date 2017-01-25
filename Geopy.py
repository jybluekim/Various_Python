import geopy

print ("Working on geopy")

from  geopy.geocoders import Nominatim

nom=Nominatim()

x = nom.geocode("756 Rosewood Dr, Palo Alto, CA 94303")

print (type (x))

print (x.longitude, x.latitude)

