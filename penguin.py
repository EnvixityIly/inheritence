class Bird:
    def __init__(self):
        print("Bird is ready")
    def WiT(self):
        print("Bird")
    def swim(self):
        print("Swim faster")
class Penguin(Bird):

    def __init__(self):

        super().__init__()
        print("Penguin is ready")
    def WiT(self):
        print("Penguin")
    def run(self):
        print("Run faster")
        
pegmedaddy = Penguin()
pegmedaddy.WiT()
pegmedaddy.swim()
pegmedaddy.run()