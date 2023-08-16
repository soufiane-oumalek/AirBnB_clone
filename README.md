<h1 align="center">HBNB CLONE PROJECT</h1>

![MasterHead](https://cloudfront-eu-central-1.images.arcpublishing.com/le360/CCUVXYGTZBGBJDYZ47UIENUC54.jpg)
<h2 align="center">Hi 👋, We are Omar ID HMAID and Soufiane OUMALEK</h2>
<h3 align="center">And this is our AirBnB project</h3>
<p align="center" style{font-famly: geneva; }>
HolbertonBnB is a comprehensive web application that emulates AirBnB's functionality by seamlessly integrating database storage, a robust back-end API, and an intuitive front-end interface.<br>
As of now, the project primarily focuses on the development of the back-end console component.
</p>

<h3 align="left">To start the console :</h3>

__Run__: *./console.py*

__How to use it__
- **create**: Craft new instances of specified classes.
- **destroy**: Obliterate objects based on class name and ID.
- **all**: Visualize representations of all objects or specific classes.
- **update**: Elevate object attributes to new heights.
- **Quit**: Gracefully exit the program.
- **C-d**: Swiftly bid farewell.

__Example__
- *the prompt :* `(hbnb) `
- **create**: `create BaseModel`
- **destroy**: `destroy BaseModel 1234-1234-1234`
- **show**: `show BaseModel 1234-1234-1234`
- **all**: `all BaseModel or all`
- **update**: `<class name> <id> <attribute name> "<attribute value>"`
- **Quit**: `quit`
- **C-d**: `Ctrl D`
 

Interactive mode 
  
 ``` 
 $ ./console.py 
 (hbnb) help 
  
 Documented commands (type help <topic>): 
 ======================================== 
 EOF  help  quit 
  
 (hbnb)  
 (hbnb)  
 (hbnb) quit 
 $ 
 ``` 
 Non Interactive mode 
 ``` 
 $ echo "help" | ./console.py 
 (hbnb) 
  
 Documented commands (type help <topic>): 
 ======================================== 
 EOF  help  quit 
 (hbnb)  
 $ 
 $ cat test_help 
 help 
 $ 
 $ cat test_help | ./console.py 
 (hbnb) 
  
 Documented commands (type help <topic>): 
 ======================================== 
 EOF  help  quit 
 (hbnb)  
 $ 
 ``` 
  
 ## ``you can use it:`` 
  
 * Start the console in interactive mode: 
  
 ```bash 
 $ ./console.py 
 (hbnb) 
 ``` 
  
 * Use help to see the available commands: 
  
 ```bash 
 (hbnb) help 
  
 Documented commands (type help <topic>): 
 ======================================== 
 EOF  all  count  create  destroy  help  quit  show  update 
  
 (hbnb) 
 ``` 
  
 * Quit the console: 
  
 ```bash 
 (hbnb) quit 
 $ 
 ``` 
  
 * create 
  
 > *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.* 
  
 ```bash 
 (hbnb) create BaseModel 
 57262839-51d7-4a9a-93e2-35ed8e91d823 
 $ 
 ``` 
  
 * show  
  
 > *Deletes an instance of a given class with a given ID.* 
 > *Update the file.json* 
  
 ```bash 
 (hbnb) show BaseModel 57262839-51d7-4a9a-93e2-35ed8e91d823 
 [BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)} 
 (hbnb) 
 (hbhb) 
 ``` 
  
 * all 
  
 > *Prints all string representation of all instances of a given class.* 
 > *If no class is passed, all classes are printed.* 
  
 ```bash 
 (hbnb) all 
 [BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)} 
 (hbnb) all BaseModel 
 [BaseModel] (57262839-51d7-4a9a-93e2-35ed8e91d823) {'id': '57262839-51d7-4a9a-93e2-35ed8e91d823', 'created_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412265), 'updated_at': datetime.datetime(2023, 8, 13, 14, 19, 19, 412357)} 
 ``` 
 * destroy 
  
 >*Deletes an instance of a given class with a given ID.* 
 >*Update the file.json* 
  
 ```bash 
 (hbnb) destroy 
 ** class name missing ** 
 (hbnb) destroy BaseModel 
 ** instance id missing ** 
 (hbnb) destroy BaseModel 57262839-51d7-4a9a-93e2-35ed8e91d823 
 (hbnb) all 
 [] 
 ``` 
  
 * count  
  
 > *Prints the number of instances of a given class.* 
  
 ```bash 
 (hbnb) create User 
 ce5f7ac5-4b2e-4c90-933d-6c78e69ab1c7 
 (hbnb) create User 
 dd697519-4ac9-42e0-80e2-fa7b3ac61193 
 (hbnb) create User 
 52c4036b-f018-49d0-8d93-d7a2d56bcdad 
 (hbnb) count User 
 3 
 ``` 
  
 ## ``how to test`` 
  
 * unittest module 
 * File extension ``` .py ``` 
 * Files and folders star with ```test_``` 
 * Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py``` 
 * Execution command: ```python3 -m unittest discover tests``` 
 * or: ```python3 -m unittest tests/test_models/test_base.py``` 
  
 ### run TEST interactive mode 
  
 ```bash 
 echo "python3 -m unittest discover tests" | bash 
 ``` 
  
 ### run TEST non-interactive mode 
  
 To run the tests in non-interactive mode, and discover all the test, you can use the command: 
  
 ```bash 
 python3 -m unittest discover tests 
 ```