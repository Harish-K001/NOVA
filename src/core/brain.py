class Brain:
    def normalize(self,message):
        message = message.lower().strip()
        cleaned_text = "".join(char for char in message if char.isalnum() or char.isspace())
        cleaned_text = " ".join(cleaned_text.split())
        return cleaned_text
    def detect_intent(self,message):
        word = message.split()
        question = ["who", "whom", "whose", "what", "which", "where", "when", "why", "how"]
        negation = ["dont", "no", "not", "never"]
        is_question = any(ch in word for ch in question)
        is_negation = any(ch in word for ch in negation)
        if is_question:
            if word[0] == "what" and "is" in word:
                return {"intent": "RETRIEVE"}
            else:
                return {"intent": "QUESTION"}

        elif is_negation and "open" in word:
            return {"intent": "NEGATION_OPEN_APP"}

        elif "open" in word:
            return {"intent": "OPEN_APP"}
        elif "call" in word and "as" in word : 
            return {"intent" : "SAVE_ALIAS"}
        elif "remember" in word and "is" in word :
            return{"intent" : "MEMORIZE"}

        else:
            return {"intent": "UNKNOWN"}
        
        
        
# ENTITY EXTRACTION - START!# 
    def extract_entities(self,message,intent):
        filler_words = ["the", "a", "an", "please", "app", "application", "for", "me","can", "my"]
        if intent == "OPEN_APP":
            words = message.lower().split()
            target_index = words.index("open")+1
            result = words[target_index:] 
            filtered = [ch for ch in result if ch not in filler_words]
            target = " ".join(filtered)
            return {"intent" : "OPEN_APP",
                    "target" : target
                    }
        elif intent == "SAVE_ALIAS":
            cleaned_words = message.lower().replace("call", "")
            words = [ch.strip() for ch in cleaned_words.split("as")]
            target = words[0]
            alias = words[1]
            return {
                "intent" : "SAVE_ALIAS",
                "target" : target,
                "alias" : alias 
            }
        elif intent == "MEMORIZE":
            cleaned_words = message.lower().replace("remember", "")
            words = [ch.strip() for ch in cleaned_words.split("is")]
            key = words[0]
            value = words[1]
            return {
                "intent" : "MEMORIZE",
                "key" : key,
                "value" : value 
            }
        elif intent == "RETRIEVE" : 
            cleaned_words = message.lower()
            parts = [part.strip() for part in cleaned_words.split("is")]
            key = parts[-1]
            return {
                "intent": "RETRIEVE",
                "key": key
            }


           

            
            
                

    def understand(self, message):
        user_message = self.normalize(message)
        action = self.detect_intent(user_message)
        intent = action["intent"]
        intents = ["OPEN_APP","SAVE_ALIAS","MEMORIZE","RETRIEVE"]
        if intent in intents:
            extracted_entity = self.extract_entities(user_message,intent)
            return extracted_entity
        return action

