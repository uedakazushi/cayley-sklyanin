# Cayley三次曲面とSklyanin代数

2026-11-13 / v1。主論文は `papers/cayley-sklyanin.tex`。補助論文 `papers/central_fiber_discriminant.tex` は中心曲面の必要十分判別式と特異点の証明を保持する。

主論文は全中心・次数18関係、Azumaya locus、四つの非可換A1模型・Brauer指数6のtwisted NCCR、21中心特異点と3ホモロジー的特異点、Karoubi特異圏三因子、量子的判別式と球面twistを扱う。斉次Sklyaninの既知中心定理と厳密有理数検算を区別する。

```sh
latexmk papers/cayley-sklyanin.tex
latexmk papers/central_fiber_discriminant.tex
python3 scripts/verify.py
python3 computations/verify_center_phi_exact.py --backend flint --run-all --verify --state-dir build/phi-state
```

日本語LuaLaTeX・LuaTeX-ja・HaranoAji・latexmk、Python3・SymPyを用いる。重い有理数検算の高速backendはpython-flint（標準Fraction版も保持）。PDF・SyncTeX・計算状態はbuild/で非追跡。VS Codeの既定LaTeX Workshop recipeを使える。Actions・force pushなし。
