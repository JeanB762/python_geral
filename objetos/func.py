class func:
  def __init__(self, val):
    self.val = val

  def __call__(self):
    print(self.val)


f = func('Hello world')

f()