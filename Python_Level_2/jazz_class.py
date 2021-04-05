class album():
    def __init__(self,name,artist,year,label,personnel):
        self.name = name
        self.artist = artist
        self.year = year
        self.label = label
        self.personnel = personnel

        print(f"Album {name} added!")

    def __repr__(self):
        return f"Album: {self.name}, Artist: {self.artist}"

a1 = album('Kind of Blue','Miles Davis',1959,'Blue Note',{'drummer':'Philly Joe Jones'})
a2 = album('Love Supreme', 'John Coltrane', 1965,'Impulse! Records',{'drummer':'Elvin Jones'})

print(a1)
print(a2)
print(a2.name)
print(a1.personnel['drummer'])
