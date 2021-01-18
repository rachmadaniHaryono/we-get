"""
Copyright (c) 2016-2021 we-get developers (https://github.com/rachmadaniHaryono/we-get/)
See the file 'LICENSE' for copying.
"""

from we_get.core.commands import COMMANDS
from prompt_toolkit.completion import Completer
from prompt_toolkit.completion import Completion


class WGCompleter(Completer):
    def __init__(self, torrents):
        self.torrents = torrents
        self.words = None
        self.word_before_cursor = None
        self.word_after_cursor = None

    def word_matches(self, word):
        """word_matches: match the owrd to the start of the text."""
        return word.startswith(self.word_before_cursor)

    def word_is_subcommand(self, word):
        """word_is_subcommand:
        split the word if the results are more then 1,
        this is a sub-comamnd "X Y".
        """
        if word.endswith(" "):
            return True
        return False

    def words_count(self, text):
        if text.endswith(" "):
            return len(text.split()) + 1
        return len(text.split())

    def word_command_flags(self, text):
        command = text.split()[0]
        if command in COMMANDS:
            return COMMANDS[command]["opts"]
        return list()

    def get_completions(self, document, complete_event):
        """get_completion: main call from the abstract base class "Completer"
        in prompt_toolkit.
        """
        self.word_before_cursor = document.get_word_before_cursor(WORD=True)
        self.word_after_cursor = document.text_after_cursor

        if self.words_count(document.text) == 1:
            self.words = COMMANDS
        elif self.words_count(document.text) == 2:
            try:
                if COMMANDS[document.text[:-1].split()[0]]["required_argument"]:
                    self.words = self.torrents
                else:
                    self.words = list()
            except KeyError:
                self.words = list()
        elif self.words_count(document.text) == 3:
            self.words = self.word_command_flags(document.text)
        else:
            self.words = COMMANDS

        for word in self.words:
            if self.word_matches(word):
                yield Completion(word, -len(self.word_before_cursor))
