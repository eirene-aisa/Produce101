TRAINEE = 35

def main():
  play_list = open("playLists_2017_06_08_22-30-00.txt", "r", encoding="UTF-8")
  trainees = play_list.readlines()

  rank_heart = []
  for tr in trainees:
    l = tr.strip().split(", ")
    rank_heart.append([l[0], l[1], int(l[2]), int(l[3])])

  rank_heart = sorted (rank_heart, key=lambda a: a[3], reverse=True)
  rank_hits = sorted (rank_heart, key=lambda a: a[2], reverse=True)

  for i in range(TRAINEE):
    print(str(i + 1) + ".")
    print(rank_heart[i][0], end='')
    print("\t♥ : " + str(rank_heart[i][3]))
    print(rank_hits[i][0], end='')
    print("\thits : " + str(rank_hits[i][2]))

if __name__ == "__main__":
  main()