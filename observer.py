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

class Dashboard(Observer):
    '''
    Sends machine state updates to a web dashboard via WebSocket.
    '''
    def __init__(self, name, websocket_url):
        super().__init__(name)
        self.websocket_url = websocket_url
    
    def update(self, state, from_):
        import json
        import asyncio
        import websockets
        
        message = json.dumps({
            "machine_name": from_.name,
            "state": state,
            "dashboard": self.name
        })
        
        async def send_message():
            try:
                async with websockets.connect(self.websocket_url) as websocket:
                    await websocket.send(message)
                    print(f"Dashboard '{self.name}': Sent update for {from_.name} - {state}")
            except Exception as e:
                print(f"Dashboard '{self.name}': Failed to send update - {e}")
        
        asyncio.run(send_message())

if __name__ == "__main__":
   
    observer = Dashboard("Main Dashboard", "ws://localhost:8765")
    fuji = Machine("Fuji")
    nxt = Machine("NXT")
    juki = Machine("JUKI")

    juki.attach(observer)
    fuji.attach(observer)
    nxt.attach(observer)
    
    juki.setState("idle")
    juki.notifyallobservers()

    nxt.setState("running")
    nxt.notifyallobservers()

    fuji.setState("operational")
    fuji.notifyallobservers()

    juki.setState("operational")
    juki.notifyallobservers()

    fuji.setState("idle")
    fuji.notifyallobservers()