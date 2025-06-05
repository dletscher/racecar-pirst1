import random

class Agent:
	def chooseAction(self, observations, possibleActions):
		lidar = observations['lidar']
		velocity = observations['velocity']

		directions = ['left', 'left', 'straight', 'right', 'right']
		lidar_max = max(lidar)
		best_index = lidar.index(lidar_max)
		steer = directions[best_index]

		distance = lidar[2]

		if distance > 3 and velocity < 0.8:
			throttle = 'accelerate'
		elif distance < 1.5 and velocity > 0.5:
			throttle = 'brake'
		else:
			throttle = 'cost'

		return (steer, throttle)	