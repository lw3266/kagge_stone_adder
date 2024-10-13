# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.a.value = 13
    dut.b.value = 10

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 10)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1 

    # Set the input values you want to test
    dut.a.value = 8
    dut.b.value = 10

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 10)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.

    Test case #0
    dut.a.value = 7
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    Test case #1
    dut.a.value = 9
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    Test case #2
    dut.a.value = 1
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    Test case #3
    dut.a.value = 10
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    Test case #4
    dut.a.value = 9
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    Test case #5
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    Test case #6
    dut.a.value = 2
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    Test case #7
    dut.a.value = 3
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    Test case #8
    dut.a.value = 12
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    Test case #9
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    Test case #10
    dut.a.value = 11
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    Test case #11
    dut.a.value = 7
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    Test case #12
    dut.a.value = 6
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    Test case #13
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    Test case #14
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    Test case #15
    dut.a.value = 9
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    Test case #16
    dut.a.value = 6
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    Test case #17
    dut.a.value = 13
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    Test case #18
    dut.a.value = 1
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    Test case #19
    dut.a.value = 3
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    Test case #20
    dut.a.value = 5
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    Test case #21
    dut.a.value = 5
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    Test case #22
    dut.a.value = 8
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    Test case #23
    dut.a.value = 14
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    Test case #24
    dut.a.value = 11
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    Test case #25
    dut.a.value = 13
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    Test case #26
    dut.a.value = 11
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    Test case #27
    dut.a.value = 4
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    Test case #28
    dut.a.value = 14
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    Test case #29
    dut.a.value = 4
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    Test case #30
    dut.a.value = 1
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    Test case #31
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    Test case #32
    dut.a.value = 0
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    Test case #33
    dut.a.value = 14
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    Test case #34
    dut.a.value = 1
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    Test case #35
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    Test case #36
    dut.a.value = 14
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    Test case #37
    dut.a.value = 14
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    Test case #38
    dut.a.value = 10
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    Test case #39
    dut.a.value = 11
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    Test case #40
    dut.a.value = 15
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    Test case #41
    dut.a.value = 12
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    Test case #42
    dut.a.value = 12
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    Test case #43
    dut.a.value = 11
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    Test case #44
    dut.a.value = 2
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    Test case #45
    dut.a.value = 12
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    Test case #46
    dut.a.value = 12
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    Test case #47
    dut.a.value = 11
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    Test case #48
    dut.a.value = 2
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    Test case #49
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    Test case #50
    dut.a.value = 11
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    Test case #51
    dut.a.value = 10
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    Test case #52
    dut.a.value = 11
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    Test case #53
    dut.a.value = 1
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    Test case #54
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    Test case #55
    dut.a.value = 12
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    Test case #56
    dut.a.value = 5
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    Test case #57
    dut.a.value = 14
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    Test case #58
    dut.a.value = 9
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    Test case #59
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    Test case #60
    dut.a.value = 8
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    Test case #61
    dut.a.value = 15
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    Test case #62
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    Test case #63
    dut.a.value = 1
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    Test case #64
    dut.a.value = 5
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    Test case #65
    dut.a.value = 7
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    Test case #66
    dut.a.value = 9
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    Test case #67
    dut.a.value = 10
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    Test case #68
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    Test case #69
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    Test case #70
    dut.a.value = 8
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    Test case #71
    dut.a.value = 4
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    Test case #72
    dut.a.value = 15
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    Test case #73
    dut.a.value = 14
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    Test case #74
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    Test case #75
    dut.a.value = 4
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    Test case #76
    dut.a.value = 4
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    Test case #77
    dut.a.value = 10
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    Test case #78
    dut.a.value = 14
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    Test case #79
    dut.a.value = 9
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    Test case #80
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    Test case #81
    dut.a.value = 4
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    Test case #82
    dut.a.value = 1
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    Test case #83
    dut.a.value = 9
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    Test case #84
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    Test case #85
    dut.a.value = 12
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    Test case #86
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    Test case #87
    dut.a.value = 15
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    Test case #88
    dut.a.value = 3
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    Test case #89
    dut.a.value = 3
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    Test case #90
    dut.a.value = 8
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    Test case #91
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    Test case #92
    dut.a.value = 11
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    Test case #93
    dut.a.value = 2
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    Test case #94
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    Test case #95
    dut.a.value = 13
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    Test case #96
    dut.a.value = 11
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    Test case #97
    dut.a.value = 10
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    Test case #98
    dut.a.value = 15
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    Test case #99
    dut.a.value = 8
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
