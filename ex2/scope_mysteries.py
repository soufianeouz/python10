from typing import Callable


def mage_counter() -> Callable:
    counter = 0

    def call_counter():
        nonlocal counter
        counter += 1
        return counter

    return call_counter
    

def spell_accumulator(initial_power: int)-> Callable:
    def accumulator(amount: int):
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str)-> Callable:
    def enchant(item_name):
        return f"{enchantment_type} {item_name}"
    return enchant

def memory_vault()-> dict[str, Callable]:
    memory = {}
    def store (key, value):
        memory[key] = value
    def recall(key):
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"
    return {"store" : store, "recall" : recall}


if __name__ == "__main__":
    
    print("Testing mage counter...")
    counter_a = mage_counter()
    for i in range(2):
        a = counter_a()
        print(f"counter_a call {i + 1}: {a}")
        
    counter_b = mage_counter()
    b = counter_b()
    print(f"counter_b call 1: {b}")
    
    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    res = accumulator(20)
    print(f"Base 100, add 20: {res}")
    res = accumulator(30)
    print(f"Base 100, add 20: {res}")
    
    print("\nTesting enchantment factory...")
    enchantment1 = enchantment_factory("Flaming")
    print(enchantment1("Sword"))
    enchantment2 = enchantment_factory("Frozen")
    print(enchantment2("Shield"))
    
    print("\nTesting memory vault...")
    vault_test = memory_vault()
    store = vault_test["store"]
    recall = vault_test["recall"]
    store("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall("secret")}")
    print(f"Recall 'unknown': {recall("unknown")}")