"""Module de demo heritage multiple super avec arguments."""


class First:
    """Classe premier niveau."""

    def __init__(self, *args, **kwargs):
        """Methode d"initialisation."""
        self.first_arg = kwargs.pop('first_arg')
        super().__init__(*args, **kwargs)


class Second(First):
    """Classe second niveau."""

    def __init__(self, *args, **kwargs):
        """Methode d"initialisation."""
        self.second_arg = kwargs.pop('second_arg')
        super().__init__(*args, **kwargs)


class Third(Second):
    """Classe troisième niveau."""

    def __init__(self, *args, **kwargs):
        """Methode d"initialisation."""
        self.third_arg = kwargs.pop('third_arg')
        super().__init__(*args, **kwargs)


third = Third(first_arg=1, second_arg=2, third_arg=3)
