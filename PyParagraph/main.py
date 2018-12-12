file = open("paragraph.txt", "r", encoding="ascii")
print(file)

file = "paragraph.txt"

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'r') as text:

    # Store all of the text inside a variable called "file_content"
    file_content = text.read()

# count the number of spaces between words
space_count = file_content.count(' ')

# count the number of hyphens that combine words
hyphen_count = file_content.count('-')

# add two to account for the first and last words which do not have any spaces
word_count = space_count + hyphen_count + 2

# cacluate
Sentence_Calc = file_content.count('.')
Sentence_Leng = word_count / Sentence_Calc
Sentence_Leng = str(round(Sentence_Leng, 1))

    # Print the contents of the text file
####### ran out of time to get the average letter count#################
print(f'Approximate Word Count: {word_count}')
print(f'Approximate Sentence Count: {Sentence_Calc}')
print(f'Approximate Sentence Length: {(Sentence_Leng)}') 

# =============================================================================
#     Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.6
# Average Sentence Length: 24.0
# 
# =============================================================================

