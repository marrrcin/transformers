class ConstantReplacementScheduler:
    def __init__(self, module, replacing_rate, replacing_steps=None):
        self.module = module
        self.replacing_rate = replacing_rate
        self.replacing_steps = replacing_steps
        self.step_counter = 0
        self.module.set_replacing_rate(replacing_rate)

    def step(self):
        self.step_counter += 1
        if self.replacing_steps is None or self.replacing_rate == 1.0:
            return self.replacing_rate
        else:
            if self.step_counter >= self.replacing_steps:
                self.module.set_replacing_rate(1.0)
                self.replacing_rate = 1.0
            return self.replacing_rate


class LinearReplacementScheduler:
    def __init__(self, module: BertEncoder, base_replacing_rate, k):
        self.module = module
        self.base_replacing_rate = base_replacing_rate
        self.step_counter = 0
        self.k = k
        self.module.set_replacing_rate(base_replacing_rate)

    def step(self):
        self.step_counter += 1
        current_replacing_rate = min(self.k * self.step_counter + self.base_replacing_rate, 1.0)
        self.module.set_replacing_rate(current_replacing_rate)
        return current_replacing_rate