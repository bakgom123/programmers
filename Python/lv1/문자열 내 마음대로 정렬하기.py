def solution(strings, n):
    return sorted(strings, key=lambda chars: (chars[n], chars))
