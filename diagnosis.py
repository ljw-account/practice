def analyze_scores(scores):
    highest = 0
    lowest = 100
    count = 0
    total = 0
    for score in scores:
        score = int(score)
        if highest < score:
            highest = score
        if lowest > score:
            lowest = score
        if score >= 60:
            count += 1
        total += score
    average = total / len(scores)
    score_ana = {"average" : average, "highest" : highest, "lowest" : lowest, "passed" : count}
    return (score_ana)

try:
    with open("scores.txt", "r", encoding="utf-8") as f:
        scores = f.read()
        scores_list = scores.split("\n")
        result = analyze_scores(scores_list)
        print(result)
except FileNotFoundError as e:
    print("找不到成績檔案")
    