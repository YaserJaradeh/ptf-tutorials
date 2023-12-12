import random
from typing import List


class Behavior:
    """
    Base class for all behaviors.
    """
    def __init__(self, name: str):
        self.name = name

    def __call__(self, *args, **kwargs):
        """
        Shortcut for run method.
        """
        return self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        """
        Run the behavior.
        This should contain the actual logic of the behavior.
        :param args: the positional arguments
        :param kwargs: the keyword arguments
        :return: True if the behavior succeeded, False otherwise
        """
        print(f"Running {self.name} - True")
        return True

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self):
        return self.name


class Composite(Behavior):
    """
    Base class for all composite behaviors.
    """
    def __init__(self, name: str, children: List[Behavior]):
        super().__init__(name)
        self.children = children

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.children})"

    def __add__(self, other: str | Behavior):
        """
        Add a child to the composite.
        The child can be a string or a behavior.
        :param other:
        :return:
        """
        if isinstance(other, str):
            self.children.append(Behavior(other))
        else:
            self.children.append(other)
        return self


class Sequence(Composite):
    """
    A sequence of behaviors.
    """
    def run(self, *args, **kwargs):
        """
        Run the sequence.
        All the children must succeed in order for the sequence to succeed.
        """
        for child in self.children:
            if not child(*args, **kwargs):
                return False
        return True


class Selector(Composite):
    """
    A selector of behaviors.
    """
    def run(self, *args, **kwargs):
        """
        Run the selector.
        The first child that succeeds will make the selector succeed.
        """
        for child in self.children:
            if child(*args, **kwargs):
                return True
        return False


class Decorator(Behavior):
    """
    Base class for all decorator behaviors.
    """
    def __init__(self, name: str, child: Behavior):
        super().__init__(name)
        self.child = child

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.child})"


class Inverter(Decorator):
    """
    Invert the result of the child behavior.
    """
    def run(self, *args, **kwargs):
        """
        Run the inverter.
        This will invert the result of the child behavior.
        """
        return not self.child(*args, **kwargs)


class AlwaysTrue(Behavior):
    """
    Always return True.
    """
    def run(self, *args, **kwargs):
        print(f"Running {self.name} - True")
        return True


class AlwaysFalse(Behavior):
    """
    Always return False.
    """
    def run(self, *args, **kwargs):
        print(f"Running {self.name} - False")
        return False


class ChanceBehavior(Behavior):
    """
    Return True with a given chance.
    """
    def __init__(self, name: str, chance: float):
        super().__init__(name)
        self.chance = chance

    def run(self, *args, **kwargs):
        """
        Run the chance behavior.
        This will return True with a given chance.
        """
        result = random.random() < self.chance
        print(f"Running {self.name} - {result}")
        return result


# Example usage:
if __name__ == '__main__':
    # First tree example
    tree = Sequence("Wanna eat", [])
    tree += Behavior("Is hungry?")
    tree += AlwaysFalse("Is food available?")
    tree += Behavior("Eat food")
    print(tree)
    tree()

    print("-" * 20)

    # Second tree example
    break_in = Selector("Break In", [])
    break_in += AlwaysFalse("Open door")
    break_in += AlwaysFalse("Open window")
    break_in += AlwaysTrue("Break window")

    tree = Sequence("Steal stuff", [])
    tree += break_in
    tree += Behavior("Disable alarm")
    tree += Behavior("Take valuables")

    print(tree)
    tree()

    print("-" * 20)

    # Third tree example
    random.seed(1233325432667)  # change to something else to make the tree fails

    tree = Sequence("Parse paper", [])
    tree += AlwaysTrue("Download abstract")
    tree += AlwaysTrue("Is LLM available?")
    tree += AlwaysTrue("Extract entities")
    tree += ChanceBehavior("Extract relations", 0.1)
    tree += AlwaysTrue("Add to ORKG")

    print(tree)
    tree(x=4)

