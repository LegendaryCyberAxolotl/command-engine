from dataclasses import dataclass, field

@dataclass
class Context:
    variables: dict[str, str | None] = field(default_factory=dict)
    history: list[str] = field(default_factory=list)
    VERSION: str = "Alpha 1"
    DEFAULT_SIGN = ">> "
    SIGN = DEFAULT_SIGN
    running: bool = True

    def setSIGN(self, sign: str):
        self.SIGN = f"{sign} "