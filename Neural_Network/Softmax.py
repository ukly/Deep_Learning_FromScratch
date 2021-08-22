def softmax(a):        #수식 그대로의 softmax함수
  exp_a = np.exp(a)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  
  return y

def edited_softmax(a):     #오버플로우를 방지할 수 있는 softmax함수
  c = np.max(a)
  exp_a = np.exp(a-c)
  sum_exp_a = np.sum(exp_a)
  y  = exp_a / sum_exp_a
  
  return y
