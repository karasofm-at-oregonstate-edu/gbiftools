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
import glob
import zipfile
import csv
import os
import shutil

zippedFiles=glob.glob("*.zip")

plantData=[]

for zippedFile in zippedFiles:
  dirName, fileExt = os.path.splitext(zippedFile)
  if os.path.exists(dirName):
    shutil.rmtree(dirName)
  os.mkdir(dirName)
  with zipfile.ZipFile(zippedFile, 'r') as zip_ref:
    zip_ref.extractall(dirName)
  
  locDataFn="%s/occurrence.txt" % dirName
  
  locData = list(csv.DictReader(open(locDataFn, 'r'), delimiter='\t'))
  plantData.extend(list(locData))

try:
  fieldNames = plantData[0].keys()
except:
  exit(0)

with open('scrubCommunityPlants.csv', 'w', newline='') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
  writer.writeheader()
  for entry in plantData:
    writer.writerow(entry)

  

