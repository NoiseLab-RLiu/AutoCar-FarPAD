import matplotlib.pyplot as plt
import numpy as np

	# position is based on a -128, +127 basis
	harzard_index = (100, 50)
	#here's our data to plot, all normal Python lists
	x = range(-64,64) # x, y range from -64 to +63
	y = range(-64,64)

	# initalize the intensity array 
	intensity = 128*[128*[0]] 

	current_harzard = harzard_index[0]
	normalized_position = harzard_index[1] + 64

	left = normalized_position
	right = normalized_position
	while current_harzard >= 0 and left >= 0 and right <=  127:
		for i in xrange(128):
			intensity[i][left] = current_harzard
			intensity[i][right] = current_harzard
		left -= 1
		right += 1
		current_harzard -= 10


	#setup the 2D grid with Numpy
	x, y = np.meshgrid(x, y)

	#convert intensity (list of lists) to a numpy array for plotting
	intensity = np.array(intensity)

	#now just plug the data into pcolormesh, it's that easy!
	plt.pcolormesh(x, y, intensity)
	plt.colorbar() #need a colorbar to show the intensity scale
	plt.show() #boom
