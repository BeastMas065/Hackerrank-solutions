import re
r=r'\b(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)\b'
for _ in range(int(input())):
    s = input()
    if re.search(r,s):
        print("VALID")
    else:
        print("INVALID")