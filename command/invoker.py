class Invoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        self.history.append(command)
        command.execute()

    def undo_last_command(self):
        if self.history:
            command_to_undo = self.history.pop()
            command_to_undo.undo()
            print("Undo successful.")
        else:
            print("Nothing to undo.")