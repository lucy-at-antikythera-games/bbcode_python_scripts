pings = '''alpha @bravo @charlie @xray @yankee @zulu'''
separator = ' @'

def sort_pings(pingtext, sep):
  # Writing out code like this for human readability
  pinglist = pingtext.split(sep)
  pingset = set(pinglist)
  ordered_pinglist = sorted(pingset, key=str.lower)
  ordered_pings = '@' + sep.join(ordered_pinglist)
  return ordered_pings

print(sort_pings(pings,separator))

# note to self: avoid double pings by running to_be_pinged_set.difference(pinged_set)
