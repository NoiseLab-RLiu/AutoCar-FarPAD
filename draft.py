def compute(left_x, top_y,   width,   height):
	left = left_x - width/2
	top = top_y - height/2
	right = left +  width
	bot = top +  height
	return [left, top, right, bot]

print compute(248 , 156 ,  98  , 206)
print compute(291   ,  152  ,  96   , 209)
print compute(487  ,  109   ,  110   ,  254)




# # python range can only do intergers 
# acc = 0.01
# print acc
# for i in xrange(8):
# 	acc += 0.12375
# 	print acc 

# (0.07 + 0.09 + 0.10 + 0.14)/9 = 0.04444
# rate = 0.07, fppi = 0.47 *** any fppi greater than 0.47
# rate = 0.09, fppi = 0.42
# rate = 0.09, fppi = 0.38 ***
# rate = 0.10, fppi = 0.31
# rate = 0.10, fppi = 0.25 ***
# rate = 0.10, fppi = 0.20
# rate = 0.13, fppi = 0.15
# rate = 0.12, fppi = 0.19
# rate = 0.13, fppi = 0.16
# rate = 0.13, fppi = 0.15
# rate = 0.13, fppi = 0.15
# rate = 0.14, fppi = 0.14
# rate = 0.14, fppi = 0.13 ***
# rate = 0.15, fppi = 0.12 
# rate = 0.15, fppi = 0.08
# rate = 0.16, fppi = 0.08
# rate = 0.17, fppi = 0.08
# rate = 0.17, fppi = 0.06
# rate = 0.18, fppi = 0.06
# rate = 0.18, fppi = 0.06 

# AP
# 2000 89
# 4000 80
# 6000 88
# 8000 81
# 9000 81.71
# 9800 89.24
# 10000 89.91
# 10200 81.00
# 11000 89.12
# 11200 89.40
# 11400 81.71
# 12000 81.18
# 13800 81.78
# 14000 90.14
# 14200 81.63
# 16000 88.71
# 18000 81.75
# 19800 81.70
