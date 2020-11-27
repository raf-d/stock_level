class Text:
    def __init__(self, t, p):
        self.text = t
        self.page_length = p
    def __iter__(self):
        self.pointer = 0
        return self
    def __next__(self):
        if self.pointer >= len(self.text):
            raise StopIteration
        start = self.pointer
        end = start + self.page_length
        result = self.text[start:end]
        self.pointer = end
        return result
text = Text("Ala ma kota", 2)
for i in text:
    print(i)