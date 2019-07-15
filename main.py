#!/usr/bin/env python3

from precise_runner import PreciseEngine, PreciseRunner

engine = PreciseEngine('.venv/bin/precise-engine', 'hey-mycroft-2.pb')
runner = PreciseRunner(engine, on_activation=lambda: print('hello'))
runner.start()
