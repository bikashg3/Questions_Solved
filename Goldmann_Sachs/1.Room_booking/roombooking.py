Class Solution:
	def Hotel(self,arrive,depart,K):
		events = [(t,1) for t in arrive] + [(t,0) for t in depart]
		events = sorted(events)
		guests = 0
		
		for event in events:
			if event[1] == 1:
				guests += 1
			else:
				guests -=1
			if guests > K:
				return 0 # guests exceeds available rooms. Can't book
		return 1 # booking done
		
