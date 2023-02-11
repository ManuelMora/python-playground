import json


class ActionsController:
    def __init__(self) -> None:
        self.user_actions = []

    def setUserActions(self, user_actions_json):
        self.user_actions = json.loads(user_actions_json)

    def isEmpty(self) -> bool:
        return True if len(self.user_actions) == 0 else False

    def length(self) -> int:
        return len(self.user_actions)

    def addAction(self, user_action_json) -> None:
        user_action = json.loads(user_action_json)
        self.user_actions.append(user_action)

    def takeAction(self) -> dict:
        return self.user_actions.pop()

    def getAllActions(self) -> list:
        return self.user_actions

    def getAllActionsStr(self) -> str:
        return json.dumps(self.user_actions)


ActionsController.__doc__ = "Class that helps to store and manage the actions a user does in the system"


user_actions_json = '[{"last_action":"1","last_response":"a"},{"last_action":"2","last_response":"b"},{"last_action":"3","last_response":"c"},{"last_action":"4","last_response":"d"}]'

action_controler = ActionsController()
action_controler.setUserActions(user_actions_json)
print(f"Current Actions = {action_controler.getAllActionsStr()}")

action_controler.addAction('{"last_action":"N","last_response":"New Action"}')
print(f"Current Actions = {action_controler.getAllActionsStr()}")

last_action = action_controler.takeAction()
print(f"Last Action = {json.dumps(last_action)}")
print(f"Current Actions = {action_controler.getAllActionsStr()}")
