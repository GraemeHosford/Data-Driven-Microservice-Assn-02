def stringlength(event, context):
  input_str = str(event['data'])
  str_len = len(input_str)
  return str(str_len)
