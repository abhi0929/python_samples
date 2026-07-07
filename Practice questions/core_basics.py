def say_hello():
    print("Welcome to python")
say_hello()                         #1st question

def add(a,b):
    return a+b
print(add(3,4))                 #2nd question

def fun():
    print("hello world")            #3rd question

def area_of_rectangle(length,width):
    return length*width
print(area_of_rectangle(6,4))       #4th question

def fun(a,b,c):
    return a+b+c
print(fun(1,2,3))

def describe_animal(animal,name):
    return (animal,name)
print(describe_animal("my"'dog',"named" 'bark'))

def power(base, exponent):
    return base ** exponent
print(power(2, 3))

def name(first,middle, last):
    return first+middle+last
print(name("abhi","ram","patel"))

def intro(name,city,hobby):
    print(f" iam  {name} from {city} and i like {hobby}")
intro("abhiram", "mancherial", "online games")

def subtract(a, b):
    return a - b
print(subtract(3, 10))

def bio(first_name, last_name,age):
    print("My name is ",first_name)
    print("My surname is ",last_name)
    print("My age is ",age)
print(bio("abhiram","akula","21"))

def send_email(to, subject, content):
    print("Dear",to)
    print("Subject:",subject)
    print("Content:",content)
send_email("hr", "job application details ", "requesting for the response ")

def ticket(alice, delhi, mumbai):
    print("name", alice)
    print("from", delhi)
    print("to", mumbai)
ticket("alice", "delhi", "mumbai")

def power(base, exponent=2):
    return base ^ exponent
print(power(4,6))

