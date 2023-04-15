"""
Breath-First-Search (BFS) is a fundamental algorithmic technique used in graph traversal, tree traversal and other
related algorithms. It is particularly useful when searching for the shortest path or the closest target in a graph.

To illustrate this concept, we will demonstrate how to use BFS to find the closest target in a graph by combining the
Dictionary and Queue to create a Graph logic.

The basic idea behind BFS is to traverse the graph layer by layer, exploring all the nodes at each layer before
moving on to the next layer. To implement BFS, we use a queue data structure to keep track of the nodes to be
explored and a dictionary to keep track of the visited nodes.

In our demonstration, we will create a graph of people who know each other, represented as a dictionary with the
Person objects as keys and a list of the Person objects they know as values. We will then perform a BFS starting from
a given Person object to find the closest person who has a specific job, such as an engineer.

To accomplish this, we will first create a Person class with a name and job attributes. We will then create several
instances of the Person class and populate the graph with their relationships.

Once the graph is established, we will implement a search function that takes a Person object as an input and
performs a BFS to find the closest person with the specified job. The search function will use a queue to keep track
of the nodes to be explored and a list to keep track of the visited nodes.

At each step of the BFS, the search function will dequeue the first node in the queue and check if it is the target
node with the specified job. If it is, the function will display the name of the person and terminate. Otherwise,
the function will add all the nodes connected to the current node to the end of the queue and mark the current node
as visited.

By using the BFS algorithm with the combination of dictionary and queue to create a graph logic, we are able to
efficiently find the closest person with the specified job in a network of relationships. This technique can be
applied to a wide range of problems, from social networks to computer networks, and is a powerful tool for solving
graph traversal problems.
"""
from collections import deque


class Person:
    def __init__(self, name: str, job: str):
        self.name = name
        self.job = job

    def show_detail(self):
        print(f"\t{self.name.title()} is the person who you are looking for.")


PersonA = Person("Nguyen Ngoc Vinh", "developer")
PersonB = Person("B", "doctor")
PersonC = Person("C", "baker")
PersonD = Person("D", "racer")
PersonE = Person("E", "seller")
PersonF = Person("F", "engineer")
PersonG = Person("G", "gamer")
PersonH = Person("H", "engineer")
PersonI = Person("I", "doctor")
PersonJ = Person("J", "vet")

"""
Person A knows B C D E, 
Person B knows C D G I J
Person C knows J H
Person E knows A B F 
Person H knows D E
"""

relationGraph = {
    PersonA: [PersonB, PersonC, PersonD, PersonE],
    PersonB: [PersonC, PersonD, PersonG, PersonI, PersonJ],
    PersonC: [PersonJ, PersonH],
    PersonD: [],
    PersonE: [PersonA, PersonB, PersonF],
    PersonF: [],
    PersonG: [],
    PersonH: [PersonD, PersonE],
    PersonI: [],
    PersonJ: []
}


def search(person: Person, job: str):
    print(f"Find the closest \"{job}\" to {person.name}:")
    search_queue = deque()
    search_queue += relationGraph[person]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person.job == job:
                person.show_detail()
                break
            else:
                search_queue += relationGraph[person]
                searched.append(person)


search(PersonA, "engineer")  # The person should be H
