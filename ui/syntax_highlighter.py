from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt6.QtCore import QRegularExpression


class BatchSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.highlighting_rules = []

        # Keywords format
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))  # Blue
        keyword_format.setFontWeight(QFont.Weight.Bold)

        keywords = [
            "echo", "off", "on", "set", "if", "else", "for", "in", "do",
            "goto", "call", "shift", "pause", "exit", "start", "cd",
            "md", "rd", "del", "copy", "xcopy", "move", "ren", "type",
            "find", "findstr", "sort", "tasklist", "taskkill", "ping", "net"
        ]

        for word in keywords:
            pattern = QRegularExpression(
                rf"\b{word}\b",
                QRegularExpression.PatternOption.CaseInsensitiveOption)
            self.highlighting_rules.append((pattern, keyword_format))

        # Variables format (%var% or !var!)
        variable_format = QTextCharFormat()
        variable_format.setForeground(QColor("#9CDCFE"))  # Light blue

        var_pattern = QRegularExpression(r"%[^%]+%|![^!]+!")
        self.highlighting_rules.append((var_pattern, variable_format))

        # Labels (:label)
        label_format = QTextCharFormat()
        label_format.setForeground(QColor("#DCDCAA"))  # Yellow
        label_format.setFontWeight(QFont.Weight.Bold)

        label_pattern = QRegularExpression(r"^\s*:[a-zA-Z0-9_]+")
        self.highlighting_rules.append((label_pattern, label_format))

        # Comments (REM or ::)
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))  # Green

        rem_pattern = QRegularExpression(r"(?i)^\s*rem\b.*")
        self.highlighting_rules.append((rem_pattern, comment_format))

        colon_pattern = QRegularExpression(r"^\s*::.*")
        self.highlighting_rules.append((colon_pattern, comment_format))

        # Strings
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))  # Orange/Red
        string_pattern = QRegularExpression(r"\".*?\"")
        self.highlighting_rules.append((string_pattern, string_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            iterator = pattern.globalMatch(text)
            while iterator.hasNext():
                match = iterator.next()
                self.setFormat(
                    match.capturedStart(),
                    match.capturedLength(),
                    format)
