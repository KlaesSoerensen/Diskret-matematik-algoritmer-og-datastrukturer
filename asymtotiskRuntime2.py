import ast

def calculate_complexity(code):
    tree = ast.parse(code)
    visitor = ComplexityVisitor()
    visitor.visit(tree)
    return visitor.complexity

class ComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.complexity = None
    
    def visit_For(self, node):
        self.complexity = 'O(n^2)'
    
    def visit_While(self, node):
        self.complexity = 'O(n)'
    
    def visit_Call(self, node):
        func_name = node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id
        if func_name == 'range':
            args = [0, 0, 1]  # default arguments for range function
            if len(node.args) > 0:
                args[0] = self._get_constant_value(node.args[0])
            if len(node.args) > 1:
                args[1] = self._get_constant_value(node.args[1])
            if len(node.args) > 2:
                args[2] = self._get_constant_value(node.args[2])
            
            start, stop, step = args
            if start == 0 and step == 1:
                if stop == 1:
                    self.complexity = 'O(1)'
                elif stop > 1:
                    if self.complexity == 'O(1)':
                        self.complexity = 'O(n)'
                    else:
                        self.complexity = 'O(n log n)'
    
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Mult):
            left = self._get_constant_value(node.left)
            right = self._get_constant_value(node.right)
            if left is not None and right is not None:
                if left == 1 and right == 1:
                    self.complexity = 'O(n^3)'
        elif isinstance(node.op, ast.Add):
            left = self._get_constant_value(node.left)
            right = self._get_constant_value(node.right)
            if left is not None and right is not None:
                if left == 1 and right == 1:
                    self.complexity = 'O(n)'
    
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Mult):
            left = self._get_constant_value(node.left)
            right = self._get_constant_value(node.right)
            if left is not None and right is not None:
                if left == 1 and right == 1:
                    self.complexity = 'O(n^3)'
        elif isinstance(node.op, ast.Add):
            left = self._get_constant_value(node.left)
            right = self._get_constant_value(node.right)
            if left is not None and right is not None:
                if left == 1 and right == 1:
                    self.complexity = 'O(n)'
        elif isinstance(node.op, ast.Sub):
            left = self._get_constant_value(node.left)
            right = self._get_constant_value(node.right)
            if left is not None and right is not None:
                if left == 1 and right == 1:
                    self.complexity = 'O(n)'
        elif isinstance(node.op, ast.Pow):
            left = self._get_constant_value(node.left)
            right = self._get_constant_value(node.right)
            if left is not None and right is not None:
                if left == 2 and right == 1:
                    self.complexity = 'O(2^n)'
    
    def visit_Compare(self, node):
        if isinstance(node.ops[0], ast.Lt):
            left = self._get_constant_value(node.left)
            right = self._get_constant_value(node.comparators[0])
            if left is not None and right is not None:
                if left == 1 and right == 1:
                    self.complexity = 'O(log n)'
        elif isinstance(node.ops[0], ast.LtE):
            left = self._get_constant_value(node.left)
            right = self._get_constant_value(node.comparators[0])
            if left is not None and right is not None:
                if left == 1 and right == 1:
                    self.complexity = 'O((log n)^2)'
    
    def _get_constant_value(self, node):
        if isinstance(node, ast.Constant):
            return node.value
        return None
    
    def generic_visit(self, node):
        if self.complexity is None:
            super().generic_visit(node)
    
    def unsupported(self):
        self.complexity = 'Unsupported'

pseudocode = '''
n  =len(n)
    i = 1
    while i<= n:
        i = i+i

'''

complexity = calculate_complexity(pseudocode)
print("The running time complexity is:", complexity)
