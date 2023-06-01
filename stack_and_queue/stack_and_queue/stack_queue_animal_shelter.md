# stack_queue_animal_shelter.


## Whiteboard Process
![ white board](./assetes/Untitled%20(21).jpg)
![ white board](./assetes/Untitled%20(20).jpg)



## Approach & Efficiency
##### enqueue 
- Time Complexity:
The time complexity of the code is O(1). 
- Space Complexity:
The space complexity of the code is also O(1).
##### dequeue 
- Time Complexity:
The time complexity of the code is O(n). 
- Space Complexity:
The space complexity of the code is  O(1). 

## Solution 

 ``` python 
  def enqueue(self, animal, species):
        self.animal_queue.append(animal)

    def dequeue(self, pref=None):
       
        if pref is None:
            return self.animal_queue.pop(0)

        matching_animals = [animal for animal in self.animal_queue if animal.species == pref]
        if matching_animals:
            selected_animal = matching_animals[0]
            self.animal_queue.remove(selected_animal)
            return selected_animal

        return None
``` 

- Input:
lele (cat), meme (cat)
- Output:
lele (cat), jax (dog), meme (cat)
- Input:
lele (cat), jax (dog), meme (cat)
- Output:
lele (cat), meme (cat)
