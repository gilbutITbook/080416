def bad_lcg(
    seed: int = 123,
    multiplier: int = 1_103_515_245,
    modulus: int = 2**32,
    increment: int = 1
):
    # 매개 변수가 잘못된 경우 LCG 알고리즘을 적용하지 않음
    try:
        assert 0 < modulus
        assert 0 < multiplier < modulus
        assert 0 <= increment < modulus
        assert 0 <= seed < modulus

        # 반복 관계의 초기 적용
        state = (multiplier * seed + increment) % modulus

        while True:
            state = (multiplier * state + increment) % modulus
            yield state / modulus

    except AssertionError:
        import random
        while True:
            yield random.random()


if __name__ == '__main__':
    for x, _ in zip(bad_lcg(multiplier=-1), range(5)):
        print(x)
