import sys
import math

mapping = {
    "x" : {
        "F" : "U",
        "B" : "D",
        "U" : "B",
        "D" : "F",
        "L" : "L",
        "R" : "R"
    },
    "x'" : {
        "F" : "D",
        "B" : "U",
        "U" : "F",
        "D" : "B",
        "L" : "L",
        "R" : "R"
    },
    "y" : {
        "F" : "L",
        "B" : "R",
        "U" : "U",
        "D" : "D",
        "L" : "B",
        "R" : "F"
    },
    "y'" : {
        "F" : "R",
        "B" : "L",
        "U" : "U",
        "D" : "D",
        "L" : "F",
        "R" : "B"
    },
    "z" : {
        "F" : "F",
        "B" : "B",
        "U" : "R",
        "D" : "L",
        "L" : "U",
        "R" : "D"
    },
    "z'" : {
        "F" : "F",
        "B" : "B",
        "U" : "L",
        "D" : "R",
        "L" : "D",
        "R" : "U"
    }
}

rotations = input().split()
face_1 = input()
face_2 = input()

for rotation in rotations:
    face_1 = mapping[rotation][face_1]
    face_2 = mapping[rotation][face_2]

print(face_1)
print(face_2)
