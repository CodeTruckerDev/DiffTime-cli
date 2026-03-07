#!/usr/bin/env python3 
import sys 
from datetime import datetime 

FMT = "%d-%m %H:%M" 

def parse(dt_str): 
  return datetime.strptime(dt_str.strip(), FMT) 

def difftime(start_str, end_str): 
  start = parse(start_str) 
  end = parse(end_str) 
  diff = abs(end - start)
  total_minutes = int(diff.total_seconds() // 60) 
  return total_minutes // 60, total_minutes % 60 

def main(): 
  if len(sys.argv) == 3: 
    start_str, end_str = sys.argv[1], sys.argv[2] 
  else: 
    lines = sys.stdin.read().strip().splitlines() 
    if len(lines) != 2: 
      sys.exit("Provide two datetimes as args or via stdin (two lines).") 
    start_str, end_str = lines 
      
  hours, minutes = difftime(start_str, end_str) 
  print(f"{hours}h {minutes}m") 
  
  if __name__ == "__main__": 
    main()
