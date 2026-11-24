import io, unittest
from pvm import Lexer, Parser, Compiler, MiniPVM, run_source, disassemble
from pvm.opcodes import Opcode as O
from pvm.parser import Program, AssignStmt, IfStmt
class PVMTests(unittest.TestCase):
    def execute(self,src):
        out=io.StringIO(); env=run_source(src,stdout=out); return out.getvalue(),env
    def test_lexer(self):
        ts=Lexer('x = 12\nlikho("hi")').tokenize()
        self.assertIn("NUMBER",[t.type for t in ts]); self.assertIn("KEYWORD",[t.type for t in ts])
    def test_parser(self):
        tree=Parser(Lexer("x = 1\n").tokenize()).parse()
        self.assertIsInstance(tree,Program); self.assertIsInstance(tree.statements[0],AssignStmt)
    def test_arithmetic(self):
        out,env=self.execute("x = 8 - 3 * 2\nlikho(x)\n")
        self.assertEqual(out,"2\n")
    def test_while(self):
        out,env=self.execute("i=1\nt=0\njabtak i<=5:\n    t=t+i\n    i=i+1\nlikho(t)\n")
        self.assertEqual(out,"15\n")
    def test_if_elif_else(self):
        out,_=self.execute('x=8\nagar x<5:\n    likho("a")\nwarna agar x<10:\n    likho("b")\nwarna:\n    likho("c")\n')
        self.assertEqual(out,"b\n")
    def test_for_loop(self):
        out,_=self.execute("t=0\nhar i mein range(1,4):\n    t=t+i\nlikho(t)\n")
        self.assertEqual(out,"6\n")
    def test_stdout_and_dialect(self):
        out,_=self.execute('agar sahi:\n    likho("yes")\n')
        self.assertEqual(out,"yes\n")
    def test_jumps_and_halt(self):
        code=Compiler().compile(Parser(Lexer("x=1\nagar x:\n    likho(x)\n").tokenize()).parse())
        self.assertEqual(code[-1].opcode,O.HALT)
        for ins in code:
            if ins.opcode in (O.POP_JUMP_IF_FALSE,O.POP_JUMP_IF_TRUE,O.JUMP_ABSOLUTE):
                self.assertGreaterEqual(ins.arg,0); self.assertLessEqual(ins.arg,len(code))
    def test_disassembler(self):
        text=disassemble(Compiler().compile(Parser(Lexer("x=1\n").tokenize()).parse()))
        self.assertIn("ADDR",text); self.assertIn("LOAD_CONST",text)
if __name__=="__main__": unittest.main()
