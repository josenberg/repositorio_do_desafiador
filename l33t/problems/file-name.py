#!/usr/bin/env python
trash = input()
file_name = input()

asw = 0
while True:
  founded_index = file_name.find('xxx')
  if (founded_index == -1):
      break;
  else:
      asw = asw + 1
      file_name = file_name[:founded_index] + file_name[founded_index + 1:]

print(asw)
