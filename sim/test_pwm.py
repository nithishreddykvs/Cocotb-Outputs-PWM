import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def pwm_test(dut):
    """Simple PWM Test with new assignment syntax"""

    # Initialize signals
    dut.clk.value = 0
    dut.rst.value = 1        # assert reset

    # Hold reset for a few clock cycles
    for _ in range(5):
        dut.clk.value = 0
        await Timer(5, units='ns')
        dut.clk.value = 1
        await Timer(5, units='ns')

    # Release reset and set duty-cycle switches
    dut.rst.value = 0        # deassert reset
    dut.sw.value  = 0b100    # set 50% duty cycle (sw = 4)

    # Run for additional clock cycles
    for _ in range(20):
        dut.clk.value = 0
        await Timer(5, units='ns')
        dut.clk.value = 1
        await Timer(5, units='ns')

    # Log the PWM output
    cocotb.log.info(f"Final PWM output: {int(dut.pwm_out.value)}")
