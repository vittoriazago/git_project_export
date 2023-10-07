class UnexpectedResponseStatus(Exception):
    def __init__(self, expected: int, actual: int) -> None:
        self.expected = expected
        self.actual = actual
        self.msg = f"Status {actual} não esperado. O esperado era {expected}"
        super().__init__(self.msg)
