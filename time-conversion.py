def timeConversion(s):
    if "AM" in s:
        #remove AM/PM - works
        s = s.replace("AM", "")

        #slice out first two string elements - works
        first_two_char = s[:2]

        #add 12 if not 24 else 0 - works
        first_two_char = int(first_two_char)
        if first_two_char == 12:
            first_two_char = "00"
            converted_time = first_two_char + s[2:]
            return converted_time


        #concat it to the rest of the string - works
        if first_two_char != "00":
            first_two_char = str(first_two_char)
            converted_time = "0" + first_two_char + s[2:]
            return converted_time
        
    else:
        #remove AM/PM - works
        s = s.replace("PM", "")
        first_two_char = s[:2]
        first_two_char = int(first_two_char)
        if first_two_char < 12:
            first_two_char += 12
        first_two_char = str(first_two_char)
        converted_time = first_two_char + s[2:]
        return converted_time
        



s = "12:05:39AM"
time = timeConversion(s)
print(time)