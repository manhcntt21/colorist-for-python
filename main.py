# @author David Do
# created in 7/28/2025 2:21 AM
# description:

def color_text(text: str, color_code: int) -> str:
    """
    Returns the text formatted with ANSI escape codes for color.
    :param text: The text to format.
    :param color_code: The ANSI color code.
    :return: The formatted text.
    """
    return f'\x1b[{color_code}m{text}\x1b[0m'

def color_background(text: str, color_code: int) -> str:
    """
    Returns the text formatted with ANSI escape codes for background color. Default text color is green.
    :param text: The text to format.
    :param color_code: The ANSI background color code.
    :return: The formatted text.
    """
    return f'\x1b[32;{color_code}m{text}\x1b[0m'

if __name__ == '__main__':
    # print("Colors Text:")
    # print(f'Hello {color_text("World", 30)}: ANSI Code for: Black!')
    # print(f'Hello {color_text("World", 31)}: ANSI Code for: Red!')
    # print(f'Hello {color_text("World", 32)}: ANSI Code for: Green!')
    # print(f'Hello {color_text("World", 33)}: ANSI Code for: Yellow!')
    # print(f'Hello {color_text("World", 34)}: ANSI Code for: Blue!')
    # print(f'Hello {color_text("World", 35)}: ANSI Code for: Magenta!')
    # print(f'Hello {color_text("World", 36)}: ANSI Code for: Cyan!')
    # print(f'Hello {color_text("World", 37)}: ANSI Code for: White!')
    #
    # print("Bright Colors:")
    # print(f'Hello {color_text("World", 90)}: ANSI Code for: Bright Black!')
    # print(f'Hello {color_text("World", 91)}: ANSI Code for: Bright Red!')
    # print(f'Hello {color_text("World", 92)}: ANSI Code for: Bright Green!')
    # print(f'Hello {color_text("World", 93)}: ANSI Code for: Bright Yellow!')
    # print(f'Hello {color_text("World", 94)}: ANSI Code for: Bright Blue!')
    # print(f'Hello {color_text("World", 95)}: ANSI Code for: Bright Magenta!')
    # print(f'Hello {color_text("World", 96)}: ANSI Code for: Bright Cyan!')
    # print(f'Hello {color_text("World", 97)}: ANSI Code for: Bright White!')

    print("Background Colors:")

    print(f'Hello {color_background("World", 40)}: ANSI Code for: Black!')
    print(f'Hello {color_background("World", 41)}: ANSI Code for: Red!')
    print(f'Hello {color_background("World", 42)}: ANSI Code for: Green!')
    print(f'Hello {color_background("World", 43)}: ANSI Code for: Yellow!')
    print(f'Hello {color_background("World", 44)}: ANSI Code for: Blue!')
    print(f'Hello {color_background("World", 45)}: ANSI Code for: Magenta!')
    print(f'Hello {color_background("World", 46)}: ANSI Code for: Cyan!')
    print(f'Hello {color_background("World", 47)}: ANSI Code for: White!')

    print(f'Hello {color_background("World", 100)}: ANSI Code for: Bright Black!')
    print(f'Hello {color_background("World", 101)}: ANSI Code for: Bright Red!')
    print(f'Hello {color_background("World", 102)}: ANSI Code for: Bright Green!')
    print(f'Hello {color_background("World", 103)}: ANSI Code for: Bright Yellow!')
    print(f'Hello {color_background("World", 104)}: ANSI Code for: Bright Blue!')
    print(f'Hello {color_background("World", 105)}: ANSI Code for: Bright Magenta!')
    print(f'Hello {color_background("World", 106)}: ANSI Code for: Bright Cyan!')
    print(f'Hello {color_background("World", 107)}: ANSI Code for: Bright White!')

    print(f'Hi from {__name__}')
