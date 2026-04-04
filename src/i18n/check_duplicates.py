import ast
from collections import Counter


FILE_PATH = "src/controller/translations.py"

def key_to_text(node):
    if isinstance(node, ast.Constant):
        return repr(node.value)
    return ast.unparse(node) if hasattr(ast, "unparse") else None


with open(FILE_PATH, "r", encoding="utf-8") as f:
    source = f.read()

tree = ast.parse(source, filename=FILE_PATH)

found = False

for node in ast.walk(tree):
    if isinstance(node, ast.Dict):
        keys = [key_to_text(k) for k in node.keys if k is not None]
        counts = Counter(keys)
        duplicates = [k for k, c in counts.items() if c > 1]

        if duplicates:
            found = True
            print("Duplicate keys found:")
            for dup in duplicates:
                print(f"  {dup} -> {counts[dup]} times")

if not found:
    print("No duplicate keys found.")