from typing import Callable, Any
from functools import reduce, lru_cache, singledispatch
from functools import partial
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    try:
        operations = {
            "add" : operator.add,
            "max" : max,
            "min" : min,
            "multiply" : operator.mul
        }
        return reduce(operations[operation], spells)
    except:
        print("error: operation is unknow,")
    
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire" : partial(base_enchantment, 50, "fire"),
        "ice" : partial(base_enchantment, 50, "ice"),
        "lightning" : partial(base_enchantment, 50, "lightning"),
        }

@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def spell(x: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(x: int) -> str:
        return f"{x} damage"

    @spell.register(str)
    def _(x: str) -> str:
        return f"{x}"

    @spell.register(list)
    def _(x: list) -> str:
        return f"{len(x)} spells"

    return spell


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    spell_powers = [13, 23, 25, 19, 20]
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    spell_powers = [2, 2, 2, 3, 10000]
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    spell_powers = [23, 25, 5, 40]
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    # print(spell_reducer([1,2,3], "add"))
    
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("\nTesting spell dispatcher...")
    test_spell = spell_dispatcher()
    print(f"Damage spell: {test_spell(42)}")
    print(f"Enchantment: {test_spell('fireball')}")
    print(f"Multi-cast: {test_spell([1,2,3])}")
    print(test_spell({"key": "value"}))