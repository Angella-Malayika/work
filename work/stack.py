print("Nakanwagi Angella \n")
print("Reg.no:2024-B071-21804 \n")
class UndoRedo:
    def __init__(self):
        self.undo_stack = []   # keeps all actions you do
        self.redo_stack = []   # keeps actions you have undone

    def do(self, action):
        # add a new action
        self.undo_stack.append(action)
        self.redo_stack = []   # clear redo stack after a new action
        print("Action done: " + action)

    def undo(self):
        # take back the last action
        if len(self.undo_stack) == 0:
            print("Nothing to undo.")
        else:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)
            print("Undo: " + action)

    def redo(self):
        # repeat the last undone action
        if len(self.redo_stack) == 0:
            print("Nothing to redo.")
        else:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
            print("Redo: " + action)

    def show_history(self):
        print("Undo stack:", self.undo_stack)
        print("Redo stack:", self.redo_stack)


# print 
editor = UndoRedo()

editor.do("Hello Malayika")
editor.do("Say Hey to everyone !!!")
editor.undo()          
editor.redo()          
editor.do("How is everyone here")   # redo stack is cleared after a new action
editor.show_history()
