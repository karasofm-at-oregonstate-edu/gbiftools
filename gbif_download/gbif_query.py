#Copywrite 2021 Mike Karasoff
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#One must set the following environment variables:
#GBIF_USER
#GBIF_PWD
#GBIF_EMAIL

from pygbif import occurrences as occ
from pygbif import species
import csv
import time
import sys

args = sys.argv
fn = args[1]

print(args)

print("reading", fn)

boundBox=[-122.55392149475273,
            37.595686384771945,
            -122.34243467834648,
           37.83197310811593] 



csvfile = open(fn)
plantData = csv.DictReader(csvfile)
dlList = []

longmin="decimalLongitude > %s" % boundBox[0]
latmin="decimalLatitude > %s" % boundBox[1]
longmax="decimalLongitude < %s" % boundBox[2]
latmax="decimalLatitude < %s" % boundBox[3]

for row in plantData:
  sp_name="%s" % row['Scientific Name'] 
  print(sp_name)
  gbifSpcInfo=species.name_backbone(name = sp_name)
  try:
      print(gbifSpcInfo['usageKey'])
  except:
        print(sp_name, "not found")
        continue

  taxonKeySel="taxonKey = %s" % gbifSpcInfo['usageKey']
  print(taxonKeySel)
  dl = occ.download( [ taxonKeySel, 'basisOfRecord = HUMAN_OBSERVATION', 'hasCoordinate = True', latmin, longmin, latmax, longmax ])

  dlMeta = occ.download_meta(dl[0])
  print(dlMeta)
  while dlMeta['status'] != 'SUCCEEDED' and dlMeta['status'] != 'KILLED':
      time.sleep(30)
      dlMeta = occ.download_meta(dl[0])
      print(dlMeta)
  
  if dlMeta['status'] == 'SUCCEEDED':
    dlList.append(dl)


for dl in dlList:
    try:
        occ.download_get(dl[0])
    except:
        pass
