# Demo 2
# nested dictionary

# green colour theme for a website
green_theme = {
    "background": { "red": 0, "green": 100, "blue": 0 },
    "foreground": { "red": 0, "green": 200, "blue": 100 },
    "font": { "red": 255, "green": 255, "blue": 255 }
}

# halve all of the green intensities (round down to nearest int)

for section in green_theme:
    green_theme[section]["green"] //= 2  # setting diction for each section
    # green_theme[section]["green"] = green_theme[section]["green"]// 2

print(green_theme)

