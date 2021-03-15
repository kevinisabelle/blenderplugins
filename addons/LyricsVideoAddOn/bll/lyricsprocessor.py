
class LyricsScriptReader:

    textFilename = ""
    waveFiles = []

    def __init__(self):
        self.script_lines = []

    def getTextLine(self, index):
        return self.script_lines[index].text

    def getTransition(self, index):
        return self.script_lines[index].transition

    def getFrame(self, index):
        return self.script_lines[index].frame

    def process_lyrics(self, filename=""):

        Text = "0|No Text Configured"

        if (filename != ""):
            f = open(filename, "r")
            Text = f.read()

        tempTextLines = Text.splitlines()
        i = -1
        self.script_lines = [0] * len(tempTextLines)
        for line in tempTextLines:
            i = i+1
            self.script_lines[i] = ScriptLine.getFromLine(line)

    def detect_index(self, currentframe):
        i = -1
        index = 0
        for cutoff in self.script_lines:
            i = i + 1
            index = i
            if cutoff.frame > currentframe:
                index = i-1
                break

        return index


class ScriptLine:

    frame = 0
    text = ""
    transition = ""

    @staticmethod
    def getFromLine(textLine):
        print('Processing line' + textLine)
        scriptLine = ScriptLine()
        lineArrObjects = textLine.split("|")
        scriptLine.frame = int(lineArrObjects[0])
        scriptLine.text = lineArrObjects[1].replace("/", "\n")
        scriptLine.transition = lineArrObjects[2] if (
            len(lineArrObjects)) > 2 else ""
        return scriptLine
