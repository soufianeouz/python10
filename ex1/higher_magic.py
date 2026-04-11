from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable)-> Callable:
    def new_spells(target: str, power: int):
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return f"Combined spell result: {res1}, {res2}"
    return new_spells


def power_amplifier(base_spell: Callable, multiplier: int)-> Callable:
    def mega_fireball(target, power):
        old_pow = power
        power = power * multiplier
        print(f"Original: {old_pow}, Amplified: {power}")
        return base_spell(target, power)
    return mega_fireball
        

def conditional_caster(condition: Callable, spell: Callable)-> Callable:
    def new_spell(target, power):
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return new_spell

def spell_sequence(spells: list[Callable])-> Callable:
    def call_spell(target, power):
        results = []
        for spell in spells:
            tmp = spell(target, power)
            results.append(tmp)
        return results
    return call_spell

if __name__ == "__main__":
    print("\nTesting spell combiner...")
    
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits Dragon"
    
    def Heals(target: str, power: int) -> str:
        return f"Heals Dragon"
    
    a = spell_combiner(fireball, Heals)
    print(a("Dragon", 10))
    
    print("\nTesting power amplifier...")
    b = power_amplifier(fireball, 3)
    b("target", 3)