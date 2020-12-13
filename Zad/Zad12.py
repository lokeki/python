#listy i tuplets

marketing = ['loyality program', 'client program', 'market research']
print(marketing)

marketing.append('public relations')
print(marketing)

print(marketing[2])

marketing.insert(1, 'investor relations')
print(marketing)

emailMarketing = marketing.copy()

emailMarketing.sort()
print(emailMarketing)

internalEmails = ['internal communication']
print(internalEmails)

emailMarketing.extend(internalEmails)
print(emailMarketing)

tupleListMarketing = tuple(emailMarketing)
print(tupleListMarketing)

