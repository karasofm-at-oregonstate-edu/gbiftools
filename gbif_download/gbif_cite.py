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
import glob
import os
import shutil
import re

dataDirs=[]
for file in os.listdir('.'):
  if os.path.isdir(file):
    dataDirs.append(file)


for dataDir in dataDirs:
    if not re.search(r'^\d\d\d\d\d\d\d-', dataDir):
        dataDirs.remove(dataDir)

failedOpens=[]

for dataDir in dataDirs:
    fn= "%s/citations.txt" % dataDir
    try:
        f = open(fn)
    except:
        failedOpens.append(fn)
        continue

    lines = f.readlines()
    for line in lines[1:]:
        print(line)
        
print("Some files failed to open:")
for failedOpen in failedOpens:
    print(failedOpen)
        

