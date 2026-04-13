import time
from functools import wraps
from typing import Any, Callable


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(
    min_power: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs["power"]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts + 1:
                        return (
                            f"Spell casting failed after"
                            f" {max_attempts} attempts"
                            )
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
                    attempt += 1

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and all(c.isalpha() or c.isspace() for c in name)
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball(*args: Any, **kwargs: Any) -> str:
        return "Fireball cast!"

    print(f"Result: {fireball('ppp')}")

    @power_validator(10)
    def dargon(*args: Any, **kwargs: Any) -> str:
        return "power is sufficient for this spell"

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def retrying(*args: Any, **kwargs: Any) -> str:
        args[0] * args[0]
        return "Waaaaaaagh spelled !"

    retrying("str")
    print(retrying(3))

    print("\nTesting MageGuild...")
    instance = MageGuild()
    print(instance.validate_mage_name("str"))
    print(instance.validate_mage_name("st89r"))
    print(instance.cast_spell(spell_name='Lightning', power=15))
    print(instance.cast_spell(spell_name='Lightning', power=7))
