# Exercise 5.7 Health station

In the exercise base there is the class `Person`, which we are already quite familiar with. There is also an outline for the class `HealthStation`. Health station objects process people in different ways, they e.g. weigh and feed people. In this exercise we will construct a health station. The code of the Person class should not be modified in this exercise!

## Weighing people

In the outline of the Health station there is an outline for the method `weigh`:

```python
class HealthStation:

    def weigh(self, person):
        # return the weight of the person passed as the parameter
        return -1
```

The method receives a person as a parameter, and it is meant to return to its caller the weight of that person. The weight information can be found by calling a suitable method of the person `person`. **So your task is to complete the code of the method!**

Here is a main program where a health station weight two people:
```python
def main():
    # example main program for the first section of the exercise

    childrens_hospital = HealthStation()

    ethan = Person("Ethan", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(ethan.get_name() + " weight: " + str(childrens_hospital.weigh(ethan)) + " kilos")
    print(peter.get_name() + " weight: " + str(childrens_hospital.weigh(peter)) + " kilos")

```

The output should be the following:

```plaintext
Ethan's weight: 7 kilos
Peter's weight: 85 kilos
```

## Feeding

It is possible to modify the state of the object that is received as a parameter. Write a method called `def feed(self, person)` for the health station. It should increase the weight of the parameter person by one.

Following is an example where people are weighed first, and then ethan is fed three times in the children's hospital. After this the people are weighed again:

```python
def main():
    childrens_hospital = HealthStation()

    ethan = Person("Ethan", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(ethan.get_name() + " weight: " + str(childrens_hospital.weigh(ethan)) + " kilos")
    print(peter.get_name() + " weight: " + str(childrens_hospital.weigh(peter)) + " kilos")

    childrens_hospital.feed(ethan)
    childrens_hospital.feed(ethan)
    childrens_hospital.feed(ethan)

    print("")

    print(ethan.get_name() + " weight: " + str(childrens_hospital.weigh(ethan)) + " kilos")
    print(peter.get_name() + " weight: " + str(childrens_hospital.weigh(peter)) + " kilos")
```

The output should reveal that Ethan's weight has increased by three:

```plaintext
Ethan weight: 7 kilos
Peter weight: 85 kilos

Ethan weight: 10 kilos
Peter weight: 85 kilos
```

## Counting weighings



Create a new method called `def weighings()` for the health station. It should tell how many weighings the health station has performed. *NB! You will need a new object variable for counting the number of weighings!*. Test main program:

```python
def main():

    childrens_hospital = HealthStation()

    ethan = Person("Ethan", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print("weighings performed: " + childrens_hospital.weighings())

    childrens_hospital.weigh(ethan)
    childrens_hospital.weigh(peter)

    print("weighings performed: " + childrens_hospital.weighings())

    childrens_hospital.weigh(ethan)
    childrens_hospital.weigh(ethan)
    childrens_hospital.weigh(ethan)
    childrens_hospital.weigh(ethan)

    print("weighings performed: " + childrens_hospital.weighings())
}
```

The output is:

```plaintext
weighings performed: 0
weighings performed: 2
weighings performed: 6
```
