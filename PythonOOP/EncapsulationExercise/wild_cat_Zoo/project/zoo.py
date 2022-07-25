from project import Cheetah, Vet
from project.animal import Animal
from project.caretaker import Caretaker
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.worker import Worker


class Zoo:
    def __init__(self,name,budget,animal_capacity,workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self,animal:Animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__. __name__} added to the zoo"

    def hire_worker(self,worker:Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self,worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_for_salaries = sum([w.salary for w in self.workers])
        if total_for_salaries >self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget-= total_for_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_for_tendering = sum([a.money_for_care for a in self.animals])
        if self.__budget < total_for_tendering:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_for_tendering
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self,amount):
        self.__budget+= amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals' + '\n'

        lions = [repr(a) for a in self.animals if isinstance(a,Lion)]
        result += f'----- {len(lions)} Lions:\n' + '\n'.join(lions) + "\n"

        tigers = [repr(a) for a in self.animals if isinstance(a,Tiger)]
        result += f'----- {len(tigers)} Tigers:\n' + '\n'.join(tigers) + "\n"

        cheetah = [repr(a) for a in self.animals if isinstance(a,Cheetah)]
        result += f'----- {len(cheetah)} Cheetahs:\n' + '\n'.join(cheetah)

        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers' + '\n'

        keepers = [repr(a) for a in self.workers if isinstance(a,Keeper)]
        result += f'----- {len(keepers)} Keepers:\n' + '\n'.join(keepers) + "\n"

        caretakers= [repr(a) for a in self.workers if isinstance(a,Caretaker)]
        result += f'----- {len(caretakers)} Caretakers:\n' + '\n'.join(caretakers) + "\n"

        vets = [repr(a) for a in self.workers if isinstance(a,Vet)]
        result += f'----- {len(vets)} Vets:\n' + '\n'.join(vets)

        return result
