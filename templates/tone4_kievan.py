


key_sig = "g \major"

# Counting from zero
repeat_start = 3
repeat_end = 5


## Soprano

s = [['fs4', 'fs4', 'a4', 'g4', 'fs4', 'g2'],
     ['g4', 'a4', 'g4', 'a2', 'g2'],
     ['b4', 'b2', 'a4', 'g4', 'a2', 'g2'],
     ['g4', 'fs2', 'g2', 'a2.'],
     ['a4', 'g2', 'a4', 'b4', 'a4', 'g4', 'fs1'],
     ['g4', 'g4', 'a2', 'g2.'],
     ['g4', 'a4', 'a4', 'g4', 'fs4', 'g4', 'a2', 'g4', 'fs2', 'e4', 'd4', 'e1']]

s1 = [['++fs4', '**fs4', 'a4', 'g4', 'fs4', 'g2'],
     ['g4', '++a4', 'g4', '**a2', 'g2'],
     ['b4', '**b2', 'a4', '++g4', '**a2', 'g2'],
     ['++g4', '**fs2', 'g2', 'a2.'],
     ['++a4', '**g2', 'a4', '**b4', 'a4', 'g4', 'fs1'],
     ['++g4', 'g4', '**a2', 'g2.'],
     ['g4', '++a4', 'a4', 'g4', 'fs4', '**g4', 'a2', 'g4', '**fs2', 'e4', 'd4', 'e1']]

ref = {'recit': [0, 1, 3, 0, 0, 0, 1],
         'emph': [[1], [3], [1, 4], [1], [1], [3], [4]],
         'pickup': [False, False, True, False, False, False]
         }

### THESE STILL NEED TO BE FIXED.
### Run a test on soprano line first to see what happens

## Alto

a = [['d4', 'd4',  'd4', 'd4', 'd4', 'd2'],
     ['e4', 'fs4', 'e4', 'fs2', 'd2'],
     ['g4', 'g2', 'd4', 'd4', 'd2', 'd2'],
     ['d4', 'd2', 'd2', 'fs2.'],
     ['fs4', 'd2', 'd4',  'd4', 'd4', 'd4', 'd1',
     ['d4', 'd4', 'd2', 'd2.'],
     ['fs4', 'd4', 'd4', 'd4', 'd2', 'd4', 'cs4', 'b4', 'b1']]

## Tenor

t = ["a4 a a c b a b2 b \ibar",
     "b4 b b c c c b c2 c4 b2 \ibar",
     "d2 d4 c4 b b c2 b \ibar",
     "b4 b b b a2 b c2. \ibar",
     "c4 c c c b2( c4) d( c) b a1 \ibar",
     "b4 b c2 b2. \ibar",
     "c4 c b a b( c2 b4 a2) a4 fs g1"]

## Bass

b = ["d4 d d d d4 d g2 g \ibar",
     "e4 e e d d d d d2 d4 g2 \ibar",
     "g2 g4 fs4 g g d2 g \ibar",
     "g4 g g g d2 d d2. \ibar",
     "d4 d d d g2. fs2 g4 d1 \ibar",
     "g4 g d2 g2. \ibar",
     "d4 d d d g( fs2 g4 d2) a4 b e1"]
