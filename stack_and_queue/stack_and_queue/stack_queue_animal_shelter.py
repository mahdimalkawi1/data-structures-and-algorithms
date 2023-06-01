class Animal:
    """Class representing an animal in the shelter."""
    def __init__(self, species, name):
        """
        Initialize an Animal object.

        Args:
            species (str): The species of the animal.
            name (str): The name of the animal.
        """
        self.species = species
        self.name = name

    def __str__(self):
        """
        Return a string representation of the Animal.

        Returns:
            str: A string representation of the Animal.
        """
        return f"{self.name} ({self.species})"


class AnimalShelter:
    """Class representing an animal shelter."""
    def __init__(self):
        """Initialize an AnimalShelter object."""
        self.animal_queue = []

    def enqueue(self, animal, species):
        """
        Add an animal to the shelter.

        Args:
            animal (Animal): The animal object to be added.
            species (str): The species of the animal.

        """
        self.animal_queue.append(animal)

    def dequeue(self, pref=None):
        """
        Remove and return an animal from the shelter.

        If a preference (species) is specified, the first animal of that species
        will be removed and returned. If no preference is specified, the animal
        that has been waiting in the shelter the longest will be removed and returned.

        Args:
            pref (str, optional): The preferred species of the animal. Defaults to None.

        Returns:
            Animal or None: The removed animal object or None if no matching animal found.
        """
        if pref is None:
            return self.animal_queue.pop(0)

        matching_animals = [animal for animal in self.animal_queue if animal.species == pref]
        if matching_animals:
            selected_animal = matching_animals[0]
            self.animal_queue.remove(selected_animal)
            return selected_animal

        return None

    def __str__(self):
        """
        Return a string representation of the AnimalShelter.

        Returns:
            str: A string representation of the AnimalShelter.
        """
        return ', '.join(str(animal) for animal in self.animal_queue)


if __name__ == "__main__":
    q = AnimalShelter()
    q.enqueue(Animal("cat", "lele"), "cat")
    q.enqueue(Animal("dog", "jax"), "dog")
    q.enqueue(Animal("cat", "meme"), "cat")
    print(q)
    q.dequeue("dog")
    print(q)
    q.dequeue("cat")
    print(q)
    q.dequeue("cat")
    print(q)
    q.dequeue("dog")

    # Handling stretch goal - dequeue without preference.
    print("Dequeue without preference:")
    q.enqueue(Animal("cat", "kitty"), "cat")
    q.enqueue(Animal("dog", "buddy"), "dog")
    q.enqueue(Animal("cat", "fluffy"), "cat")
    print(q)
    print(q.dequeue())  # Dequeue without preference
    print(q)
