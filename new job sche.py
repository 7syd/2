def schedule_jobs_with_deadline(job_data, overall_deadline):
    sorted_jobs = sorted(job_data, key=lambda x: x[2], reverse=True)
    
    schedule = []
    max_profit = 0
    current_time = 0

    for job in sorted_jobs:
        job_id, job_completion_time, job_profit = job
        if current_time + job_completion_time <= overall_deadline:
            schedule.append(job_id)
            max_profit += job_profit
            current_time += job_completion_time

    return schedule, max_profit

if __name__ == "__main__":
    job_data = []
    n = int(input("Enter the number of jobs: "))

    for i in range(n):
        job_id = input("Enter Job ID: ")
        job_completion_time = int(input("Enter Job Completion Time: "))
        job_profit = int(input("Enter Job Profit: "))
        job_data.append((job_id, job_completion_time, job_profit))

    overall_deadline = int(input("Enter the overall deadline: "))

    schedule, max_profit = schedule_jobs_with_deadline(job_data, overall_deadline)

    print("Scheduled Jobs:", schedule)
    print("Maximum Profit:", max_profit)
