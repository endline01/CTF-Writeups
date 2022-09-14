#!/usr/bin/python3
output = [18104, 60672, 252228, 71314, 220302, 432082, 168152, 92598, 60672, 71314, 327782, 294796, 220302, 359708, 92598, 252228, 327782, 294796, 349066, 306498, 294796, 199018, 327782, 156450, 113882, 125584, 60672, 156450, 327782, 294796, 306498, 359708, 145808, 327782, 71314, 349066, 145808, 327782, 81956, 410798]
for i in output:
	#brute force on 127 ascii chars value
	for x in range(128):
		#make the same equation on the ascii values and if its equal to it, then its our flag char
		if i ==((x<<1 * 23244 )>>3)%435262:
			print(chr(x),end='')
