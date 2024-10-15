<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This adder adds two 4 bits binary values and returns the result. 

From the source code, we can see that the orginal inputs are used to create two immediate values: one through binary XOR, and the other through binary AND. This is an intersting procedure, as the immediate values then got grouped into two bit values. Lastly, another XOR operation is performed. Lastly, the sum and a carry_out value is produced. When the sum is greater than 15, then value is truncated and the carray_out is set to one.


## How to test

We created Python tests to determine whether the results are valid. The logic is simple, add the two input values (0 ~ 15). The result is moded by 16 to obtain the sum, and divided by 16 to get the carry_out.

## External hardware

For this assignment, I am unaware of any external hardwares needed.
