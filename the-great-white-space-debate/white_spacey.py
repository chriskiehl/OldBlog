'''
Created on Apr 19, 2014

@author: Chris
'''

import os 
import re
from functools import partial

def get_src_files(root, extension='.java'):
  for root, _, files in os.walk(root):
    yield from (os.path.join(root, f) for f in files
                if f.endswith(extension))
    
def read_files(filenames):
  for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as f:
      yield from f.readlines()

def extract_forloops(lines):
  yield from (
      line.strip() for line in lines
      if 'for (' in line
      # One of those god forsaken 'enhanced' for loops. Ignore
      and ':' not in line
  )

if __name__ == '__main__':
  spaced_apart = partial(re.search, '[a-zA-Z]\s\=')
  grouped_together = partial(re.search, '[a-zA-Z]\=')
  
  java_src_path = r'C:\Program Files\Java\jdk1.8.0_20\src'
  guava_src_path = r'C:\Users\Chris\Dropbox\JavaSources\guava-libraries'
  gwt_src_path = r'C:\Users\Chris\Dropbox\JavaSources\gwt'
  forloops = extract_forloops(read_files(get_src_files(gwt_src_path)))

  counts = {'spaced': 0, 'nonspaced':0}
  for loop in forloops:
    if grouped_together(loop):
      counts['nonspaced'] += 1
    elif spaced_apart(loop):
      counts['spaced'] += 1
  print(counts)