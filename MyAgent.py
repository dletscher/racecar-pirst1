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

		if velocity == 0:
			throttle = 'accelerate'
		elif distance > 3 and velocity <= 0.1:
			throttle = 'accelerate'
		elif distance < 1.5 and velocity > 0.1:
			throttle = 'brake'
		else:
			throttle = 'coast'


		return (steer, throttle)	