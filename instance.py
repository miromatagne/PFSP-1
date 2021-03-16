class Instance:

    def __init__(self):
        self.nb_jobs = 0
        self.nb_machines = 0
        self.processing_times_matrix = []
        self.due_dates = []
        self.priority = []

    def read_data_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                print("File " + filename + " is now open, start to read...")
                self.nb_jobs, self.nb_machines = tuple(
                    map(int, f.readline().split(" ")))
                print("Number of jobs : " + str(self.nb_jobs))
                print("Number of machines  : " + str(self.nb_machines))
                print("Start to read matrix...")
                for i in range(self.nb_jobs):
                    line = f.readline().strip().split(" ")
                    line = list(map(int, line))
                    self.processing_times_matrix.append(line[1::2])
                # print(self.processing_times_matrix)
                f.readline()
                for i in range(self.nb_jobs):
                    line = f.readline().split(" ")
                    self.due_dates.append(int(line[1]))
                    self.priority.append(int(line[-1]))
                # print(self.due_dates)
                # print(self.priority)
            return True
        except OSError as e:
            print("Error while opening" + filename)
            return False

    def compute_wct(self, sol):
        previous_machine_end_time = [0 for i in range(len(sol))]

        # First machine
        for j in range(len(sol)):
            job_number = sol[j]
            previous_machine_end_time[j] = previous_machine_end_time[j -
                                                                     1] + self.processing_times_matrix[job_number][0]
        # Following machines
        for m in range(1, self.nb_machines):
            previous_machine_end_time[0] += self.processing_times_matrix[sol[0]][m]
            previous_job_end_time = previous_machine_end_time[0]
            for j in range(1, len(sol)):
                job_number = sol[j]
                previous_machine_end_time[j] = max(
                    previous_job_end_time, previous_machine_end_time[j]) + self.processing_times_matrix[job_number][m]
                previous_job_end_time = previous_machine_end_time[j]
        wct = 0
        for j in range(len(sol)):
            wct += previous_machine_end_time[j] * self.priority[sol[j]]
        return wct

    def get_nb_jobs(self):
        return self.nb_jobs

    def get_weighed_sum(self):
        weights = {}
        for i in range(self.nb_jobs):
            total_processing_time = 0
            total_processing_time += sum(self.processing_times_matrix[i])
            weights[i] = total_processing_time * self.priority[i]
        sorted_weighed_sum = dict(
            sorted(weights.items(), key=lambda item: item[1]))
        return sorted_weighed_sum.keys()
