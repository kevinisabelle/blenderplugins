lyricsExample = '''
100|    Phrase test et test/2e ligne    |trans:default
150|    |trans:zoom
'''


class Transition:

    def process_transition(self):
        print('test')


class LyricsScriptReader:

    def read_file(self):
        print('test')
        print(self)

    def process_lyrics(self, Text):
        tempTextLines = Text.splitlines()
        LyricsLines = Text.splitlines()
        StartPositions = [0] * len(tempTextLines)
        i = -1
        for line in tempTextLines:
            i = i+1
            LyricsLines[i] = line.split("|", 1)[1].replace("/", "\n")
            StartPositions[i] = int(line.split("|", 1)[0])

    def detect_index(self, currentframe, *positions):
        i = -1
        index = 0
        for cutoff in positions:
            i = i + 1
            if cutoff > currentframe:
                index = i-1
                break

        return index


scriptReader = LyricsScriptReader()
scriptReader.read_file()
