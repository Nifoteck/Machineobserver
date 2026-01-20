class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, state, from_):
        print("Observer update method not implemented.")


class Employee(Observer):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role
    
    def update(self, state, from_):
        print(f"Employee: {self.name}, Role: {self.role}, Machine: {from_.name}, State: {state}")

class Subject:
    def __init__(self):
        self.state = None
        self.observers = []
    
    def setState(self, my_state):
        self.state = my_state
    
    def attach(self, observer):
        self.observers.append(observer)

    def notifyallobservers(self):
        for observer in self.observers:
            observer.update(self.state, self)


class Machine(Subject):
    def __init__(self, name):
        super().__init__()
        self.name = name


if __name__ == "__main__":

    fuji = Machine("Fuji")
    nxt = Machine("NXT")
    juki = Machine("JUKI")


    jus = Employee("Justina", "Operator")
    rob = Employee("Robert", "Supervisor")
    ben = Employee("Benjamin", "Technician")
    med = Employee("Medusa", "Technician")
    mik = Employee("Mike", "Operator")
    
    fuji.attach(jus)
    fuji.attach(rob)
    nxt.attach(rob)
    juki.attach(mik)
    nxt.attach(ben)
    juki.attach(rob)

    juki.setState("idle")
    juki.notifyallobservers()

    nxt.setState("running")
    nxt.notifyallobservers()

    fuji.setState("operational")
    fuji.notifyallobservers()

    juki.setState("operational")
    juki.notifyallobservers()
