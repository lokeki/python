#listy

hitsTitle = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitle.append('CHILD IN TIME')
hitsTitle.append('AGAIN')
print(hitsTitle)

hitsTitle.insert(2,'HOTEL CALIFORNIA')
print(hitsTitle)

hitsTitle.insert(0, 'THE SOUND OF SILENCE' )
print(hitsTitle)

print(hitsTitle.index('HOTEL CALIFORNIA'))

hitsTitle.remove("HOTEL CALIFORNIA")
print(hitsTitle)

hitsTitle[0] = 'ENJOY THE SILENCE'
print(hitsTitle)

hitsToRead = hitsTitle.copy()

hitsTitle.reverse()
print(hitsTitle)

hitsTitle.sort()
print(hitsTitle)

hitsTitle.pop(0)
hitsTitle.pop(0)

additionalSongs = ('NOTHING COMPARES 2 U', 'WISH YOU WERE HERE')
print(additionalSongs)

hitsTitle.extend(additionalSongs)
print(hitsTitle)

print(hitsTitle.count('WISH YOU WERE HERE'), ' and ', hitsTitle.count('RIDERS ON THE STORM'))

hitsToRead.clear()



