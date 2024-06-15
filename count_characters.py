def count_char(text):
      dic = {}
      for t in text:
            if t != " ":
                  if t in dic:
                        dic[t] += 1
                  else:
                        dic[t] = 1
      return dic

print(count_char("python is programming language"))