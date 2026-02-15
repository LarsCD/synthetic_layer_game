import time

def usleep(microseconds):
    """
    high precision waiting function, used for rendering individual characters of displays fast
    """
    # high precision busy wait
    start = time.perf_counter_ns()
    deadline = start + (microseconds * 1000)
    while time.perf_counter_ns() < deadline:
        pass # Spin
