message = str(input())

good = ':-)'
bad = ':-('
good_cnt = 0
bad_cnt = 0
for s in range(len(message)):
	if message[s] == '-':
		if good in message[s-1:s+2]:
			good_cnt += 1
		elif bad in message[s-1:s+2]:
			bad_cnt += 1
if good_cnt == 0 == bad_cnt:
	print('none')
elif good_cnt > bad_cnt:
	print('happy')
elif good_cnt < bad_cnt:
	print('sad')
elif good_cnt == bad_cnt:
	print('unsure')