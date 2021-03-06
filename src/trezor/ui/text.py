from micropython import const
from trezor import ui

TEXT_HEADER_HEIGHT = const(48)
TEXT_LINE_HEIGHT = const(26)
TEXT_MARGIN_LEFT = const(14)
TEXT_MAX_LINES = const(4)

# needs to be different from all colors and font ids
BR = const(-256)


def render_words(words: list, new_lines: bool, max_lines: int) -> None:
    # initial rendering state
    font = ui.NORMAL
    fg = ui.FG
    bg = ui.BG
    offset_x = TEXT_MARGIN_LEFT
    offset_y = TEXT_HEADER_HEIGHT + TEXT_LINE_HEIGHT
    OFFSET_X_MAX = ui.WIDTH
    OFFSET_Y_MAX = TEXT_HEADER_HEIGHT + TEXT_LINE_HEIGHT * max_lines

    # sizes of common glyphs
    SPACE = ui.display.text_width(' ', font)
    DASH = ui.display.text_width('-', ui.BOLD)
    ELLIPSIS = ui.display.text_width('...', ui.BOLD)

    for word in words:
        if isinstance(word, int):
            if word == BR:
                # line break
                if not offset_y < OFFSET_Y_MAX:
                    ui.display.text(offset_x, offset_y, '...', ui.BOLD, ui.GREY, bg)
                    return
                offset_x = TEXT_MARGIN_LEFT
                offset_y += TEXT_LINE_HEIGHT
            elif word == ui.NORMAL or word == ui.BOLD or word == ui.MONO:
                # change of font style
                font = word
            else:
                # change of foreground color
                fg = word
            continue

        width = ui.display.text_width(word, font)

        while offset_x + width + SPACE + ELLIPSIS > OFFSET_X_MAX:
            space_for_another_line = offset_y < OFFSET_Y_MAX
            word_fits_in_one_line = width < (OFFSET_X_MAX - TEXT_MARGIN_LEFT)
            if space_for_another_line and word_fits_in_one_line:
                # line break
                offset_x = TEXT_MARGIN_LEFT
                offset_y += TEXT_LINE_HEIGHT
                break
            # word split
            if space_for_another_line:
                split = '-'
                splitw = DASH
            else:
                split = '...'
                splitw = ELLIPSIS
            # find span that fits
            for index in range(len(word) - 1, 0, -1):
                letter = word[index]
                width -= ui.display.text_width(letter, font)
                if offset_x + width + splitw < OFFSET_X_MAX:
                    break
            else:
                index = 0
            span = word[:index]
            # render word span
            ui.display.text(offset_x, offset_y, span, font, fg, bg)
            ui.display.text(offset_x + width, offset_y, split, ui.BOLD, ui.GREY, bg)
            # line break
            if not space_for_another_line:
                return
            offset_x = TEXT_MARGIN_LEFT
            offset_y += TEXT_LINE_HEIGHT
            # continue with the rest
            word = word[index:]
            width = ui.display.text_width(word, font)

        # render word
        ui.display.text(offset_x, offset_y, word, font, fg, bg)
        offset_x += width
        offset_x += SPACE

        # line break
        if new_lines:
            if not offset_y < OFFSET_Y_MAX:
                ui.display.text(offset_x, offset_y, '...', ui.BOLD, ui.GREY, bg)
                return
            offset_x = TEXT_MARGIN_LEFT
            offset_y += TEXT_LINE_HEIGHT


class Text(ui.Widget):
    def __init__(self,
                 header_text: str,
                 header_icon: bytes,
                 *content: list,
                 new_lines: bool = True,
                 max_lines: int = TEXT_MAX_LINES,
                 icon_color: int = ui.ORANGE_ICON):
        self.header_text = header_text
        self.header_icon = header_icon
        self.content = content
        self.new_lines = new_lines
        self.max_lines = max_lines
        self.icon_color = icon_color

    def render(self):
        ui.header(self.header_text, self.header_icon, ui.TITLE_GREY, ui.BG, self.icon_color)
        render_words(self.content, self.new_lines, self.max_lines)
