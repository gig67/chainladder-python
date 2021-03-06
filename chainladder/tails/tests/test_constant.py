import chainladder as cl
import numpy as np
from chainladder.utils.cupy import cp


def test_constant_balances():
    raa = cl.load_dataset('quarterly')
    xp = cp.get_array_module(raa.values)
    assert round(float(xp.prod(cl.TailConstant(1.05, decay=0.8)
                     .fit(raa).ldf_.iloc[0, 1].values[0, 0, 0, -5:])),3) == 1.050
