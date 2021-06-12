import numpy as np
import pytest

from tvm import relay
from tvm.contrib import coverage
from multiprocessing import Process, Manager

def func(cov_collect):
    out_channels = 16
    batch_size = 1

    data = relay.var("data", relay.TensorType((batch_size, 3, 224, 224), "float32"))
    weight = relay.var("weight")
    relay.nn.conv2d(
        data=data, weight=weight, kernel_size=(3, 3), channels=out_channels, padding=(1, 1)
    )

    cov_collect.append(coverage.get_now())
    cov_collect.append(coverage.get_total())
    cov_collect.append(coverage.get_hitmap())

def test_mp():
    main_now = coverage.get_now()
    main_total = coverage.get_total()
    hitmap_array = np.array(coverage.get_hitmap())
    assert hitmap_array.sum() == coverage.get_now()

    with Manager() as manager:
        cov_collect = manager.list()
        
        p = Process(target=func, args=(cov_collect,))
        p.start()
        p.join()

        coverage.set_now(cov_collect[0])
        assert main_total == cov_collect[1]
        coverage.set_hitmap(cov_collect[2])
    
    new_cov_percent = coverage.get_now() / coverage.get_total()
    old_cov_percent = main_now / main_total
    assert new_cov_percent > old_cov_percent
    
    hitmap_array = np.array(coverage.get_hitmap())
    assert hitmap_array.sum() == coverage.get_now()

    coverage.reset()
    assert coverage.get_now() == 0

if __name__ == '__main__':
    test_mp()
