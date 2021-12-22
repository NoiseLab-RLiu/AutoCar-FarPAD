import matplotlib.pyplot as plt
import numpy as np

class Heatmap():
	'''plot the heatmap of the harzard index of all the idenfiied person in the frame
	'''
	def __init__(self, data):
		'''get index array of all the people in the frame
		'''
		assert len(data) == 6 # data is a arrary of 6 sub arraies of parameters.

		self.distance = data[0] # distance is the size of the bounding box.
		self.distance_weight = data[1]
		self.position = data[2] # position is the distance to the center line
		self.position_weight = data[3]
		self.age = data[4]
		self.age_weight = data[5]

		self.harzard_arrary = [] # save the harzard of each people and distance in the given data frame
		# harzard index, relative position to the center vertical of the frame, bounding box size

		for i in xrange(len(distance)):
			self.calculate(i)

	def calculate(self, person_idx):
		'''calculate the harzard update the self.harzard_arrary 
		'''
		i = person_idx
		cur_harzard = self.distance[i] * self.distance_weight + \
		abs(self.position[i]) * self.position_weight + self.age[i] + self.age_weight 
		self.harzard_arrary.append((cur_harzard, self.position[i]))

		return 

	def get_intensity(self):
		'''get the harzard intensity matrix of the current frame
		'''
		# initalize the intensity array 
		intensity = 128*[128*[0]] 

		for harzard_index in self.harzard_arrary:
			current_harzard = harzard_index[0]
			normalized_position = harzard_index[1] + 64

			left = normalized_position
			right = normalized_position
			while current_harzard >= 0 and left >= 0 and right <=  127:
				for i in xrange(128):
					if intensity[i][left] < current_harzard:
						intensity[i][left] = current_harzard
					if intensity[i][right] < current_harzard:
						intensity[i][right] = current_harzard
				left -= 1
				right += 1
				current_harzard -= 10 # degenerate harzard index on a 10/unit basis
		return intensity

	def plot(self):
		'''plot the heatmap based on the given value
		'''
		intensity = self.get_intensity()
		#here's our data to plot, all normal Python lists
		x = range(-64,64) # x, y range from -64 to +63
		y = range(-64,64)

		#setup the 2D grid with Numpy
		x, y = np.meshgrid(x, y)

		#convert intensity (list of lists) to a numpy array for plotting
		intensity = np.array(intensity)

		#now just plug the data into pcolormesh, it's that easy!
		plt.pcolormesh(x, y, intensity)
		plt.colorbar() #need a colorbar to show the intensity scale
		plt.show() #boom

# dummy data for testing 
if __name__ == "__main__": # only will be excuted if testing the current module, if this moduel is imported from somewhere else if code below won't be excuted

	distance = [50, 60, 70] # distance is the size of the bounding box.
	distance_weight = 1
	position = [-25, -15, 10] # position is the distance to the center line
	position_weight = 1
	age = [10, 10, 10]
	age_weight = 1
	data = [distance, distance_weight, position, position_weight, age, age_weight]

	heat_mp = Heatmap(data)
	heat_mp.plot()
