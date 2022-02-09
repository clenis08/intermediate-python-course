from unicodedata import name
from datos import DATA

def main():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == 'python']
    all_python_devs_fun = list(filter(lambda worker:worker["language"] == 'python',DATA))
    all_python_devs_fun = list(map(lambda worker: worker["name"], all_python_devs_fun))

    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == 'Platzi']
    all_platzi_work_fun = list(filter(lambda worker:worker["organization"] == 'Platzi',DATA))
    all_platzi_work_fun = list(map(lambda worker: worker["name"], all_platzi_work_fun))

    adults_list = [worker["name"] for worker in DATA if worker['age'] > 18]
    adults = list(filter(lambda worker: worker['age'] > 18, DATA ))
    adults = list(map(lambda worker: worker['name'], adults))
    
    old_adults_list = [{**worker, **{"old": worker["age"] > 70}} for worker in DATA  ]
    old_adults=list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))

    print(old_adults_list )
    print(old_adults)
    
    # for worker in adults:
    #     print(worker)

if __name__ == '__main__':
    main()