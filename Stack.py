#Stack

class Stack:
    def __init__(self):
        self.items = ["IDGAF by Dua Lipa",
                      "Two Less Lonely People by KZ Tandingan",
                      "Rockstar by Post Malone",
                      "Bodak yellow by Cardi B",
                      "Home by Machine Gun Kelly",
                      "Breakeven by The Script",
                      "Say you won't let go by James Arthur",
                      "Attention by Charlie Puth",
                      "No Limit by G - Eazy",]
        self.items2 = sorted(self.items)  
        self.items3 = self.items2[::-1]   

    def sort(self):
        return sorted(self.items2)
    def reverse(self):
        return self.items2[::-1]
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peekname(self):
        return self.items3[len(self.items)-1]
    def peeknamenext(self):
        return self.items3[len(self.items)-2]
    def peektime(self):
        return self.items[len(self.items)-1]
    def peektimenext(self):
        return self.items[len(self.items)-2]
    def size(self):
        return len(self.items)




if __name__ == "__main__":
    Mumshie = Stack()
    print "Welcome to My Playlist"
    print "My Playlist has",Mumshie.size(),"songs"
    x = input("Sort by:\n1. Name\n2.Time\n\tEnter your choice: ")
    if x == 1:
        while Mumshie.size() >= 2:
            print "Currently playing ",Mumshie.peekname()
            print "Next song is ",Mumshie.peeknamenext(), "\n - - - - - - - - - - - - - - - - - - "
            khirbae.pop()
    elif x == 2:
        while Mumshie.size() >= 2:
            print "Now Playing ",Mumshie.peektime()
            print "Next song is ", Mumshie.peektimenext(), "\n - - - - - - - - - - - - - - - - - - "
            Mumshie.pop()
    else:
print "INVALID SORTING"
