import csv

class task():
    def __init__(self,name, description="" ,priority=None):
        self.name = name
        self.description = description
        self.priority = priority

class to_do_list():
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)
        self.save_to_csv()

    def remove_task(self,task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                self.save_to_csv()
                print("Task removed successfully!")
                return
        print("Task not found!")
        
    def show_tasks(self):
        for task in self.tasks:
            print(task.name , task.description , task.priority)

    def save_to_csv(self):
        header = ["name","description","priority"]
        with open("to_do.csv","w") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for task in self.tasks:
                writer.writerow([
                    task.name,
                    task.description,
                    task.priority
                ])

    def load_from_csv(self):
        try:
            with open("to_do.csv","r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    new_task=task(
                        row["name"],
                        row["description"],
                        row["priority"]
                    )

                    self.tasks.append(new_task)

        except FileNotFoundError:
            pass


my_works = to_do_list()
my_works.load_from_csv()

while True:
    user_choice = input(
        "Welcome to your To-Do List!\n"
        "1. Add task\n"
        "2. Remove task\n"
        "3. Show tasks\n"
        "4. Exit\n"
        "Your choice: "
    )

    if user_choice == "1":
        tasks_name = input("Name of the task: ")
        tasks_description = input("Description (optional): ")
        tasks_priority = input("Priority (optional): ")

        new_task = task(
            tasks_name,
            tasks_description,
            tasks_priority
        )

        my_works.add_task(new_task)

        print("Task added successfully!")

    elif user_choice == "2":
        task_name = input("enter the name of the task to remove:")
        my_works.remove_task(task_name)
    
    elif user_choice == "3":
        my_works.show_tasks()

    elif user_choice == "4":
        break

    else:
        print("Invalid choice!")