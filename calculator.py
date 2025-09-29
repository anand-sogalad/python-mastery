# Import operations first to register them
from src.calculator.calculator import Calculator
from src.calculator.core.registry import OperationRegistry

print("Calculator imported successfully!")

# Check what's registered
registry = OperationRegistry.get_registry()
print(f"Registered operations: {list(registry.keys())}")
print(f"Registry contents: {registry}")

# Test the calculator
calc = Calculator()
print("Calculator instance created!")

# Try a simple operation
try:
    result = calc.run_operation("add", 5, 3)
    print(f"✅ 5 + 3 = {result}")
except Exception as e:
    print(f"❌ Error: {e}")

# Try another operation
try:
    result = calc.run_operation("multiply", 4, 6)
    print(f"✅ 4 * 6 = {result}")
except Exception as e:
    print(f"❌ Error: {e}")
