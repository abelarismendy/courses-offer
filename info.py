import json
from collections import defaultdict
def get_info(filename):
    with open(filename) as f:
        return json.load(f)

def proccess_schedules(info):
    for course in info:
        for nrc in info[course]:
            info[course][nrc]['schedule'] = process_schedule(info[course][nrc]['schedule'])
    return info

def process_schedule(schedule):
    result = defaultdict(list)
    for entry in schedule:
        days = entry['days'].split()
        for day in days:
            result[day].append(entry['time'])
    # print(result)
    return dict(result)

if __name__ == '__main__':
    filename = 'prueba'
    route = 'output/' + filename + '.json'
    info = get_info(route)
    info = proccess_schedules(info)
    course_list = list(info.keys())