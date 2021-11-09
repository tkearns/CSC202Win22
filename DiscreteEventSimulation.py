from BasicDS import Queue
from BasicDS import PriorityQueue
import random

class BankSimulation:
    tellers = []
    customer_queue = Queue()
    event_queue = PriorityQueue()
# keeping track of simulation statistics
    total_customers = 0
    total_time = 0
# parameters for time between arrivals and service time distributions
    interarrival = 1   # average time between customers
    avg_service_time = 5
# will want a call like random.randrange(1,21)

    def __init__(self,num_tellers):
        tellers = [None]*num_tellers

    def run(self, start_time, end_time):
        current_time = start_time;
        while (event_queue.size() > 0 and current_time <= end_time):  # event loop
            curr_event = eventQueue.remove()
            currentTime = curr_event.get_time()
            event.process()
        display_summary()

    def display_summary():
        print()

    def add_to_teller(self, teller, cust):
        tellers[teller] = cust
        add_event(Departure(current_time))

    def add_cust(self, c):  #checks to see if teller available, if not adds to waiting queue
        added_to_teller = False
        for t in tellers:
            if tellers[t] is None:
                add_to_teller(t, c)
                added_to_teller = True
                break
        if not added_to_teller:
            customer_queue.appemd(c)
        add_event(Arrival(current_time + ramdom.exponential))

class Customer:
    arrival_time
    def __init__ (self, arr_time):
        self.arrival_time= arr_time

    def get_arrival_time(self):
        return self.arrival_time

class Event:
    current_time = 0
    def __init__(self, event_time):
        time = event_time
    def process(self):
        pass
    def get_time(self):
        return current_time
    def __lt__(self, other):
        isinstance(object, Event)
        if (self.time < other.time):
            return True

class Departure(Event):
    def __init__(self, time, teller):
        Event.__init__(self, time)
        self.teller = teller

    def process(self, sim):
        c = self.teller
        sim.tellers[c] = None
        total_customers
        total_time = total_time + current_time - c.get_arrival_time()
        if customer_queue.size() > 0:
            add_to_teller(self, c, customer_queue.dequeue())



class Arrival(Event):
    def __init__(self):
        Event.__init__(self, time)

    def process(self, sim):
        now = sim.get_current_time()
        bank= sim
        c = Customer(sim.get_current_time)
        bank.add(c)


start_time = 9 * 60             # 9 a.m.
end_time = 17 * 60              # 5 p.m.
n_tellers = 5

# Create a simulation
sim = BankSimulation(n_tellers)
# initialize the event queue with an arrival
sim.addEvent(Arrival())
run the simulation
sim.run(start_time, end_time)
