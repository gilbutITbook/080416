class LinearCongruentialGenerator:
    def __init__(self, seed: int = 123):
        self.__seed: int = seed
        self._multiplier: int = 1103515245
        self._modulus: int = 2**32
        self._increment: int = 1

        # 따라야 할 간단한 규칙들
        assert 0 < self._modulus
        assert 0 < self._multiplier < self._modulus
        assert 0 <= self._increment < self._modulus
        assert 0 <= seed < self._modulus

        # 반복 관계의 초기 적용
        self._state = (
            (self._multiplier * self.__seed + self._increment)
            % self._modulus)

    @property
    def seed(self):
        return self.__seed

    def next(self):
        # 상태 증가
        self._state = (
            (self._multiplier * self._state + self._increment)
            % self._modulus)
        return self._state / self._modulus


def lcg(
    seed: int = 123,
    multiplier: int = 1_103_515_245,
    modulus: int = 2**32,
    increment: int = 1
):
    # 따라야 할 간단한 규칙들
    assert 0 < modulus
    assert 0 < multiplier < modulus
    assert 0 <= increment < modulus
    assert 0 <= seed < modulus

    # 반복 관계의 초기 적용
    state = (multiplier * seed + increment) % modulus

    while True:
        state = (multiplier * state + increment) % modulus
        yield state / modulus
