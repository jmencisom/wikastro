from astropy.coordinates import SkyCoord, get_constellation
astropy.time.Time.erfaWarnings=False
ra='11h55m45s'
dec='+55d19m14s'
c = SkyCoord(ra, dec, frame='icrs')
print get_constellation(c)