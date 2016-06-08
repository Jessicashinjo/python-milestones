# Python Planet List

## Adding to a list

Unlike JavaScript, in Python, there are several ways to add items to a list.

1. Using the `+` operator.
1. Use the `append(value)` method to add a single, new value.
1. Use the `extend(new_list)` method which will concatenate another list on to the end of a list.
1. Use the `insert(loc, value)` method to insert a single, new value at a specific location in a list.

## Exercise

```
mkdir -p ~/workspace/python/exercises/lists && cd $_
echo 'planet_list = ["mercury", "mars"]
pla' >> planets.py
subl .
```

1. Use `append()` to add Jupiter and Saturn at the end of the list.
1. Use the `extend()` method to add another list of the last two planets in our solar system to the end of the list.
1. Use `insert()` to add Earth, and Venus in the correct order.
1. Use `append()` again to add Pluto to the end of the list.
1. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called `rocky_planets`.
1. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the `del` operation to remove it from the end of `planet_list`.

