import json
from collections import defaultdict, OrderedDict
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
    # order the dictionary by key (day) 'L', 'M', 'I', 'J', 'V', 'S', 'D' (not necessary contains all the keys)
    result = OrderedDict((k, result[k]) for k in 'L M I J V S D'.split())
    # DELETE THE EMPTY KEYS
    for key in list(result.keys()):
        if not result[key]:
            del result[key]
    result = dict(result)
    # print(result)
    return result

if __name__ == '__main__':
    filename = 'prueba'
    route = 'output/' + filename + '.json'
    info = get_info(route)
    info = proccess_schedules(info)
    course_list = list(info.keys())
    # write the processed info to a new file
    with open('output/' + filename + '_processed.json', 'w') as f:
        json.dump(info, f, indent=4)