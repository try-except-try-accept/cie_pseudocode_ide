def MID(string, index, num_chars):
  """Implementation of CAIE's psuedocode MID function"""
  return string[index:index+num_chars]
  
def LENGTH(string):
  """Implementation of CAIE's psuedocode LENGTH function"""
  return len(string)
  
def LEFT(string, num_chars):
  """Implementation of CAIE's psuedocode LEFT function"""
  return string[:num_chars]
  
def RIGHT(string, num_chars):
  """Implementation of CAIE's psuedocode RIGHT function"""
  return string[0-num_chars:]

def INT(real):
  """Implementation of CAIE's psuedocode INT function"""
  return int(real)

def NUM_TO_STRING(num):
  """Implementation of CAIE's psuedocode NUM_TO_STRING function"""
  return str(num)
  
def STRING_TO_NUM(string):
  """Implementation of CAIE's psuedocode STRING_TO_NUM function"""
  return int(string)
  


## OUTPUT LENGTH("Hello")
print(LENGTH("hello"))