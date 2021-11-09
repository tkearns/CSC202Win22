import numpy as np
import prioirityqueue from

class Server:

class Simulation
    def __init__ (self, numserv, arrrate, servtime, sim_length):
        self.numservers = numserv
        self.inter_arrrate = arrrate
        self.servicetime =servtime
        self.clock = 0
        self.sim_length = sim_length
        self.total_wait_time = 0
        event_queue = prioirityqueue()   # create empty event queue
        #etc

def gen_interarrival_time(arrrate):
    return np.random.exponential(1./arrrate)

def gen_service_time(servrate):
    return np.random.exponential(1.servrate)    # generates integer from 1..4


def event_handler():


def advance_time():



def handle_customer_event():


def handle_service_completion

def main(self):
        eventqueue = prioirityqueue()
        sim = Simulation()  :  # need structure for calling
        simrunning = True
        while simrunning:
            currevent = eventqueue.remove()
            if isinstance(currevent, "arrival")


