# mock
## mock 是什么？

mock的意思是虚假的、模拟的。 在Python的单元测试中，由于一切都是对象（object）。 
而mock的技术，就是在测试时，不修改源码的前提下，替换某些对象，模拟测试环境。

比方说，一个函数里，调用了三个函数。 只需要测试这三个函数是否被依次调用即可，而无需测试真实的调用修改。

~~~
from https://note.qidong.name/2018/02/pytest-mock/
~~~

## 应用场景
大型项目的单元测试