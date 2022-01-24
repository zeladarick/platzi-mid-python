DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():

    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print("All python developers: ", all_python_devs, "\n")
    
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print("All Platzi workers: ", all_platzi_workers, "\n")

    all_adults = list(
        filter(lambda worker : worker["age"] > 18, DATA)
    )
    all_adults_names = list(
        map(lambda worker : worker["name"], all_adults)
    )
    print("All adults: ", all_adults_names, "\n")

    old_people = [
        {
            'name': worker["name"],
            'age': worker["age"],
            'organization': worker["organization"],
            'position': worker["position"],
            'language': worker["language"],
            'old' : worker["age"] > 70
        }
        for worker in DATA
    ]

    old_people = list(
        map(lambda worker: { **worker, **{'old' : worker["age"] > 70}}, DATA)
    )

    #ONLY SUPPORTED IN PYTHON 3.9!!! 
    # old_people = list(
    #     map(lambda worker : worker | {"old" : worker["age"] > 70}, DATA)
    # )

    print("Old People: ", old_people, "\n");


    #Challenges

    #all_python_devs and all_platzi_workers with filter and map
    all_python_devs_challenge = list(
        filter(lambda worker : worker["language"] == "python", DATA)
    )
    all_python_devs_challenge = list (
        map(lambda worker : worker["name"], all_python_devs_challenge)
    )

    all_platzi_workers_challenge = list(
        filter(lambda worker : worker["organization"] == "Platzi", DATA)
    )
    all_platzi_workers_challenge = list (
        map(lambda worker : worker["name"], all_platzi_workers_challenge)
    )

    #old_people and adults with list comprenhensions
    old_people_challenge = [{ **worker, **{"old" : worker["age"] > 70 }} for worker in DATA ]
    all_adults_challenge = [ worker for worker in DATA if worker["age"] > 18]


    #Autograder
    print("All python devs test: ", all_python_devs_challenge == all_python_devs)
    print("All Platzi workers test: ", all_platzi_workers_challenge == all_platzi_workers)
    print("Old people test: ", old_people_challenge == old_people)
    print("Adults test: ", all_adults_challenge == all_adults)


if __name__ == '__main__':
    run()