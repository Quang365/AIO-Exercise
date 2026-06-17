import math

def f1_score(tp, fp, fn):
    if not isinstance(tp, int):
        print("tp must be int")
        return

    if not isinstance(fp, int):
        print("fp must be int")
        return

    if not isinstance(fn, int):
        print("fn must be int")
        return

    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp, fp, and fn must be greater than or equal to 0")
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return f1_score

assert round(f1_score(tp=2, fp=3, fn=5), 2) == 0.33
print(f1_score(tp=2, fp=3, fn=5))
