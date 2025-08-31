from abc import ABC, abstractmethod
import secrets
import string
from dataclasses import dataclass
from mnemonic import Mnemonic


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass

@dataclass
class RandomPasswordGenerator(PasswordGenerator):
    length: int = 16
    use_upper: bool = True
    use_lower: bool = True
    use_digits: bool = True
    use_symbols: bool = True

    secure: bool = True  # use secrets
    

    def _charset(self) -> str:

        cs = ""
        if self.use_lower: cs += string.ascii_lowercase
        if self.use_upper: cs += string.ascii_uppercase
        if self.use_digits: cs += string.digits
        if self.use_symbols: cs += string.punctuation
        if not cs:
            cs = string.ascii_letters
        return cs

    def generate(self) -> str:
        chars = self._charset()
        # use secrets.choice for cryptographic randomness
        return ''.join(secrets.SystemRandom().choice(chars) for _ in range(self.length))

@dataclass
class PinGenerator(PasswordGenerator):
    length: int = 6
    allow_leading_zero: bool = True
    def generate(self) -> str:
        if self.allow_leading_zero:
            return ''.join(secrets.choice(string.digits) for _ in range(self.length))
        else:
            return str(secrets.randbelow(10**self.length - 10**(self.length-1)) + 10**(self.length-1))

@dataclass
class PassphraseGenerator(PasswordGenerator):
    strength: int = 256
    words: int = 4
    separator: str = '-'
    language:str = "english"

    def generate(self) -> str:
        mnemo = Mnemonic(self.language)
        full_phrase = mnemo.generate(strength=self.strength).split()
        selected_words = full_phrase[:self.words]
        return self.separator.join(selected_words)

    

class GeneratorFactory:
    @staticmethod
    def create(kind: str, **kwargs) -> PasswordGenerator:
        kind = kind.lower()
        if kind == "pin":
            return PinGenerator(**kwargs)
        elif kind == "passphrase":
            return PassphraseGenerator(**kwargs)
        else:
            # default: random
            return RandomPasswordGenerator(**kwargs)




