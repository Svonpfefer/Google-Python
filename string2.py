#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  add = ''
  if len(s) <= 3:
    pass
  elif s[(len(s)-3):len(s)] == 'ing' :
    add = 'ly'
  else:
    add = 'ing'
  
  return s + add


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  notsearch = s.find('not')
  badsearch = s.find('bad')
  oldstring = s[notsearch:(badsearch+3)]
  if notsearch !=-1  and badsearch !=-1 and ( notsearch < badsearch) :
     s= s.replace(oldstring,'good')
  else:
    pass
  return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  alength = len(a)
  blength = len(b)
  if alength % 2 != 0 or blength % 2 != 0:
    if alength % 2 != 0:
        parta_1 = a[0:(alength/2+1)]
        parta_2 = a[(alength/2+1):alength]
    else:
        parta_1 = a[0:alength/2]
        parta_2 = a[alength/2:alength]
        
    if blength % 2 != 0:
        partb_1 = b[0:(blength/2+1)]
        partb_2 = b[(blength/2+1):blength]
    else:
        partb_1 = b[0:blength/2]
        partb_2 = b[blength/2:blength] 
    

  else:
    parta_1 = a[0:alength/2]
    parta_2 = a[alength/2:alength]
    partb_1 = b[0:blength/2]
    partb_2 = b[blength/2:blength] 
  return parta_1 + partb_1 + parta_2 +partb_2


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
