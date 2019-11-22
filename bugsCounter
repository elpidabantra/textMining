class DetectBugs:
    def __init__(self, landscape_file, bug_file): 
        self.landscape_file = landscape_file
        self.bug_file = bug_file

        landscape = []
        bug = []

        with open(landscape_file) as f:
            content = f.readlines()
        landscape = [x.strip("\n") for x in content] 
        with open(bug_file) as f:
            content = f.readlines()
        bug = [x.strip("\n") for x in content] 

        self.landscape_file = landscape
        self.bug_file =  bug


    def return_num_of_bugs_in_line(self, bug_line, landscape_line):
        bug_seq = []
        for di in bug_line:
            bug_seq.append(di)
        line_counter = 0
        bug_elem1 = bug_line[0]
        bug_elemlast = bug_line[-1]
        if len(bug_seq) == 1:                                                       # for one char bug
            if bug_line[0] == " ":
                for ll in landscape_line:
                    line_counter = line_counter + 1
            else:
                for ll in landscape_line:
                    if ll == bug_line[0]:
                        line_counter = line_counter + 1
        else: 
            start1 = 0                                                              # for more than one chars bug
            for landscape_elem in landscape_line:
                if bug_seq[start1] == " ":
                    landscape_elem = " "
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

    def all_the_bug_in_landscape_line(self, bug_seq, landscape_line):                # find all bug_seq in landscape_line
        bug_line_list = []
        ro = -1
        start1 = 0 
        for landscape_elem in landscape_line:
            ro = ro + 1
            if bug_seq[start1] == " ":
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


    def return_start_list(self, landscape_line, bug_0):                              # we take all the positions in the landscape line where bug_0 starts
        splits = []
        start_list = []
        bug_seq_0 = []
        start = 0
        v = 0
        for di in bug_0:
            bug_seq_0.append(di)
        for bu in self.all_the_bug_in_landscape_line(bug_seq_0, landscape_line):
            landscape_line = landscape_line.replace(bu,"sol")
        splits = landscape_line.split("sol")
        for spl in splits:
            start = start + len(spl) + v
            v = len(bug_0)
            start_list.append(start)
        del start_list[-1] 
        
        return start_list                                             
                    


    def counter(self):
        landscape = self.landscape_file
        bug = self.bug_file
        
        # check if the bug and the landscape have length greater than 0.
        if not bug:
            return "There are no bugs"
        if not landscape:
            return "There is no landscape"
        if bug == [""]:
            return "There are no bugs"
        if landscape == [""]:
            return "There is no landscape"

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
        if b_len == 1:                                                                      # one line bug
            for l_line in range(0, l_len - (b_len - 1)):
                line_counter = self.return_num_of_bugs_in_line(bug[0], landscape[l_line])
                count = count + line_counter
        else:                                                                               # more than one lines bug
            bug_len = len(bug)
            for l_line in range(0, l_len - (bug_len -1) ):                                                                       
                bugs_in_line = []
                bugs_in_line = self.return_start_list(landscape[l_line], bug[0])
                if len(bugs_in_line) > 0:
                    for b_starts in bugs_in_line:                                           #search for each bug0 if the count is increased
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

bugs = DetectBugs("landscape.txt", "bug.txt")
print(bugs.counter())



