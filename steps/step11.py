import numpy as np


class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError('{} is not supported'.format(type(data)))

        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)

        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            x, y = f.input, f.output
            x.grad = f.backward(y.grad)

            if x.creator is not None:
                funcs.append(x.creator)


def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x


class Function:
    def __call__(self, inputs):
<<<<<<< HEAD
        xs = [x.data for x in inputs]  # Get data from Variable
        ys = self.forward(xs)
        outputs = [Variable(as_array(y)) for y in ys]  # Wrap data

        for output in outputs:
            output.set_creator(self)
=======
        # 인수와 반환값을 리스트로 변경
        # x = input.data
        # y = self.forward(x)
        xs = [x.data for x in inputs]
        ys = self.forward(xs)
        # output = Variable(as_array(y))
        outputs = [Variable(as_array(y)) for y in ys]
        # output.set_creator(self)

        for output in outputs:
            output.set_creator(self)

>>>>>>> d7c276b433519f1fe6939a7d1b4fb5516ef8f332
        self.inputs = inputs
        self.outputs = outputs
        return outputs

<<<<<<< HEAD
    def forward(self, xs):
        raise NotImplementedError()

    def backward(self, gys):
        raise NotImplementedError()


=======
    def forward(self, x):
        raise NotImplementedError()

    def backward(self, gy):
        raise NotImplementedError()

>>>>>>> d7c276b433519f1fe6939a7d1b4fb5516ef8f332
class Add(Function):
    def forward(self, xs):
        x0, x1 = xs
        y = x0 + x1
<<<<<<< HEAD
        return (y,)


xs = [Variable(np.array(2)), Variable(np.array(3))]
f = Add()
ys = f(xs)
y = ys[0]
print(y.data)
=======
        return (y, )

def main():
    xs = [Variable(np.array(2)), Variable(np.array(3))] # 리스트로 준비
    f = Add()
    ys = f(xs)
    y = ys[0]
    print(y.data)

if __name__ =="__main__":
    main()
>>>>>>> d7c276b433519f1fe6939a7d1b4fb5516ef8f332
