import numpy as np

<<<<<<< HEAD

=======
>>>>>>> d7c276b433519f1fe6939a7d1b4fb5516ef8f332
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
<<<<<<< HEAD
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)
        if not isinstance(ys, tuple):
            ys = (ys,)
=======
    def __call__(self, *inputs): # * 추가: 리스트 사용 대신, 임의 개수의 인수를 건네어 함수 호출 가능
        xs = [x.data for x in inputs]
        # ys = self.forward(xs)
        ys = self.forward(*xs) # 별표를 붙여 언팩
        if not isinstance(ys, tuple): # 튜플이 아닌 경우에도 추가적으로 지원해줌
            ys = (ys, )
>>>>>>> d7c276b433519f1fe6939a7d1b4fb5516ef8f332
        outputs = [Variable(as_array(y)) for y in ys]

        for output in outputs:
            output.set_creator(self)
<<<<<<< HEAD
        self.inputs = inputs
        self.outputs = outputs
        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, xs):
        raise NotImplementedError()

    def backward(self, gys):
        raise NotImplementedError()


=======

        self.inputs = inputs
        self.outputs = outputs
        # return outputs
        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, x):
        raise NotImplementedError()

    def backward(self, gy):
        raise NotImplementedError()

>>>>>>> d7c276b433519f1fe6939a7d1b4fb5516ef8f332
class Add(Function):
    def forward(self, x0, x1):
        y = x0 + x1
        return y

<<<<<<< HEAD

def add(x0, x1):
    return Add()(x0, x1)


x0 = Variable(np.array(2))
x1 = Variable(np.array(3))
y = add(x0, x1)
print(y.data)
=======
def add(x0, x1):
    return Add()(x0, x1)

def main():
    # xs = [Variable(np.array(2)), Variable(np.array(3))] # 리스트로 준비
    x0 = Variable(np.array(2))
    x1 = Variable(np.array(3))
    # f = Add()
    y = add(x0, x1)
    # y = ys[0]
    print(y.data)

if __name__ =="__main__":
    main()
>>>>>>> d7c276b433519f1fe6939a7d1b4fb5516ef8f332
