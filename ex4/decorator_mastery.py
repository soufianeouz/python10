# def power_validator(min_power):
#     def decorator(func):
#         def wrapper(power):
#             if power >= min_power:
#                 return func(power)
#             else:
#                 return "Insufficient power"
#         return wrapper
#     return decorator


# @power_validator(10)
# def fireball(power):
#     return "yaw"

# print(fireball(5))

from typing import Callable
import time

def spell_timer(func: Callable) -> Callable:
    def wrapper():
        start = time.time()
        print("Casting function_name...")
        end = time.time()
        return end - start
    return wrapper
def power_validator(min_power: int) -> Callable:
    pass

def retry_spell(max_attempts: int) -> Callable:
    pass

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass
def func():
    pass

if __name__ == "__main__":
    a = spell_timer(func)
    print(f"Spell completed in {a():.2f} seconds")