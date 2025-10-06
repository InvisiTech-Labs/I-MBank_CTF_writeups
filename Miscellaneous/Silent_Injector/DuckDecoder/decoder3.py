############## DuckDecoder ##############
#  
#  Description:   Python script to decode/display USB Rubber Ducky inject.bin files
#    Author(s):   JPaulMora (@jpaulmora) 
#      Version:   0.1.c (Python 3 updated version)
#                                              Copyright (C) 2015  Juan Pablo Mora
#
#  Updated for Python 3 by ChatGPT (2025)
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import binascii
import os
import sys


def hexstr(fn):
    """Read file as binary and return hex string."""
    with open(fn, 'rb') as f:
        content = f.read()
    payload = binascii.hexlify(content)
    return payload


def dsem(h, n):
    """Split hex stream into chunks of size n."""
    n = max(1, n)
    return [h[i:i + n] for i in range(0, len(h), n)]


def letiscover(letters, types, mode):
    """Decode inject.bin hex codes to readable form."""
    Delay = 0
    String = 0
    Result = []

    Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
               ",", ".", "/", ";", "'", "[", "]", "\\", "-", "=", " ", "\n",
               "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "BSPACE", '`',
               "TAB", "UP", "DOWN", "RIGHT", "LEFT", "DEL"]

    CapLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                  "Y", "Z", "<", ">", "?", ":", "\"", "{", "}", "|", "_", "+",
                  "SPACE", "ENTER", "!", "@", "#", "$", "%", "^", "&", "*",
                  "(", ")", "BSPACE", "~", "TAB", "UP", "DOWN", "RIGHT", "LEFT"]

    AltLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                  "Y", "Z", ",", ".", "/", ";", "'", "[", "]", "\\", "-", "=",
                  "SPACE\n", "ENTER", "1", "2", "3", "4", "5", "6", "7", "8",
                  "9", "0", "BSPACE", '`', "TAB", "UP", "DOWN", "RIGHT", "LEFT", "DEL"]

    HexLetters = ['04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e',
                  '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                  '1a', '1b', '1c', '1d', '36', '37', '38', '33', '34', '2f', '30',
                  '31', '2d', '2e', '2c', '28', '1e', '1f', '20', '21', '22', '23',
                  '24', '25', '26', '27', '2a', '35', '2b', '52', '51', '4f', '50', '4c']

    if mode == 1:
        # Decode to DuckEncoder-friendly output
        NoStrKeys = ["\n", "BSPACE", "TAB", "DEL", "UP", "DOWN", "RIGHT", "LEFT"]
        NoStrKReplace = ["ENTER", "BACKSPACE", "TAB", "DEL", "UP", "DOWN", "RIGHT", "LEFT"]

        for i in range(len(letters)):
            if letters[i] in HexLetters:
                LetterPos = HexLetters.index(letters[i])

                # Normal letters
                if types[i] == "00":
                    if Delay != 0:
                        Result.append(f"\nDELAY {Delay}\n")
                        Delay = 0
                    if Letters[LetterPos] in NoStrKeys:
                        Result.append("\n" + NoStrKReplace[NoStrKeys.index(Letters[LetterPos])])
                        String = 0
                    else:
                        if String == 0:
                            Result.append("\nSTRING ")
                            String = 1
                        Result.append(Letters[LetterPos])

                elif types[i] == "01":
                    Result.append(f"\nCONTROL {AltLetters[LetterPos]}")
                    Delay = 0
                    String = 0

                elif types[i] == "02":
                    if Delay != 0:
                        Result.append(f"\nDELAY {Delay}\n")
                    if String == 0 and CapLetters[LetterPos] != "\n":
                        Result.append("\nSTRING ")
                        String = 1
                    if CapLetters[LetterPos] == "\n":
                        Result.append("\nENTER ")
                        String = 0
                    elif CapLetters[LetterPos] == "BSPACE":
                        Result.append("\nBACKSPACE ")
                        String = 0
                    else:
                        Result.append(CapLetters[LetterPos])
                    Delay = 0

                elif types[i] == "04":
                    Result.append(f"\nALT {AltLetters[LetterPos]}")
                    String = 0

                elif types[i] == "05":
                    Result.append(f"\nCTRL-ALT {AltLetters[LetterPos]}")
                    String = 0

                elif types[i] == "08":
                    Result.append(f"\nGUI {AltLetters[LetterPos]}")
                    String = 0

            elif letters[i] == '00':
                Delay += int(types[i], 16)
                String = 0

    else:
        # Display human-readable output
        Arrows = ["UP", "DOWN", "RIGHT", "LEFT"]
        Arrow = 0
        for i in range(len(letters)):
            if letters[i] in HexLetters:
                LetterPos = HexLetters.index(letters[i])
                if types[i] == "00":
                    if Letters[LetterPos] == "BSPACE" and len(Result) > 0:
                        Result.pop()
                    elif Letters[LetterPos] in Arrows:
                        Result.append("\n" + Letters[LetterPos])
                        Arrow = 1
                    elif Letters[LetterPos] == "TAB":
                        Result.append("     ")
                    else:
                        if Arrow == 1:
                            Result.append("\n")
                            Arrow = 0
                        Result.append(Letters[LetterPos])
                elif types[i] == "01":
                    Result.append(f"\nCONTROL {AltLetters[LetterPos]}\n")
                elif types[i] == "02":
                    Result.append(CapLetters[LetterPos])
                elif types[i] == "04":
                    Result.append(f"\nALT {AltLetters[LetterPos]}\n")
                elif types[i] == "08":
                    Result.append(f"\nGUI {AltLetters[LetterPos]}")

    Result.append("\n\n")
    return Result


def usage(reason, ecode):
    print(f" Usage: {sys.argv[0]} < display|decode > silent.bin\n\n"
          f" Example: {sys.argv[0]} display /Documents/silent.bin\n")
    if reason:
        print(reason + "\n")
    sys.exit(ecode)


########################## Main ###################################

if 2 < len(sys.argv) < 5:
    try:
        filename = os.path.realpath(sys.argv[2])
    except IndexError:
        usage("Error: File not found", 1)

    List = dsem(hexstr(filename), 2)
    mode = sys.argv[1]
    chars = [x.decode() for x in List[::2]]
    types = [x.decode() for x in List[1::2]]

    if mode == "decode":
        Result = letiscover(chars, types, 1)
    elif mode == "display":
        Result = letiscover(chars, types, 0)
    else:
        usage("Error: No such option", -1)

    string = "".join(Result)
    print(string)
else:
    usage("", 2)
