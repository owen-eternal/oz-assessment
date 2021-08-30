# Sorting API

Endpoint: **http://somesorting.herokuapp.com/api/v1/bubble**

**Container Pull:** 
```bash
docker pull 040900507/offerzen-assessment
```

### Project Overview: Bubble sort API

This API is my implementation of a bubble sort algorithm using Python, Flask and SWaggerUI. Allows the user to send a post
request of an unsorted list of elements to the  */api/v1/bubble* endpoint and receive a list of sorted elements as a json response.

Upon success:

1. **201** | must return a json object of sourted array

An exception is thrown on the following conditions:

1. **401** Must not be empty | *cannot send an empty array.*
2. **401** Elements in list must be less then Max Length | *the number of elements exceeds the max length set on the server.*


### Project Achitecture

To build the project architecture, I used my own library called [mudbrick](https://pypi.org/project/mudbrick/).
It automatically builds a production ready flask application factory boilerplate. [github repo](https://github.com/owen-eternal/mudbrick)

1. autoscript/
    - workflow.yaml            
2. sorting/
    - __init__.py           
    - bubble_sort.py          
3. tests/
    - __init__.py
    - test_api.py              
    - test_bubble_sort.py
4. webapp/
    - api/               
        - __init__.py
        - routes.py
    - swagger_docs/               
        - config.py
        - docs.yml
    - __init__.py
    - settings.py
5. autorun.py
6. Procfile                    
7. README.md                   
8. requirements.txt            
9. setup.cfg                   
10. wsgi.py                    


### Local development

run the following script to envoke the development server: 

```bash
python autorun.py
```

If your **FLASK_ENV** is set to development - Tests set by the *workflow.yaml* module are performed first. Should any of the tests fail, the development server won't run. The **_RPA automation scritpt_** detects the flask enviroment and runs all the neccessary instructions set by the **_workflow.yaml module_**. It compares the instruction from the **_workflow.yaml module_** to a set of instructions defined in your **_enviroment variables_**, if instructions donot match: It stops executing the whole program. This is neccessary to protect the server from executing melicious commands.

**RPA automation script**

```python
def run_server(path, env):

    with open(path, 'r') as file:
        broke = False
        command_list = yaml.load(file, Loader=SafeLoader)[env]
        for command in command_list:
            if broke:
                break
            for run in command['run']:
                if run in app.config['ALLOWED_COMMANDS']:
                    print('\n')
                    process = subprocess.run(run, shell=True)
                    if process.returncode == 1:
                        broke = True
                        break
                else:
                    raise Exception('Invalid command')
    return broke
```

### Enviroment variables

The following enviroment variables need to be configured before running your application.
**NB** use the keys as is.

- #### Flask enviroment

Configures the enviroment to production/development.

```.env
FLASK_ENV=development
```

- #### Maximum length

Configures the maximum amount of elements allowed inside an array.

```.env
MAXIMUM_LENGTH=10_000
```

- #### Allowed commands

Protects your server from running malicious commands. 

```.env
PROD_COMMANDS = ['FLASK_APP=wsgi.py flask run']
DEV_COMMANDS=['flake8', 'coverage run -m unittest discover', 'coverage report', 'FLASK_APP=wsgi.py flask run']
```

### Overview: Bubble sort algorithm

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

The class adheres to the following contraint: 

1. Arrays of 10_000 elements are not allowed.
2. Must filter out all non integer values.
3. Must flatten any nested array before proceeding to the sort function.

```python
class BubbleSort():

    # filter for integers
    def __filter_list(self, array):
        filtered_list = []
        for item in array:
            if isinstance(item, int):
                filtered_list.append(item)
        return filtered_list

    # flatten list
    def __flatten_list(self, array):
        if len(array) == 0:
            return array
        if isinstance(array[0], list):
            return self.__flatten_list(array[0]) + self.__flatten_list(array[1:])
        return array[:1] + self.__flatten_list(array[1:])

    # bubble sort
    def bubble_sort(self, array: list, max_length: int):
        if len(array) > max_length:
            raise ValueError(f'Elements must be less then {max_length}')
        flat_list = self.__flatten_list(array)
        filtered_list = self.__filter_list(flat_list)
        n = len(filtered_list)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if filtered_list[j] > filtered_list[j + 1]:
                    filtered_list[j], filtered_list[j+1] = filtered_list[j+1], filtered_list[j]
        return filtered_list
```

### Overview Hosting

I used github action as my remote CI server to conduct the following workflows:

1. on push to my github master branch: 
    - build development enviroment.
    - install required dependencies.
    - run linter for code checks
    - run code coverage and produce a report
    - if all the above job passes, commit code to the master branch.

I used Heroku for hosting:

2. on pull by Heroku:
    - run build
    - test build
    - run linter
    - do code coverage
    - report
    - containerize
    - and run automatic deploys
