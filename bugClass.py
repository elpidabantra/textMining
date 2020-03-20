class DetectBugs:
	def __init__(self, landscape_file, bug_file): 
		self.landscape_file = landscape_file
		self.bug_file = bug_file

		landscape = []
		bug = []

		with open(bug_file) as f:
			content = f.readlines()
		bug = [x.strip("\n") for x in content] 


		with open(landscape_file) as f2:
			content2 = f2.readlines()
		landscape = [x.strip("\n") for x in content2] 

		self.landscape_file = landscape
		self.bug_file =  bug


	def cal_b_ls_matrix(self):
		bug = self.bug_file
		landscape = self.landscape_file

		if bug == []:
			return 0

		if landscape == []:
			return 0

		if len(bug)>len(landscape):
			return 0



		"""
		QUICK FIX for non ascii chars
		
		bug2 = []
		landscape2 = []
		
		for i in bug:
			if '\xc2\xb1' in i:
				i = i.replace('\xc2\xb1',"?")
			if '\xc2\xa7' in i:
				i = i.replace('\xc2\xa7',"]")
			bug2.append(i)
		bug = bug2 


		for i in landscape:
			if '\xc2\xb1' in i:
				i = i.replace('\xc2\xb1',"?")
			if '\xc2\xa7' in i:
				i = i.replace('\xc2\xa7',"]")
			landscape2.append(i)
		landscape = landscape2 

		"""




		bug_matrix = []
		bugd = {}
		c = 1
		for l in bug:
			for elem in l:
				if elem in bugd:
					continue
				if elem == " ":
					bugd[elem] = 0
				else:
					bugd[elem] = c
				c = c + 1
		for z in range(len(bug)):
			ll = []
			for s in bug[z]:
				ll.append(bugd[s])
			bug_matrix.append(ll)



		ls_matrix = []


		for l in landscape:
			for elem in l:
				if elem in bugd:
					continue
				else:
					bugd[elem] = c
					c = c + 1
		for z in range(len(landscape)):
			ll = []
			for s in landscape[z]:
				ll.append(bugd[s])
			ls_matrix.append(ll)

		self.landscape_file = ls_matrix
		self.bug_file =  bug_matrix

		if len(max(self.bug_file))>len(max(self.landscape_file)):
			return 0



	def return_num_of_bugs_in_line(self, bug_line, landscape_line):
		if bug_line == []:
			return 0
		bug_seq = []
		for di in bug_line:
			bug_seq.append(di)
		line_counter = 0
		bug_elem1 = bug_line[0]
		bug_elemlast = bug_line[-1]
		if len(bug_seq) == 1:													   # for one char bug
			if bug_line[0] == 0:
				for ll in landscape_line:
					line_counter = line_counter + 1
			else:
				for ll in landscape_line:
					if ll == bug_line[0]:
						line_counter = line_counter + 1
		else: 
			start1 = 0															  # for more than one chars bug
			for landscape_elem in landscape_line:
				if bug_seq[start1] == 0:
					landscape_elem = 0
				if bug_seq[start1] == landscape_elem:
					if start1 == len(bug_seq)-1:
						line_counter = line_counter + 1
						start1 = 0
					else:
						if bug_seq[start1] == landscape_elem:
							start1 = start1 + 1
				else:
					start1 = 0
		return line_counter


	def all_the_bug_in_landscape_line(self, bug_seq, landscape_line):				# find all bug_seq in landscape_line
		
		if bug_seq == []:
			return []
		if landscape_line == []:
			return []
		if len(bug_seq)>len(landscape_line):
			return []

		bug_line_list = []
		ro = -1
		start1 = 0 
		for landscape_elem in landscape_line:
			ro = ro + 1
			if bug_seq[start1] == 0:
				if start1 == len(bug_seq)-1:
					wholebug = landscape_line[ro-(len(bug_seq)-1):ro+1]
					bug_line_list.append(wholebug)
					start1 = 0
				else:
					start1 = start1 + 1

			else:
				if bug_seq[start1] == landscape_elem:
					if start1 == len(bug_seq)-1:
						wholebug = landscape_line[ro-(len(bug_seq)-1):ro+1]
						bug_line_list.append(wholebug)
						start1 = 0
					else:
						if bug_seq[start1] == landscape_elem:
							start1 = start1 + 1
				else:
					start1 == 0
		return bug_line_list


	def return_start_list(self, landscape_line, bug_0):		# we take all the positions in the landscape line where bug_0 starts
		if bug_0 == []:
			return []
		if landscape_line == []:
			return []
		if len(bug_0)>len(landscape_line):
			return []
		rr = self.all_the_bug_in_landscape_line(bug_0, landscape_line)
		splits = []
		start_list = []
		start = 0
		v = 0
		s = ""
		for i in landscape_line:
			s = s+str(i)
		landscape_line = s
		
		for bu in rr:

			s = ""
			for i in bu:
				s = s+str(i)
			bu = s

			landscape_line = landscape_line.replace(bu,"sol")
		splits = landscape_line.split("sol")

		for spl in splits:
			start = start + len(spl) + v
			v = len(bug_0)
			start_list.append(start)
		del start_list[-1] 
		
		return start_list											 
					
###########################################################################################

	def counter(self):
		landscape = self.landscape_file
		bug = self.bug_file
		
		# check if the bug and the landscape have length greater than 0.
		if not bug:
			return 0
		if not landscape:
			return 0
		if bug == [""]:
			return 0
		if landscape == [""]:
			return 0



		# check if the bug is larger than the landscape
		l_len = len(landscape)
		b_len = len(bug) 
		l_wid = len(max(landscape, key=len))
		b_wid = len(max(bug, key=len))
		if l_len < b_len:
			return 0
		if l_wid < b_wid:
			return 0
		count = 0

		if b_len == 1:		
			for l_line in range(0, l_len - (b_len - 1)):
				line_counter = self.return_num_of_bugs_in_line(bug[0], landscape[l_line])
				count = count + line_counter
		else:																			   # more than one lines bug
			bug_len = len(bug)
			for l_line in range(0, l_len - (bug_len -1) ):																	   
				bugs_in_line = []
				bugs_in_line = self.return_start_list(landscape[l_line], bug[0])
				if len(bugs_in_line) > 0:
					for b_starts in bugs_in_line:										   #search for each bug0 if the count is increased
						for bugnext in range(1,bug_len):
							start_list = []
							start_list = self.return_start_list(landscape[l_line + bugnext], bug[bugnext])
							if not start_list:
								continue
							if b_starts not in start_list:
								continue
							if bugnext == bug_len-1:							  
								count = count + 1
		return count

	def main(self):
		self.cal_b_ls_matrix()
		return self.counter()
		


bugs = DetectBugs("landscape.txt", "bug.txt").main()
print(bugs)




