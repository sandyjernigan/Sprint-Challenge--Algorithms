#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

`n` to the 3rd power compared to adding `a = a + n * n`,
will run `n` times before `a` will be greater than or equal to `n` to the 3rd power.
Therefore, this is a linear formula. The runtime grows at the same rate as the input.

b) O(c^n)

As the input grows the runtime is growing at a much faster rate. 
if `n` is 2 this will run twice, however if `n` is 100 it'll run 700 times and if `n` is 200 it'll fun 1600 times. 

c) O(n)

This function is resursive and will run back on itself `n` times until you have 0 bunnies. 
Therefore, this is a linear formula. The runtime grows at the same rate as the input.

## Exercise II

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

### You've got to crack a few eggs to make an omelette

    def dropEgg(n):
      > Suppose that you have an n-story building and plenty of eggs.
      > `n` will be the number of stories of the building. Assume this will be a positive integer

      > Start Out with the egg isn't broken
      brokenEgg = FALSE

      > Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f.      
      > `f` will the floor
      > `breakpoint` is the floor in which the egg will break if it is dropped at that floor

      if f >= breakPoint:

        > the egg will break
        brokenEgg = TRUE

        > If less than the floor at which the egg will break, the egg doesn't get broken. This is already set to FALSE so no change needs to be made.

      > Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.
      > # One idea to determine the floor at which the egg will break is to start at the halfway point and see if the egg breaks.

### pseudocode
    def dropEgg(n):
      brokenEgg = FALSE
      lowestBreakFloor = 0 # This will be the lowest tested floor that egg broke
      highestSafeFloor = 0 # This will be the highest tested floor that egg did not break

      half = len(n) // 2 # get first halfway point

      while (lowestBreakFloor - highestSafeFloor != 1):

        testFloor = half

        if (at testFloor a dropped Egg returns broken egg):
          brokenEgg = TRUE
          lowestBreakFloor = testFloor

        else:
          brokenEgg = FALSE
          highestSafeFloor = testFloor
        
        testFloor = lowestBreakFloor - ((lowestBreakFloor - highestSafeFloor) // 2) # Find next halfway between the highest safe floor and the lowest break floor and test again

      breakPoint = lowestBreakFloor
      return breakPoint
      
      


