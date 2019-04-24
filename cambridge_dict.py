import sqlite3


class CambridgeDict():
    def __init__(self):
        self.connection = sqlite3.connect('CambridgeDict.db')
        self.curs = self.connection.cursor()

    def define(self, word):
        word = word.lower()
        whitelist = set('abcdefghijklmnopqrstuvwxyz')
        word = ''.join(filter(whitelist.__contains__, word))
        self.curs.execute("SELECT definition FROM Dictionary WHERE word = \"{0}\";".format(word))
        try:
            definition = self.curs.fetchall()[0][0]
            length = 50
            for i in range(length, len(definition), length):
                if definition[i] != ' ':
                    definition = definition[0:i] + "-\n" + definition[i:]
                else:
                    definition = definition[0:i] + "\n" + definition[i + 1:]
            return definition
        except IndexError:
            return 'Unable to find definition'
