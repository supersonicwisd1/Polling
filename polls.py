class Polling:
    def __init__(self):
        self.polling_id = None
        self.party = None
        self.votes = None
        self.entered_by = None

    def setID(self, polling_id):
        self.polling_id = polling_id

    def setParty(self, party):
        self.party = party

    def setVotes(self, votes):
        self.votes = votes

    def setInput(self, entered_by):
        self.entered_by = entered_by


polls = Polling()
polls.setID(8)
print(polls.polling_id)


