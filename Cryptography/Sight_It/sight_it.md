# Sight It

## 1. Initial Analysis

I started by reading the contents of the message.txt file carefully. The text seemed like a collection of proverbs or advice about finding hidden information. The lines:

    Find the hidden message within these lines.

    Look beyond the content to find the structure.

    Notice how seemingly random elements might connect.

...were strong hints that the hidden message wasn't in the meaning of the sentences themselves, but in their structure.

## 2. Identifying the Pattern

I needed to find a pattern that could extract a message from the structure of the text. Common techniques include:

    Taking the first letter of each word.

    Taking the last letter of each line.

    Taking the first letter of each line.

    Looking for capitalization patterns or punctuation.

Given the hint "Look beyond the content to find the structure," I focused on the position of the words and lines, not the words themselves.

## 2. Testing the First-Letter-of-Each-Line Technique

I decided to test the most common steganography technique for this kind of challenge: extracting the first character from every line.

I copied the text and wrote down the first letter of each line:

    Find the ... -> F

    Life is... -> L

    Any keen... -> A

    Great puzzles... -> G

    {Sometimes... -> { This is a crucial clue!

    Help yourself... -> H

    In forensics... -> I

    Detect what... -> D

    Discovering secrets... -> D

    Each line... -> E

    Never ignore... -> N

    Important evidence... -> I

    Nothing is... -> N

    Plain text files... -> P

    Look beyond... -> L

    Always check... -> A

    Information hides... -> I

    Notice how... -> N

    Solving puzzles... -> S

    Investigation skills... -> I

    Great analysts... -> G

    Hidden messages... -> H

    The art of... -> T

Why I did this? The presence of a curly brace { as the first character of the fifth line was the smoking gun. In CTF flags, the format is always flag{...}. Seeing the { confirmed that I was assembling the word flag and that this was the correct method.

## 4. Assembling the Message

###Method1
I used the following command and then formatted the output by making use of my linux basic skills
	```bash
	cut -c1 message.txt | tr '[:upper:]' '[:lower:]' | sed 's/$/\n/' > output.txt
	```
using cat command i viewed the contents of output.txt

	```bash
	cat output.txt
	```
	
Then i replaced the spaces with underscores as most flags are formatted and had my final flag:

	flag{hidden_in_plain_sight}

###Method2
I concatenated all the first letters I collected, in order:

    F L A G { H I D D E N I N P L A I N S I G H T }

I noticed that this formed readable words: *FLAG{ HIDDEN IN PLAIN SIGHT }*

Final Assembly: To format it correctly as a flag, I removed the spaces and combined the words with underscores, as is common in flag formats.

The final flag is:

    flag{hidden_in_plain_sight}
