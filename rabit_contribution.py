import operator as op

def cnt_nick(filename):
  commenters = open(filename, 'r', encoding="UTF-8").read().splitlines()
  rabits = {}
  for c in commenters:
    if c in rabits:
      rabits[c] += 1
    else:
      rabits[c] = 1

  rabits = sorted(rabits.items(), key=op.itemgetter(1), reverse=True)
  i = 1
  for rabit in rabits:
    print("{}.\t {}\t {}번".format(i, rabit[0], rabit[1]))
    i += 1

def main():
  cnt_nick("commenters6_12_17-32.txt")

if __name__ == "__main__":
  main()