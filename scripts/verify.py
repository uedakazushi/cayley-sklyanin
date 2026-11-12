"""Check each manuscript independently; not a mathematical proof verifier."""
from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parents[1]
reports=[]
for entry in ['papers/cayley-sklyanin.tex','papers/central_fiber_discriminant.tex']:
    seen={}
    def visit(n):
        p=(R/n).resolve()
        assert p.is_relative_to(R)
        if n in seen:return
        t=re.sub(r'(?<!\\)%[^\n]*','',p.read_text());seen[n]=t
        for q in re.findall(r'\\input\{([^}]+)\}',t):visit(q if q.endswith('.tex') else q+'.tex')
    visit(entry)
    t='\n'.join(seen.values());labels=re.findall(r'\\label\{([^}]+)\}',t);refs=re.findall(r'\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}',t);bib=re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}',t);cites=[x.strip() for g in re.findall(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}',t) for x in g.split(',')]
    assert len(labels)==len(set(labels));assert len(bib)==len(set(bib));assert not set(refs)-set(labels),set(refs)-set(labels);assert not set(cites)-set(bib),set(cites)-set(bib)
    reports.append({'entry':entry,'tex_inputs':len(seen),'labels':len(labels),'references':len(refs),'citations':len(cites),'bibitems':len(bib),'sha256':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in seen}})
(R/'build').mkdir(exist_ok=True);(R/'build/source_check.json').write_text(json.dumps(reports,indent=2)+'\n');print(json.dumps(reports,indent=2))
