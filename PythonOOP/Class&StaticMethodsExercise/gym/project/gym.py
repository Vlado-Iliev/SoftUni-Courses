from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = list()
        self.trainers = list()
        self.equipment = list()
        self.plans = list()
        self.subscriptions = list()

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ''
        for sub in self.subscriptions:
            if sub.id == subscription_id:
                result += repr(sub) + '\n'
                for customer in self.customers:
                    if customer.id == sub.customer_id:
                        result += repr(customer) + '\n'

                for trainer in self.trainers:
                    if trainer.id == sub.trainer_id:
                        result += repr(trainer) + '\n'

                for plan in self.plans:
                    if plan.id == sub.exercise_id:
                        for equipment in self.equipment:
                            if equipment.id == plan.equipment_id:
                                result += repr(equipment) + '\n'
                        result += repr(plan)

        return result
