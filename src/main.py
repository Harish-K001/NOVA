from core.assistant import Assistant
from core.brain import Brain
from core.automation import Automation
from core.memory import Memory
from core.app_registry import Appregistry



def main():
    assistant = Assistant("NOVA", "0.1")

    brain = Brain()
    automation = Automation()
    memory = Memory()
    registry = Appregistry()
    

    assistant.greet()
    while True:

        message = input("You: ")

        action = brain.understand(message)


        if action["intent"] == "GREETING":
            assistant.greet()

        elif action["intent"] == "IDENTITY":
            assistant.introduce()

        elif action["intent"] == "SAVE_ALIAS":

            memory.save_alias(action["alias"],action["target"])
            print("NOVA: Got it! I'll remember that for sure.")

        elif action["intent"] == "OPEN_APP":
            target = action["target"]
            real_target = memory.get_alias(target)

            if real_target is  None:
                real_target = target

            launch_command = registry.get_command(real_target)
            print(f"Real Target: {real_target}")
            print(f"Launch Command: {launch_command}")

            if launch_command is not None:
                    automation.open_app(launch_command)
                
            else:
                    print("I dont know the given application!")
                

            
        elif action["intent"] == "LIST_APPS" :
            apps = registry.get_apps()
            for app in apps:
                 print(app)
        elif action["intent"] == "EXIT":
            print("NOVA: Goodbye!")
            break

        else:
            print("NOVA: I don't know how to do that yet.")


if __name__ == "__main__":
    main()  