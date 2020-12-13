#wyk/enumerate/zip
'''
workDays = [19, 21, 22, 21, 20, 22]

print(workDays)
print(workDays[2])

enumerateDays = list(enumerate(workDays))
print(enumerateDays)

#enumerate - numerujemy kazdy element z listy i tworza sie tumple
for pos, value in enumerateDays:
    print("Pos:", pos, "Value:", value)

month = ['I', 'II', 'III', 'IV', 'V', 'VI']

#zip - laczymy dwie tablice i tworza sie yumple(pary)
monthDay = list(zip(month,workDays))
print(monthDay)

for mon, day in monthDay:
    print('Month:', mon, 'Day:', day)

for pos, (mon, day) in enumerate(zip(month, workDays)):
    print('Pos:', pos, 'Month:', mon, 'Day:', day)
    print('{} - {} - {}'.format(pos, mon, day)
'''

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton', 'cosik']

for project, leader in zip(projects, leaders):
    print('The leader of {} is {}'.format(project, leader))

print('')

dates = ['2016-06-23', '2016-08-29', '1994-01-01']
for project, data, leader in zip(projects, dates, leaders):
    print('The leader of {} started {} is {}'.format(project, data, leader))

print('')

for position, (project, data, leader) in enumerate(zip(projects, dates, leaders)):
    print('{} The leader of {} started {} is {}'.format(position + 1, project, data, leader))
