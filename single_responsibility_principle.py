# To-do List Class
# - create task
# - read task
# - update task
# - delete task

class Todolist:
    def __init__(self):
        self.todo_list = []
    @property
    def length(self):
        return len(self.todo_list)
    @property
    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False
    @property
    def get_list(self):
        return self.todo_list
    
class TodolistCreator:
    @staticmethod
    def add_todo(todolist: Todolist, todo: str):
        todolist.get_list.append(todo)

class TodolistPresenter:
    @staticmethod
    def display_todolist(todolist: Todolist):
        if todolist.is_empty:
            print("To-do List is empty...")
        for num, todo in enumerate(todolist.get_list):
            print(f"{num+1}. {todo}")

class TodolistRemover:
    @staticmethod
    def remove_task(todolist: Todolist, todo_index: int):
        try:
            todolist.get_list.remove(todo_index)
        except ValueError:
            pass
    @staticmethod
    def remove_all_tasks(todolist: Todolist):
        todolist.get_list.clear()

class TodolistUpdater(Todolist):
    @staticmethod
    def update_task(todolist: Todolist, todo_index: str, new_todo: str):
        try:
            todolist.get_list[todo_index] = new_todo
        except ValueError:
            pass


todolist = Todolist()

TodolistCreator.add_todo(todolist, "Eat")
TodolistCreator.add_todo(todolist, "Sleep")
TodolistCreator.add_todo(todolist, "Code")

TodolistPresenter.display_todolist(todolist)

TodolistRemover.remove_all_tasks(todolist)

TodolistPresenter.display_todolist(todolist)