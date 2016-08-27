#!/usr/bin/python
import sys
import csv

if __name__ == '__main__':
  if len(sys.argv) < 3:
    progname = sys.argv[0]
    print
    print "Usage: " + progname + " scheduleFile teamTranslator"
    print
    print "ScheduleFile should be in comma-separated format with a header row containing a column for week and along with all team placeholders (e.g., NFC 1, AFC 3, etc."
    print
    print "TeamTranslator should be a tab-separated file with each line containing a team placeholder and a team name (separated by a tab). Example line:"
    print "NFC 3	Poppa Kapp"
    exit()
  schedule = sys.argv[1]
  teamfile = sys.argv[2]
  teams = {}
  with open(teamfile) as teamf:
    for line in teamf:
      parts = line.strip().split("\t")
      if len(parts) > 1:
        teams[parts[0]] = parts[1]

  with open(schedule) as skedfile:
    skedReader = csv.reader(skedfile)
    headerFlag = True
    headers    = {}
    for row in skedReader:
      if headerFlag:
        headerFlag = False
        headerIndex = 0
        for col in row:
          headers[col] = headerIndex
          headerIndex += 1
        continue
      try:
        week = int(row[headers['Week']])
        print "Week " + str(week)
        done = {}
        if (0 < week < 15):
          for teamId in teams:
            team     = teams[teamId]
            opponent = teams[row[headers[teamId]]]
            if not team in done:
              print team + ' vs ' + opponent
            done[team]     = True
            done[opponent] = True            
          print
          
      except:
        continue
  
