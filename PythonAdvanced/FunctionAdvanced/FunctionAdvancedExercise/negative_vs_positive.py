def printer(negatives, positives):
    print(sum(negatives))
    print(sum(positives))
    if abs(sum(negatives)) > sum(positives):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


def spliter(*args):
    negatives = []
    positives = []
    for num in args:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)
    printer(negatives, positives)


line = [int(x) for x in input().split()]

spliter(*line)
