class Brain:

    def understand(self, message):

        message = message.lower().strip()
        words = message.split()

        if len(words) == 3 and  words[0] == "call":

            target = words[1]
            alias = words[2]
            return {
                "intent" : "SAVE_ALIAS",
                "target" : target,
                "alias"  : alias
            }
        elif len(words) == 2 and words[0] == "open":  
            target = words[1]
            return{
                "intent"  : "OPEN_APP",
                "target"  : target
            }

        elif message in ["hello", "hi", "hey"]:
            return {
                "intent": "GREETING"
            }

        elif message == "who are you":
            return {
                "intent": "IDENTITY"
            }

        
        elif message in ["exit", "quit"]:
            return {
                "intent": "EXIT"
            }

        else:
            return {
                "intent": "UNKNOWN"
            }