"""Memento class for saving the data"""

"""
Memento Method is a "Behavioral Design pattern" which provides the ability to restore an object 
to its previous state. 
"""

class Memento:

	"""Constructor function"""
	def __init__(self, file, content):

		"""put all your file content here"""
		
		self.file = file     
		self.content = content
        
  
        

"""It's a File Writing Utility"""

class X:

	"""Constructor Function"""

	def __init__(self, file_path):

		"""store the input file data"""
		self.file = file_path
		self.content = ""

	"""Append the data into content attr"""

	def write(self, string):
		self.content += string

	"""save the data into the Memento"""

	def save(self):
		return Memento(self.file, self.content)

	"""UNDO feature provided"""

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class Y:

	"""saves the data"""

	def save(self, x):
		self.mem = x.save()

	"""undo the content"""

	def undo(self, x):
		x.undo(self.mem)


if __name__ == '__main__':

	"""create the caretaker object"""
	y = Y()

	"""create the writer object"""
	x = X("GFG.txt")   #file = object , content = ""

	"""write data into file using writer object"""
	x.write("First vision of Data\n")   #file = object , content = "First vision of Data \n"
	print(x.content + "\n\n")


	"""save the file"""
	y.save(x) # Memento file = object , content = "First vision of Data \n"

	"""again write using the writer """
	x.write("Second vision of Data\n")  #file = object , content = "First vision of Data \n Second vision of Data"

	print(x.content + "\n\n")

	"""undo the file"""
	y.undo(x)

	print(x.content + "\n\n")  #file = object , content = "First vision of Data "
