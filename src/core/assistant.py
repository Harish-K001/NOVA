class Assistant:

    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.creator = "HK"

    def greet(self):
        print(f"Hello! {self.creator}, Great to see you online!")

    def introduce(self):
        print(f"Hello! I am {self.name} (Version {self.version},) Created by {self.creator}, Your Local AI assistant. I help automate your ThinkPad, manage tasks, and learn your workflow over time.")
        