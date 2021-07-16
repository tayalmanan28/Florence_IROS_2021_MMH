from copy import deepcopy
import os
import math
import time
from copy import deepcopy

T = 0
step = 10
DEL_LIMIT = 60
SAN_LIMIT = 10

## Clear screen
def clear():
  os.system('cls')

## Pass time by one step
def time_pass():
  global T, step
  T = T + step

## Format names, ages, and times in database to printable strings
ageCharLim = 3
nameCharLim = 24
timeCharLim =  4
def value_format(bare, vType):
  if vType = 0:
    vCharLim = nameCharLim
  elif vType = 1:
    vCharLim = ageCharLim  
  elif vType = 2:
    vCharLim = timeCharLim  
  if len(bare) >= vCharLim: 
    return (bare, deepcopy(bare[:vCharLim]))
  val = deepcopy(bare)
  while len(val) < vCharLim:
    val = val + ' '
  return (bare, val)
## Format database entry to list of printable strings
### entry = [Formatted-Name, Formatted-Age, Status, MED, Formatted-LD, Formatted-LS, Name, Age, LD, LS]
def entry_format(inEntry):
  bare_name, bare_age, stat, med, bare_ld, bare_ls = inEntry
  entry = [value_format(bare_name, 0), value_format(bare_age, 1), stat, med, value_format(bare_ld, 2), value_format(bare_ls, 2), bare_name, bare_age, bare_ld, bare_ls]
  return entry  
### Display database to user
def db_display(DB):
  clear()
  print(' ------------------------------------------------------------------------ ')
  print('| Name                     | Age | Status | MED | LAST_DETECT | LAST_SAN |')
  for entry in DB:
    print('| '+entry[0]+' | '+entry[1]+' |      '+entry[2]+' |   '+entry[3]+' |        '+entry[4]+' |     '+entry[5]+' |')
  print(' ------------------------------------------------------------------------ ')

## Remove visitor entry after DEL_LIMIT minutes
def visit_delete(DB):
  global T
  DB_new = [entry for entry in DB if not (entry[2] == 'V' and entry[8] < T - DEL_LIMIT)]
  return DB_new

## Revise LAST_DETECT value on meeting person
def meet_person(DB, name):
  global T
  entryNum = 0
  for entry in DB:
    if entry[0] == value_format(name, 0):
      DB[entryNum][8] = T
      DB[entryNum][4] = value_format(T, 2)
      break
    entryNum += 1
  if DB[entryNum][9] < T - SAN_LIMIT:
    DB[entryNum][9] = T
    DB = sanitize_person()
  return DB

## Sanitize person
def sanitize_person():
  # Function to demonstrate the flow process of entering sanitization subroutine
  pass

## Time-of-Day-based Medicine Update
#### MED is set to 0 every morning (0730 hrs), afternoon (1300 hrs), and night (1930 hrs)
def medicine_tUpdate(DB):
  if T == 450 or T == 780 or T == 1170:
    for entryNum, entry in enumerate(DB):
      if entry[2] == 'P':
        DB[entryNum][3] = 0
  return DB

## Run a custom event provided by the 
def runEvent(event):
  # Function to demonstrate the flow process of performing a requested custom event
  pass

def main(inputs, events):
  global T
  DB = []
  for inEntry in inputs:
    DB.append(entry_format(inEntry))
  
  while True:
    if len(events) != 0:
      if events[0][0] <= T:
        runEvent(events[0])
        events = events[1:]
    DB = visit_delete(DB)
    DB = medicine_tUpdate(DB)
    db_display(DB)
    time_pass()
    if T > 1320:  ## Program runs until 2200 hrs
      break
    time.sleep(5)

if __name__ == '__main__':
  inputs = [['Aaron John Sabu', 22, 'P', ],
            [      'Sabu John', 57, 'V', ],
            [],
            [],
            [],]
  events = []
  main(inputs, events)