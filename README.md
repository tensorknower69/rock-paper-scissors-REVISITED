# rock-paper-scissors-REVISITED
Rock paper scissors but without if else just a single formula

formula:
```
f(a,b) = (b⨯a)·(1-a-b)
```
numpy:
```python
np.dot(np.cross(b, a), 1 - a - b)
```
where
- `[1, 0, 0]` means rock.
- `[0, 1, 0]` means paper.
- `[0, 0, 1]` means scissors.
- `a` is your hand.
- `b` is the opponent's hand.
- `f(a,b) = 1` means you win.
- `f(a,b) = 0` means a draw.
- `f(a,b) = -1` means you lose.

## Thought Process
If you think for a while, you may see that `f` is anticommutative:
```
f(a,b) = -f(b,a)
```

And if `a` equals `b` then
```
f(a,b) = 0
```

It looks hell alike cross product, it has to be at play.

However, it can't just be a cross-product, as the result of `f(a,b)` is a scalar. Therefore, in order to damp the cross product'd result down to a scalar. A linear transformation from `1x3` (e.g. rock ⨯ paper) to `1x1` (e.g. lose: `-1`) has to exist, so a dot product is somehow used as well.

After that, I played around with my fingers and wrote the python code to test different formulae. Eventually, I found out that the result of the cross product has some relationship with the 3D vector of the unused hand, say `m`:
```
f(a,b) = (b⨯a)·m
```

Doesn't it look pretty much the same as the true formula? What's left is to express `m` in terms of `a` and `b`. Thinking for a bit, you can see the following is true:

```
m = 1-a-b
```

It doesn't matter when `a` equals `b`, `m` becomes some weird vector as in `f(a,b) = (b⨯a)·m`, `(b⨯a)` is 0, and collapses the entire formula into 0 (a draw), which is what we want.

Substituting it in, you will get the true formula:

```
f(a,b) = (b⨯a)·(1-a-b)
```

### Some sanity check:

`f(x,x) = 0` (a draw):
```
f(x,x)
= (x⨯x)·(1-x-x)
= 0·(1-x-x)
= 0
```

Anticommutativity (`f(a,b) = -f(b,a)`):
```
f(a,b)
= (b⨯a)·(1-a-b)
= -(a⨯b)·(1-b-a)
= -f(b,a)
```

## Why
Idk, osu's multiplayer was down.
