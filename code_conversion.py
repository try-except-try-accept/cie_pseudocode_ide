tests = {'byref':
{
	'expected':
'''tbc
''',
'input':
'''// this procedure swaps
// values of X and Y
PROCEDURE SWAP(BYREF X : INTEGER, Y INTEGER)
Temp ← X // temporarily store X
X ← Y
Y ← Temp
ENDPROCEDURE'''
},

'declaration_and_assignment':
{
	'expected':
'''counter = 0 # integer
total_to_pay = 0.0 # real
game_over = False # boolean
HOURLY_RATE = 6.50
DEFAULT_TEXT = "N/A"
counter += 1
total_to_pay = number_of_hours * hourly_rate
''',
'input':
'''DECLARE Counter : INTEGER
DECLARE TotalToPay : REAL
DECLARE GameOver : BOOLEAN
CONSTANT HourlyRate = 6.50
CONSTANT DefaultText = "N/A"
Counter ← 0
Counter ← Counter + 1
TotalToPay ← NumberOfHours * HourlyRate'''
},

'arrays':
{
	'expected':
'''student_names = [None for i in range(30)] # array of strings
noughts_and_crosses = [[None for i in range(3)] for j in range(3)] # 2d array of characters
student_names[0] = "Ali"
noughts_and_crosses[1, 2] = 'X'
student_names[n+1] = student_names[n]
# assigning a group of array elements
for index in range(1, 31):
    student_names[index] = ""

''',
'input':
'''DECLARE StudentNames : ARRAY[1:30] OF STRING
DECLARE NoughtsAndCrosses : ARRAY[1:3,1:3] OF CHAR
StudentNames[1] ← "Ali"
NoughtsAndCrosses[2,3] ← ꞌXꞌ
StudentNames[n+1] ← StudentNames[n]
// assigning a group of array elements
FOR Index ← 1 TO 30
StudentNames[Index] ← ""
NEXT Index'''
},

'input_output':
{
	'expected':
'''answer = input()
print(score)
print("You have", lives, " lives left")
''',
'input':
'''INPUT Answer
OUTPUT Score
OUTPUT "You have ", Lives, " lives left"'''
},

'built-in_functions':
{
	'expected':
'''"ABCDEFGH"[:3]
"ABCDEFGH"[-3:]
len("Happy Days")
"ABCDEFGH"[3:6]
'W'.is_lower()
'h'.is_upper()
"Error 803".upper()
"JIM 803".lower()
str(87.5)
float("23.45")
int("23")
"12.36".replace("-", "", 1).replace(".", "", 1).is_numeric()
ord('A')
chr(87)
INT(27.5415)
RAND(87)
''',
'input':
'''LEFT("ABCDEFGH", 3)
RIGHT("ABCDEFGH", 3)
LENGTH("Happy Days")
MID("ABCDEFGH", 2, 3
LCASE('W')
UCASE('h')
TO_UPPER("Error 803")
TO_LOWER("JIM 803")
NUM_TO_STR(87.5)
STR_TO_NUM("23.45")
STR_TO_NUM("23")
IS_NUM("12.36")
ASC('A')
CHR(87)
int(27.5415)
randrange(0, 87)'''
},

'operators':
{
	'expected':
'''x = 10 # integer
y = 5 # integer
s = "Hello" # string
s + s
y > x and len(s) == 5
y > x or len(s) == 5
not (y > x or len(s) == 5)
y % x
y // x
''',
'input':
'''DECLARE x : INTEGER
DECLARE y : INTEGER
DECLARE s : STRING
x ← 10
y ← 5
s ← "Hello"
s & s
y > x AND LENGTH(s) = 5
y > x OR LENGTH(s) = 5
NOT (y > x OR LENGTH(s) = 5)
y MOD x
y DIV x'''
},

'selection':
	{
		'expected': '''if challenger_score > champion_score: if challenger_score > highest_score: print(challenger_name, " is champion and highest scorer")
else: print(player1_name, " is the new champion"
else: print(champion_name, " is still the new champion")
if champion_score > highest_score: print(champion_name, " is also the highest scorer"''',
'input': '''IF ChallengerScore > ChampionScore
THEN
IF ChallengerScore > HighestScore
THEN
OUTPUT ChallengerName, " is champion and highest scorer"
ELSE
OUTPUT Player1Name, " is the new champion"
ENDIF
ELSE
OUTPUT ChampionName, " is still the champion"
IF ChampionScore > HighestScore
THEN
OUTPUT ChampionName, " is also the highest scorer"
ENDIF
ENDIF'''
	},
'case_statements':
{
	'expected': '''
''',
'input': '''INPUT Move
CASE OF Move
ꞌWꞌ: Position ← Position − 10
ꞌSꞌ: Position ← Position + 10
ꞌAꞌ: Position ← Position − 1
ꞌDꞌ: Position ← Position + 1
OTHERWISE: CALL Beep
ENDCASE'''
},

'count_controlled_loops': {
	'expected': '''
''',
'input':
'''Total ← 0
FOR Row ← 1 TO MaxRow
RowTotal ← 0
FOR Column ← 1 TO 10
RowTotal ← RowTotal + Amount[Row, Column]
NEXT Column
OUTPUT "Total for Row ", Row, " is ", RowTotal
Total ← Total + RowTotal
NEXT Row
OUTPUT "The grand total is ", Total'''
},
'post_condition_loops':
	{'expected': '''
''',
'input': '''REPEAT
OUTPUT "Please enter the password"
INPUT Password
UNTIL Password = "Secret"'''
	 },
'pre_condition_loops':
	{'expected': '''
''',
'input': '''WHILE Number > 9
Number ← Number – 9
ENDWHILE'''
	 },
'procedures':
	{
'expected': '''
''',
'input': '''PROCEDURE DefaultSquare
CALL Square(100)
ENDPROCEDURE
PROCEDURE Square(Size: INTEGER)
FOR Side ← 1 TO 4
CALL MoveForward (Size)
CALL Turn (90)
NEXT Side
ENDPROCEDURE
IF Size = Default
THEN
CALL DefaultSquare
ELSE
CALL Square(Size)
ENDIF'''
	},

'functions':
	{
		'expected': '''
''',
'input':
'''FUNCTION Max(Number1: INTEGER, Number2: INTEGER) RETURNS INTEGER
IF Number1 > Number2
THEN
RETURN Number1
ELSE
RETURN Number2
ENDIF
ENDFUNCTION
OUTPUT "Penalty Fine = ", Max(10, Distance*2)'''
	},
'text_files':
	{
'expected': '''
''',
'input': '''DECLARE LineOfText: STRING
OPENFILE "FileA.txt" FOR READ
OPENFILE "FileB.txt" FOR WRITE
WHILE NOT EOF("FileA.txt")
READFILE "FileA.txt", LineOfText
IF LineOfText = ""
THEN
WRITEFILE "FileB.txt", "-------------------------"
ELSE
WRITEFILE "FILEB.txt", LineOfText
ENDIF
ENDWHILE
CLOSEFILE "FileA.txt"
CLOSEFILE "FileB.txt"'''
	},
'binary_files':
	{
		'expected': '''
''',
'input': '''DECLARE Pupil : Student
DECLARE NewPupil: Student
DECLARE Position: INTEGER
NewPupil.Surname ← "Johnson"
NewPupil.Firstname ← "Leroy"
NewPupil.DateOfBirth ← 02/01/2005
NewPupil.YearGroup ← 6
NewPupil.FormGroup ← ꞌAꞌ
OPENFILE StudentFile.Dat FOR RANDOM
FOR Position = ← 20 TO 10 STEP - 1
SEEK "StudentFile.Dat", Position
GETRECORD "StudentFile.Dat", Pupil
SEEK "StudentFile.Dat", Position + 1
PUTRECORD "StudentFile.Dat", Pupil
NEXT Position
SEEK "StudentFile.Dat", 10
PUTRECORD "StudentFile.Dat", NewPupil
CLOSEFILE "StudentFile.dat"'''
	},
'user_defined_types':
	{
'expected': '''
''',
'input': '''TYPE Season = (Spring, Summer, Autumn, Winter)
TYPE TAddPointer = ^INTEGER
TYPE Student
DECLARE Surname: STRING
DECLARE FirstName: STRING
DECLARE DateOfBirth: DATE
DECLARE YearGroup: INTEGER
DECLARE FormGroup: CHAR
ENDTYPE
DECLARE Pupil1: Student
DECLARE Pupil2: Student
DECLARE Form : ARRAY[1: 30] OF Student
DECLARE ThisSeason: Season
DECLARE NextSeason: Season
DECLARE MyAddPointer: TAddPointer
Pupil1.Surname ← "Johnson"
Pupil1.Firstname ← "Leroy"
Pupil1.DateOfBirth ← 02/01/2005
Pupil1.YearGroup ← 6
Pupil1.FormGroup ← ꞌAꞌ
Pupil2 ← Pupil1
FOR Index ← 1 TO 30
Form[Index].YearGroup ← Form[Index].YearGroup + 1
NEXT INDEX
ThisSeason ← Spring
MyAddPointer ← ^ThisSeason
NextSeason ← MyAddPointer^ + 1
// pointer is dereferenced to access the value stored at the address
'''
}
}


from json import dump

with open("test_data/pseudocode_examples.json", "w") as f:
	dump(tests, f)