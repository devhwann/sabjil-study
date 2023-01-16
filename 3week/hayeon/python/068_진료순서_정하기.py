def solution(emergency):
    return [len(emergency) - sorted(emergency).index(e) for e in emergency]
