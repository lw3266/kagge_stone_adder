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

    # Test case #0
    dut.a.value = 7
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #1
    dut.a.value = 9
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #2
    dut.a.value = 1
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #3
    dut.a.value = 10
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #4
    dut.a.value = 9
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #5
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #6
    dut.a.value = 2
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #7
    dut.a.value = 3
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #8
    dut.a.value = 12
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #9
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #10
    dut.a.value = 11
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #11
    dut.a.value = 7
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #12
    dut.a.value = 6
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #13
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #14
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #15
    dut.a.value = 9
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #16
    dut.a.value = 6
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #17
    dut.a.value = 13
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #18
    dut.a.value = 1
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #19
    dut.a.value = 3
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #20
    dut.a.value = 5
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #21
    dut.a.value = 5
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #22
    dut.a.value = 8
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #23
    dut.a.value = 14
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #24
    dut.a.value = 11
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #25
    dut.a.value = 13
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #26
    dut.a.value = 11
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #27
    dut.a.value = 4
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #28
    dut.a.value = 14
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #29
    dut.a.value = 4
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #30
    dut.a.value = 1
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #31
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #32
    dut.a.value = 0
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #33
    dut.a.value = 14
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #34
    dut.a.value = 1
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #35
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #36
    dut.a.value = 14
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #37
    dut.a.value = 14
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #38
    dut.a.value = 10
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #39
    dut.a.value = 11
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #40
    dut.a.value = 15
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #41
    dut.a.value = 12
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #42
    dut.a.value = 12
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #43
    dut.a.value = 11
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #44
    dut.a.value = 2
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #45
    dut.a.value = 12
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #46
    dut.a.value = 12
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #47
    dut.a.value = 11
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #48
    dut.a.value = 2
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #49
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #50
    dut.a.value = 11
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #51
    dut.a.value = 10
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #52
    dut.a.value = 11
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #53
    dut.a.value = 1
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #54
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #55
    dut.a.value = 12
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #56
    dut.a.value = 5
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #57
    dut.a.value = 14
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #58
    dut.a.value = 9
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #59
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #60
    dut.a.value = 8
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #61
    dut.a.value = 15
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #62
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #63
    dut.a.value = 1
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #64
    dut.a.value = 5
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #65
    dut.a.value = 7
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #66
    dut.a.value = 9
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #67
    dut.a.value = 10
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #68
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #69
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #70
    dut.a.value = 8
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #71
    dut.a.value = 4
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #72
    dut.a.value = 15
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #73
    dut.a.value = 14
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #74
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #75
    dut.a.value = 4
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #76
    dut.a.value = 4
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #77
    dut.a.value = 10
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #78
    dut.a.value = 14
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #79
    dut.a.value = 9
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #80
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #81
    dut.a.value = 4
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #82
    dut.a.value = 1
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #83
    dut.a.value = 9
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #84
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #85
    dut.a.value = 12
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #86
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #87
    dut.a.value = 15
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #88
    dut.a.value = 3
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #89
    dut.a.value = 3
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #90
    dut.a.value = 8
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #91
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #92
    dut.a.value = 11
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #93
    dut.a.value = 2
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #94
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #95
    dut.a.value = 13
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #96
    dut.a.value = 11
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #97
    dut.a.value = 10
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #98
    dut.a.value = 15
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #99
    dut.a.value = 8
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #100
    dut.a.value = 8
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #101
    dut.a.value = 11
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #102
    dut.a.value = 5
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #103
    dut.a.value = 14
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #104
    dut.a.value = 8
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #105
    dut.a.value = 8
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #106
    dut.a.value = 9
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #107
    dut.a.value = 13
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #108
    dut.a.value = 12
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #109
    dut.a.value = 14
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #110
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #111
    dut.a.value = 12
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #112
    dut.a.value = 12
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #113
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #114
    dut.a.value = 10
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #115
    dut.a.value = 5
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #116
    dut.a.value = 14
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #117
    dut.a.value = 5
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #118
    dut.a.value = 11
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #119
    dut.a.value = 12
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #120
    dut.a.value = 6
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #121
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #122
    dut.a.value = 2
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #123
    dut.a.value = 4
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #124
    dut.a.value = 15
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #125
    dut.a.value = 5
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #126
    dut.a.value = 13
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #127
    dut.a.value = 14
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #128
    dut.a.value = 8
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #129
    dut.a.value = 4
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #130
    dut.a.value = 10
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #131
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #132
    dut.a.value = 10
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #133
    dut.a.value = 12
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #134
    dut.a.value = 14
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #135
    dut.a.value = 8
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #136
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #137
    dut.a.value = 3
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #138
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #139
    dut.a.value = 13
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #140
    dut.a.value = 9
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #141
    dut.a.value = 5
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #142
    dut.a.value = 4
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #143
    dut.a.value = 15
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #144
    dut.a.value = 3
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #145
    dut.a.value = 15
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #146
    dut.a.value = 13
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #147
    dut.a.value = 6
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #148
    dut.a.value = 14
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #149
    dut.a.value = 12
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #150
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #151
    dut.a.value = 0
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #152
    dut.a.value = 0
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #153
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #154
    dut.a.value = 11
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #155
    dut.a.value = 7
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #156
    dut.a.value = 4
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #157
    dut.a.value = 11
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #158
    dut.a.value = 0
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #159
    dut.a.value = 6
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #160
    dut.a.value = 14
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #161
    dut.a.value = 1
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #162
    dut.a.value = 9
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #163
    dut.a.value = 3
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #164
    dut.a.value = 9
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #165
    dut.a.value = 3
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #166
    dut.a.value = 4
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #167
    dut.a.value = 9
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #168
    dut.a.value = 7
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #169
    dut.a.value = 0
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #170
    dut.a.value = 0
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #171
    dut.a.value = 6
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #172
    dut.a.value = 4
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #173
    dut.a.value = 14
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #174
    dut.a.value = 12
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #175
    dut.a.value = 8
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #176
    dut.a.value = 9
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #177
    dut.a.value = 6
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #178
    dut.a.value = 0
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #179
    dut.a.value = 10
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #180
    dut.a.value = 10
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #181
    dut.a.value = 12
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #182
    dut.a.value = 1
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #183
    dut.a.value = 3
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #184
    dut.a.value = 4
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #185
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #186
    dut.a.value = 11
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #187
    dut.a.value = 9
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #188
    dut.a.value = 2
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #189
    dut.a.value = 4
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #190
    dut.a.value = 11
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #191
    dut.a.value = 9
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #192
    dut.a.value = 5
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #193
    dut.a.value = 8
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #194
    dut.a.value = 9
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #195
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #196
    dut.a.value = 0
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #197
    dut.a.value = 2
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #198
    dut.a.value = 0
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #199
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #200
    dut.a.value = 8
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #201
    dut.a.value = 8
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #202
    dut.a.value = 6
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #203
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #204
    dut.a.value = 9
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #205
    dut.a.value = 7
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #206
    dut.a.value = 5
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #207
    dut.a.value = 10
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #208
    dut.a.value = 15
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #209
    dut.a.value = 0
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #210
    dut.a.value = 4
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #211
    dut.a.value = 12
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #212
    dut.a.value = 9
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #213
    dut.a.value = 7
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #214
    dut.a.value = 3
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #215
    dut.a.value = 13
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #216
    dut.a.value = 6
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #217
    dut.a.value = 0
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #218
    dut.a.value = 7
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #219
    dut.a.value = 5
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #220
    dut.a.value = 12
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #221
    dut.a.value = 6
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #222
    dut.a.value = 12
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #223
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #224
    dut.a.value = 2
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #225
    dut.a.value = 4
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #226
    dut.a.value = 10
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #227
    dut.a.value = 11
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #228
    dut.a.value = 15
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #229
    dut.a.value = 12
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #230
    dut.a.value = 4
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #231
    dut.a.value = 15
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #232
    dut.a.value = 15
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 1
    
    # Test case #233
    dut.a.value = 7
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #234
    dut.a.value = 3
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #235
    dut.a.value = 7
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #236
    dut.a.value = 8
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #237
    dut.a.value = 1
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #238
    dut.a.value = 13
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #239
    dut.a.value = 15
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 1
    
    # Test case #240
    dut.a.value = 9
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #241
    dut.a.value = 6
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #242
    dut.a.value = 5
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #243
    dut.a.value = 7
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #244
    dut.a.value = 4
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #245
    dut.a.value = 7
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #246
    dut.a.value = 13
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #247
    dut.a.value = 2
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #248
    dut.a.value = 5
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #249
    dut.a.value = 2
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #250
    dut.a.value = 5
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #251
    dut.a.value = 8
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #252
    dut.a.value = 7
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #253
    dut.a.value = 1
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #254
    dut.a.value = 6
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #255
    dut.a.value = 4
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #256
    dut.a.value = 5
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #257
    dut.a.value = 2
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #258
    dut.a.value = 12
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #259
    dut.a.value = 14
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #260
    dut.a.value = 13
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #261
    dut.a.value = 8
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #262
    dut.a.value = 12
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #263
    dut.a.value = 6
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #264
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #265
    dut.a.value = 10
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #266
    dut.a.value = 2
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #267
    dut.a.value = 7
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #268
    dut.a.value = 11
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #269
    dut.a.value = 15
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #270
    dut.a.value = 9
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #271
    dut.a.value = 0
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #272
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #273
    dut.a.value = 8
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #274
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #275
    dut.a.value = 10
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #276
    dut.a.value = 13
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #277
    dut.a.value = 3
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #278
    dut.a.value = 12
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #279
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #280
    dut.a.value = 2
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #281
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #282
    dut.a.value = 8
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #283
    dut.a.value = 14
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #284
    dut.a.value = 9
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #285
    dut.a.value = 5
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #286
    dut.a.value = 1
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #287
    dut.a.value = 1
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #288
    dut.a.value = 9
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #289
    dut.a.value = 9
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #290
    dut.a.value = 1
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #291
    dut.a.value = 15
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1
    
    # Test case #292
    dut.a.value = 5
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #293
    dut.a.value = 7
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #294
    dut.a.value = 12
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #295
    dut.a.value = 2
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #296
    dut.a.value = 9
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #297
    dut.a.value = 2
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #298
    dut.a.value = 13
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #299
    dut.a.value = 5
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #300
    dut.a.value = 14
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #301
    dut.a.value = 9
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #302
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #303
    dut.a.value = 14
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #304
    dut.a.value = 5
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #305
    dut.a.value = 15
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #306
    dut.a.value = 10
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #307
    dut.a.value = 4
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #308
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #309
    dut.a.value = 1
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #310
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #311
    dut.a.value = 11
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #312
    dut.a.value = 15
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #313
    dut.a.value = 9
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #314
    dut.a.value = 14
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #315
    dut.a.value = 2
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #316
    dut.a.value = 9
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #317
    dut.a.value = 12
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #318
    dut.a.value = 7
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #319
    dut.a.value = 4
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #320
    dut.a.value = 2
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #321
    dut.a.value = 2
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #322
    dut.a.value = 2
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #323
    dut.a.value = 12
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #324
    dut.a.value = 1
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #325
    dut.a.value = 0
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 0
    
    # Test case #326
    dut.a.value = 0
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #327
    dut.a.value = 7
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #328
    dut.a.value = 9
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #329
    dut.a.value = 11
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #330
    dut.a.value = 15
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1
    
    # Test case #331
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #332
    dut.a.value = 10
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #333
    dut.a.value = 3
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #334
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #335
    dut.a.value = 13
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #336
    dut.a.value = 11
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #337
    dut.a.value = 11
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #338
    dut.a.value = 5
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #339
    dut.a.value = 1
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #340
    dut.a.value = 5
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #341
    dut.a.value = 6
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #342
    dut.a.value = 13
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #343
    dut.a.value = 5
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #344
    dut.a.value = 14
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #345
    dut.a.value = 14
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #346
    dut.a.value = 15
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #347
    dut.a.value = 6
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #348
    dut.a.value = 3
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #349
    dut.a.value = 10
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #350
    dut.a.value = 0
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #351
    dut.a.value = 14
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #352
    dut.a.value = 6
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #353
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #354
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #355
    dut.a.value = 1
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #356
    dut.a.value = 13
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #357
    dut.a.value = 13
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #358
    dut.a.value = 6
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #359
    dut.a.value = 1
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #360
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #361
    dut.a.value = 2
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #362
    dut.a.value = 2
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #363
    dut.a.value = 11
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #364
    dut.a.value = 1
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #365
    dut.a.value = 5
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #366
    dut.a.value = 12
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #367
    dut.a.value = 13
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #368
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #369
    dut.a.value = 13
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #370
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #371
    dut.a.value = 5
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #372
    dut.a.value = 7
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #373
    dut.a.value = 11
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #374
    dut.a.value = 4
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #375
    dut.a.value = 1
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #376
    dut.a.value = 12
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #377
    dut.a.value = 10
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #378
    dut.a.value = 11
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #379
    dut.a.value = 4
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #380
    dut.a.value = 11
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #381
    dut.a.value = 14
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #382
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #383
    dut.a.value = 10
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #384
    dut.a.value = 3
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #385
    dut.a.value = 6
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #386
    dut.a.value = 7
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #387
    dut.a.value = 6
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #388
    dut.a.value = 13
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #389
    dut.a.value = 11
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #390
    dut.a.value = 15
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #391
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #392
    dut.a.value = 0
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #393
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #394
    dut.a.value = 10
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #395
    dut.a.value = 8
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #396
    dut.a.value = 7
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #397
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #398
    dut.a.value = 1
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #399
    dut.a.value = 11
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #400
    dut.a.value = 0
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #401
    dut.a.value = 10
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #402
    dut.a.value = 13
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #403
    dut.a.value = 5
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #404
    dut.a.value = 3
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #405
    dut.a.value = 13
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #406
    dut.a.value = 13
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #407
    dut.a.value = 13
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #408
    dut.a.value = 11
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #409
    dut.a.value = 8
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #410
    dut.a.value = 5
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #411
    dut.a.value = 12
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #412
    dut.a.value = 6
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #413
    dut.a.value = 15
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #414
    dut.a.value = 2
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #415
    dut.a.value = 12
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #416
    dut.a.value = 13
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #417
    dut.a.value = 10
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #418
    dut.a.value = 8
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #419
    dut.a.value = 5
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #420
    dut.a.value = 0
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #421
    dut.a.value = 13
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #422
    dut.a.value = 9
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #423
    dut.a.value = 10
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #424
    dut.a.value = 2
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #425
    dut.a.value = 11
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #426
    dut.a.value = 3
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #427
    dut.a.value = 4
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #428
    dut.a.value = 1
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #429
    dut.a.value = 2
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #430
    dut.a.value = 14
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #431
    dut.a.value = 6
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #432
    dut.a.value = 5
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #433
    dut.a.value = 6
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #434
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #435
    dut.a.value = 8
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #436
    dut.a.value = 14
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #437
    dut.a.value = 15
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #438
    dut.a.value = 0
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #439
    dut.a.value = 12
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #440
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #441
    dut.a.value = 9
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #442
    dut.a.value = 14
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #443
    dut.a.value = 10
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #444
    dut.a.value = 1
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #445
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #446
    dut.a.value = 10
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #447
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #448
    dut.a.value = 10
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #449
    dut.a.value = 13
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #450
    dut.a.value = 12
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #451
    dut.a.value = 13
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #452
    dut.a.value = 11
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #453
    dut.a.value = 2
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #454
    dut.a.value = 5
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #455
    dut.a.value = 13
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #456
    dut.a.value = 6
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #457
    dut.a.value = 2
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #458
    dut.a.value = 4
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #459
    dut.a.value = 4
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #460
    dut.a.value = 8
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #461
    dut.a.value = 5
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #462
    dut.a.value = 0
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 0
    
    # Test case #463
    dut.a.value = 2
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #464
    dut.a.value = 1
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 0
    
    # Test case #465
    dut.a.value = 6
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #466
    dut.a.value = 6
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #467
    dut.a.value = 8
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #468
    dut.a.value = 15
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #469
    dut.a.value = 13
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #470
    dut.a.value = 8
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #471
    dut.a.value = 7
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #472
    dut.a.value = 1
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #473
    dut.a.value = 3
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #474
    dut.a.value = 5
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #475
    dut.a.value = 11
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #476
    dut.a.value = 14
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #477
    dut.a.value = 15
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1
    
    # Test case #478
    dut.a.value = 0
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #479
    dut.a.value = 9
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #480
    dut.a.value = 2
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #481
    dut.a.value = 15
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #482
    dut.a.value = 3
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #483
    dut.a.value = 9
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #484
    dut.a.value = 1
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #485
    dut.a.value = 8
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #486
    dut.a.value = 1
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #487
    dut.a.value = 8
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #488
    dut.a.value = 8
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #489
    dut.a.value = 8
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #490
    dut.a.value = 2
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #491
    dut.a.value = 10
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #492
    dut.a.value = 4
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #493
    dut.a.value = 14
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #494
    dut.a.value = 11
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #495
    dut.a.value = 6
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #496
    dut.a.value = 8
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #497
    dut.a.value = 5
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #498
    dut.a.value = 12
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #499
    dut.a.value = 14
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #500
    dut.a.value = 5
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #501
    dut.a.value = 7
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #502
    dut.a.value = 5
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #503
    dut.a.value = 9
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #504
    dut.a.value = 10
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #505
    dut.a.value = 10
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #506
    dut.a.value = 5
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #507
    dut.a.value = 12
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #508
    dut.a.value = 14
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #509
    dut.a.value = 15
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #510
    dut.a.value = 2
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #511
    dut.a.value = 7
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #512
    dut.a.value = 11
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #513
    dut.a.value = 6
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #514
    dut.a.value = 11
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #515
    dut.a.value = 5
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #516
    dut.a.value = 11
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #517
    dut.a.value = 7
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #518
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #519
    dut.a.value = 14
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #520
    dut.a.value = 2
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #521
    dut.a.value = 1
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #522
    dut.a.value = 13
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #523
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #524
    dut.a.value = 7
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #525
    dut.a.value = 4
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #526
    dut.a.value = 6
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #527
    dut.a.value = 4
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #528
    dut.a.value = 8
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #529
    dut.a.value = 8
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #530
    dut.a.value = 15
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #531
    dut.a.value = 4
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #532
    dut.a.value = 9
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #533
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #534
    dut.a.value = 12
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #535
    dut.a.value = 9
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #536
    dut.a.value = 1
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #537
    dut.a.value = 6
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #538
    dut.a.value = 7
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #539
    dut.a.value = 9
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #540
    dut.a.value = 8
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #541
    dut.a.value = 9
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #542
    dut.a.value = 9
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #543
    dut.a.value = 15
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #544
    dut.a.value = 8
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #545
    dut.a.value = 4
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #546
    dut.a.value = 5
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #547
    dut.a.value = 1
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #548
    dut.a.value = 5
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #549
    dut.a.value = 3
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #550
    dut.a.value = 4
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #551
    dut.a.value = 0
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #552
    dut.a.value = 7
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #553
    dut.a.value = 3
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #554
    dut.a.value = 13
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #555
    dut.a.value = 13
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #556
    dut.a.value = 9
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #557
    dut.a.value = 3
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #558
    dut.a.value = 4
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #559
    dut.a.value = 3
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #560
    dut.a.value = 10
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #561
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #562
    dut.a.value = 1
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #563
    dut.a.value = 13
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #564
    dut.a.value = 15
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #565
    dut.a.value = 7
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #566
    dut.a.value = 13
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #567
    dut.a.value = 8
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #568
    dut.a.value = 13
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #569
    dut.a.value = 2
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #570
    dut.a.value = 7
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #571
    dut.a.value = 0
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 0
    
    # Test case #572
    dut.a.value = 6
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #573
    dut.a.value = 3
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #574
    dut.a.value = 6
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #575
    dut.a.value = 6
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #576
    dut.a.value = 15
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #577
    dut.a.value = 15
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #578
    dut.a.value = 13
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #579
    dut.a.value = 6
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #580
    dut.a.value = 13
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #581
    dut.a.value = 0
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #582
    dut.a.value = 5
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #583
    dut.a.value = 14
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #584
    dut.a.value = 4
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #585
    dut.a.value = 13
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #586
    dut.a.value = 1
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #587
    dut.a.value = 13
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #588
    dut.a.value = 2
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #589
    dut.a.value = 2
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #590
    dut.a.value = 7
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #591
    dut.a.value = 9
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #592
    dut.a.value = 2
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #593
    dut.a.value = 6
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #594
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #595
    dut.a.value = 12
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #596
    dut.a.value = 10
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #597
    dut.a.value = 13
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #598
    dut.a.value = 6
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #599
    dut.a.value = 1
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #600
    dut.a.value = 13
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #601
    dut.a.value = 6
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #602
    dut.a.value = 13
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #603
    dut.a.value = 5
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #604
    dut.a.value = 4
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #605
    dut.a.value = 7
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #606
    dut.a.value = 0
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 0
    
    # Test case #607
    dut.a.value = 2
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #608
    dut.a.value = 9
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #609
    dut.a.value = 1
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #610
    dut.a.value = 5
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #611
    dut.a.value = 1
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #612
    dut.a.value = 11
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #613
    dut.a.value = 14
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #614
    dut.a.value = 11
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #615
    dut.a.value = 11
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #616
    dut.a.value = 14
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #617
    dut.a.value = 6
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #618
    dut.a.value = 5
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #619
    dut.a.value = 10
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #620
    dut.a.value = 3
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #621
    dut.a.value = 5
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #622
    dut.a.value = 2
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #623
    dut.a.value = 5
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #624
    dut.a.value = 15
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #625
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #626
    dut.a.value = 4
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #627
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #628
    dut.a.value = 10
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #629
    dut.a.value = 0
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #630
    dut.a.value = 1
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #631
    dut.a.value = 13
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #632
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #633
    dut.a.value = 11
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #634
    dut.a.value = 15
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #635
    dut.a.value = 13
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #636
    dut.a.value = 7
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #637
    dut.a.value = 5
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #638
    dut.a.value = 9
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #639
    dut.a.value = 5
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #640
    dut.a.value = 0
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #641
    dut.a.value = 13
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #642
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #643
    dut.a.value = 4
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #644
    dut.a.value = 2
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #645
    dut.a.value = 11
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #646
    dut.a.value = 1
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #647
    dut.a.value = 2
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #648
    dut.a.value = 12
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #649
    dut.a.value = 2
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #650
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #651
    dut.a.value = 13
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #652
    dut.a.value = 1
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #653
    dut.a.value = 4
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #654
    dut.a.value = 12
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #655
    dut.a.value = 3
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #656
    dut.a.value = 9
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #657
    dut.a.value = 1
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #658
    dut.a.value = 0
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #659
    dut.a.value = 10
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #660
    dut.a.value = 11
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #661
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #662
    dut.a.value = 13
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #663
    dut.a.value = 11
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #664
    dut.a.value = 5
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #665
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #666
    dut.a.value = 13
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #667
    dut.a.value = 3
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #668
    dut.a.value = 3
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #669
    dut.a.value = 9
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #670
    dut.a.value = 1
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #671
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #672
    dut.a.value = 12
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #673
    dut.a.value = 15
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #674
    dut.a.value = 3
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #675
    dut.a.value = 15
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1
    
    # Test case #676
    dut.a.value = 14
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #677
    dut.a.value = 10
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #678
    dut.a.value = 12
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #679
    dut.a.value = 5
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #680
    dut.a.value = 3
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #681
    dut.a.value = 10
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #682
    dut.a.value = 11
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #683
    dut.a.value = 14
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1
    
    # Test case #684
    dut.a.value = 5
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #685
    dut.a.value = 14
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #686
    dut.a.value = 3
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #687
    dut.a.value = 1
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #688
    dut.a.value = 8
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #689
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #690
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #691
    dut.a.value = 10
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #692
    dut.a.value = 15
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #693
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #694
    dut.a.value = 10
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #695
    dut.a.value = 14
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #696
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #697
    dut.a.value = 13
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #698
    dut.a.value = 6
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #699
    dut.a.value = 15
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #700
    dut.a.value = 3
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #701
    dut.a.value = 1
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #702
    dut.a.value = 8
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #703
    dut.a.value = 6
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #704
    dut.a.value = 4
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #705
    dut.a.value = 11
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #706
    dut.a.value = 13
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #707
    dut.a.value = 7
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #708
    dut.a.value = 10
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #709
    dut.a.value = 8
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #710
    dut.a.value = 7
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #711
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #712
    dut.a.value = 15
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1
    
    # Test case #713
    dut.a.value = 11
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #714
    dut.a.value = 9
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #715
    dut.a.value = 0
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #716
    dut.a.value = 8
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #717
    dut.a.value = 3
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #718
    dut.a.value = 4
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #719
    dut.a.value = 0
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #720
    dut.a.value = 11
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #721
    dut.a.value = 7
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #722
    dut.a.value = 1
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #723
    dut.a.value = 4
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #724
    dut.a.value = 11
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #725
    dut.a.value = 15
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #726
    dut.a.value = 3
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #727
    dut.a.value = 13
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #728
    dut.a.value = 14
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #729
    dut.a.value = 7
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #730
    dut.a.value = 3
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #731
    dut.a.value = 4
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #732
    dut.a.value = 9
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #733
    dut.a.value = 11
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #734
    dut.a.value = 0
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #735
    dut.a.value = 6
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #736
    dut.a.value = 7
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #737
    dut.a.value = 3
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #738
    dut.a.value = 11
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #739
    dut.a.value = 3
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #740
    dut.a.value = 4
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #741
    dut.a.value = 8
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #742
    dut.a.value = 2
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #743
    dut.a.value = 10
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #744
    dut.a.value = 15
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #745
    dut.a.value = 7
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #746
    dut.a.value = 9
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #747
    dut.a.value = 14
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #748
    dut.a.value = 2
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #749
    dut.a.value = 0
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #750
    dut.a.value = 5
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #751
    dut.a.value = 13
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #752
    dut.a.value = 3
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #753
    dut.a.value = 4
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #754
    dut.a.value = 8
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #755
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #756
    dut.a.value = 9
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #757
    dut.a.value = 4
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #758
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #759
    dut.a.value = 11
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #760
    dut.a.value = 1
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #761
    dut.a.value = 5
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #762
    dut.a.value = 14
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #763
    dut.a.value = 13
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #764
    dut.a.value = 12
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #765
    dut.a.value = 3
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #766
    dut.a.value = 3
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #767
    dut.a.value = 13
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #768
    dut.a.value = 1
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #769
    dut.a.value = 4
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #770
    dut.a.value = 8
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #771
    dut.a.value = 5
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #772
    dut.a.value = 7
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #773
    dut.a.value = 12
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #774
    dut.a.value = 9
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #775
    dut.a.value = 13
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #776
    dut.a.value = 10
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #777
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #778
    dut.a.value = 5
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #779
    dut.a.value = 8
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #780
    dut.a.value = 14
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #781
    dut.a.value = 3
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #782
    dut.a.value = 12
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #783
    dut.a.value = 7
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #784
    dut.a.value = 2
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #785
    dut.a.value = 6
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #786
    dut.a.value = 5
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #787
    dut.a.value = 12
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #788
    dut.a.value = 5
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #789
    dut.a.value = 7
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #790
    dut.a.value = 0
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #791
    dut.a.value = 8
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #792
    dut.a.value = 6
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #793
    dut.a.value = 2
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #794
    dut.a.value = 14
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #795
    dut.a.value = 12
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #796
    dut.a.value = 6
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #797
    dut.a.value = 14
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #798
    dut.a.value = 0
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #799
    dut.a.value = 15
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #800
    dut.a.value = 2
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #801
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #802
    dut.a.value = 0
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #803
    dut.a.value = 4
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #804
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #805
    dut.a.value = 4
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #806
    dut.a.value = 15
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #807
    dut.a.value = 11
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #808
    dut.a.value = 10
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #809
    dut.a.value = 0
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #810
    dut.a.value = 7
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #811
    dut.a.value = 5
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #812
    dut.a.value = 12
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #813
    dut.a.value = 15
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #814
    dut.a.value = 10
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #815
    dut.a.value = 14
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #816
    dut.a.value = 3
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #817
    dut.a.value = 3
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #818
    dut.a.value = 3
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #819
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #820
    dut.a.value = 2
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #821
    dut.a.value = 5
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #822
    dut.a.value = 11
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #823
    dut.a.value = 6
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #824
    dut.a.value = 13
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #825
    dut.a.value = 14
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #826
    dut.a.value = 3
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #827
    dut.a.value = 2
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #828
    dut.a.value = 7
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #829
    dut.a.value = 11
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #830
    dut.a.value = 0
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #831
    dut.a.value = 13
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #832
    dut.a.value = 3
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #833
    dut.a.value = 7
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #834
    dut.a.value = 8
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #835
    dut.a.value = 10
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #836
    dut.a.value = 0
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #837
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #838
    dut.a.value = 15
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #839
    dut.a.value = 1
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #840
    dut.a.value = 9
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #841
    dut.a.value = 1
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #842
    dut.a.value = 2
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #843
    dut.a.value = 11
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #844
    dut.a.value = 4
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #845
    dut.a.value = 11
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #846
    dut.a.value = 15
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #847
    dut.a.value = 8
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #848
    dut.a.value = 10
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #849
    dut.a.value = 9
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #850
    dut.a.value = 1
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #851
    dut.a.value = 13
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #852
    dut.a.value = 3
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #853
    dut.a.value = 12
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #854
    dut.a.value = 13
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #855
    dut.a.value = 15
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #856
    dut.a.value = 12
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #857
    dut.a.value = 3
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #858
    dut.a.value = 3
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #859
    dut.a.value = 9
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #860
    dut.a.value = 5
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #861
    dut.a.value = 12
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #862
    dut.a.value = 13
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #863
    dut.a.value = 7
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #864
    dut.a.value = 4
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 0
    
    # Test case #865
    dut.a.value = 10
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #866
    dut.a.value = 5
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #867
    dut.a.value = 6
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #868
    dut.a.value = 1
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 0
    
    # Test case #869
    dut.a.value = 11
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #870
    dut.a.value = 0
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #871
    dut.a.value = 5
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #872
    dut.a.value = 11
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #873
    dut.a.value = 11
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #874
    dut.a.value = 6
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #875
    dut.a.value = 7
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #876
    dut.a.value = 9
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #877
    dut.a.value = 0
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #878
    dut.a.value = 8
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #879
    dut.a.value = 14
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #880
    dut.a.value = 8
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #881
    dut.a.value = 1
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #882
    dut.a.value = 15
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #883
    dut.a.value = 6
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #884
    dut.a.value = 9
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #885
    dut.a.value = 15
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #886
    dut.a.value = 12
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #887
    dut.a.value = 6
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #888
    dut.a.value = 12
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #889
    dut.a.value = 7
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #890
    dut.a.value = 6
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #891
    dut.a.value = 14
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1
    
    # Test case #892
    dut.a.value = 1
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #893
    dut.a.value = 5
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #894
    dut.a.value = 6
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #895
    dut.a.value = 5
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #896
    dut.a.value = 11
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #897
    dut.a.value = 12
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #898
    dut.a.value = 13
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #899
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #900
    dut.a.value = 3
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #901
    dut.a.value = 0
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 0
    
    # Test case #902
    dut.a.value = 0
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #903
    dut.a.value = 8
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #904
    dut.a.value = 8
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #905
    dut.a.value = 15
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1
    
    # Test case #906
    dut.a.value = 13
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #907
    dut.a.value = 13
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #908
    dut.a.value = 12
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #909
    dut.a.value = 8
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #910
    dut.a.value = 6
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #911
    dut.a.value = 1
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #912
    dut.a.value = 4
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #913
    dut.a.value = 12
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #914
    dut.a.value = 15
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 1
    
    # Test case #915
    dut.a.value = 8
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #916
    dut.a.value = 4
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #917
    dut.a.value = 2
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #918
    dut.a.value = 15
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #919
    dut.a.value = 0
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #920
    dut.a.value = 9
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #921
    dut.a.value = 5
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #922
    dut.a.value = 14
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #923
    dut.a.value = 5
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
    
    # Test case #924
    dut.a.value = 5
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #925
    dut.a.value = 13
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #926
    dut.a.value = 10
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #927
    dut.a.value = 12
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #928
    dut.a.value = 11
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #929
    dut.a.value = 0
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #930
    dut.a.value = 1
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #931
    dut.a.value = 12
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #932
    dut.a.value = 1
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #933
    dut.a.value = 9
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #934
    dut.a.value = 9
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #935
    dut.a.value = 8
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #936
    dut.a.value = 10
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #937
    dut.a.value = 9
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #938
    dut.a.value = 0
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #939
    dut.a.value = 2
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #940
    dut.a.value = 11
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #941
    dut.a.value = 0
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #942
    dut.a.value = 13
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #943
    dut.a.value = 4
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #944
    dut.a.value = 6
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #945
    dut.a.value = 2
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #946
    dut.a.value = 13
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #947
    dut.a.value = 13
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #948
    dut.a.value = 14
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #949
    dut.a.value = 15
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 1
    
    # Test case #950
    dut.a.value = 0
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #951
    dut.a.value = 10
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #952
    dut.a.value = 6
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #953
    dut.a.value = 2
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #954
    dut.a.value = 2
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #955
    dut.a.value = 12
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #956
    dut.a.value = 4
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #957
    dut.a.value = 4
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #958
    dut.a.value = 9
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #959
    dut.a.value = 10
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 1
    
    # Test case #960
    dut.a.value = 13
    dut.b.value = 13
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 1
    
    # Test case #961
    dut.a.value = 7
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #962
    dut.a.value = 12
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #963
    dut.a.value = 8
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #964
    dut.a.value = 10
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #965
    dut.a.value = 1
    dut.b.value = 11
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #966
    dut.a.value = 0
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 0
    
    # Test case #967
    dut.a.value = 5
    dut.b.value = 6
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #968
    dut.a.value = 0
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 0
    
    # Test case #969
    dut.a.value = 12
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #970
    dut.a.value = 13
    dut.b.value = 8
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #971
    dut.a.value = 0
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 0
    
    # Test case #972
    dut.a.value = 5
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 9 and dut.carry_out.value == 0
    
    # Test case #973
    dut.a.value = 3
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 1 and dut.carry_out.value == 1
    
    # Test case #974
    dut.a.value = 13
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 1
    
    # Test case #975
    dut.a.value = 14
    dut.b.value = 10
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #976
    dut.a.value = 11
    dut.b.value = 5
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #977
    dut.a.value = 4
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 11 and dut.carry_out.value == 0
    
    # Test case #978
    dut.a.value = 9
    dut.b.value = 12
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 5 and dut.carry_out.value == 1
    
    # Test case #979
    dut.a.value = 1
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #980
    dut.a.value = 4
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #981
    dut.a.value = 14
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #982
    dut.a.value = 14
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 1
    
    # Test case #983
    dut.a.value = 10
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 8 and dut.carry_out.value == 1
    
    # Test case #984
    dut.a.value = 12
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 3 and dut.carry_out.value == 1
    
    # Test case #985
    dut.a.value = 1
    dut.b.value = 9
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 10 and dut.carry_out.value == 0
    
    # Test case #986
    dut.a.value = 15
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 0 and dut.carry_out.value == 1
    
    # Test case #987
    dut.a.value = 10
    dut.b.value = 4
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 14 and dut.carry_out.value == 0
    
    # Test case #988
    dut.a.value = 6
    dut.b.value = 14
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #989
    dut.a.value = 3
    dut.b.value = 3
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #990
    dut.a.value = 12
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 0
    
    # Test case #991
    dut.a.value = 13
    dut.b.value = 7
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 1
    
    # Test case #992
    dut.a.value = 6
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 7 and dut.carry_out.value == 0
    
    # Test case #993
    dut.a.value = 14
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 13 and dut.carry_out.value == 1
    
    # Test case #994
    dut.a.value = 13
    dut.b.value = 15
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 12 and dut.carry_out.value == 1
    
    # Test case #995
    dut.a.value = 2
    dut.b.value = 2
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 4 and dut.carry_out.value == 0
    
    # Test case #996
    dut.a.value = 1
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 2 and dut.carry_out.value == 0
    
    # Test case #997
    dut.a.value = 6
    dut.b.value = 0
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #998
    dut.a.value = 5
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 6 and dut.carry_out.value == 0
    
    # Test case #999
    dut.a.value = 14
    dut.b.value = 1
    await ClockCycles(dut.clk, 10)
    dut._log.info(f"value of outputs are: {dut.sum.value} and {dut.carry_out.value}.")
    assert dut.sum.value == 15 and dut.carry_out.value == 0
