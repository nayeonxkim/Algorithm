# 

1, 2, 3

4, 5, 6

7, 8, 9

```python
N = 3
arr = [list((map(int, input().split())) for _ in range(N)]
```

123

456

789

→ split 생략



000

000

000

→ `A = [[0] * 3 for _ in range(3)]`

`[[0] * 3]` 이거 아님;

---

# 행 순회

----->

----->

----->

n X m arr

```python
for i in range(n):        # i = 행
    for j in range(m):    # j = 열
        arr[i][j]
```

---

# 열 순회

```python
for j in range(m):        # i = 행
    for i in range(n):    # j = 열
        arr[i][j]
```

\> 행과 열의 수가 다른 경우 유의

그냥 row, col이라고 쓰자.

---

# 지그재그 순회

```python
for i in range(n):
    for j in range(m):
        arr[i][j + (m-1-2*j) * (i%2)]
```

\> 홀수면 실행, 짝수면 0 (그냥 j)

---

# 비트 연산자

1 bit = 0또는 1

bit * 8 = 1 byte



숫자 1 = 2**0

비트 0번자리에 2**0 즉 1 저장함. 나머지는 0


