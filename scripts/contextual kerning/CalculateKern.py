#MenuTitle: Calculate Kern Feature
__doc__="""
Calculate Kern Feature and write Numbers Value along with opentype code
"""
from collections import defaultdict
import base64
import vanilla

class WindowKern():
	
	def __init__(self):
		self.w = vanilla.Window((350, 200), "Generate Kern Feature")
		self.w.group1 = vanilla.Group('auto')
		self.w.group1.text = vanilla.TextBox('auto','Script :')
		self.w.group1.popUpButton = vanilla.PopUpButton('auto', ["javanese", "balinese", "kawi"])
		self.w.group2 = vanilla.Group('auto')
		self.w.group2.text2 = vanilla.TextBox('auto','Consonant Anchor :')
		self.w.group2.editText2 = vanilla.EditText('auto', text='bottom')
		self.w.group3 = vanilla.Group('auto')
		self.w.group3.text3 = vanilla.TextBox('auto', 'Below Form Anchor :')
		self.w.group3.editText3 = vanilla.EditText('auto', text='_bottom')
		self.w.group4 = vanilla.Group('auto')
		self.w.group4.text4 = vanilla.TextBox('auto', 'Threshold :')
		self.w.group4.threshold4 = vanilla.EditText('auto', text='70')
		self.w.generate = vanilla.Button('auto', 'Generate Kern', callback=self.printAll)
		
		rules = [
			"H:|-[group1]-|",
			"H:|-[group2]-|",
			"H:|-[group3]-|",
			"H:|-[group4]-|",
			"H:|-[generate]-|",
			"V:|[group1(>=20)]-space-[group2(>=20)]-space-[group3(>=20)]-space-[group4(>=20)]-[generate]-|"
		]
		
		nestRules1 = [
			"H:|[text]-[popUpButton]|",
		]
		
		nestRules2 = [
			"H:|[text2]-[editText2]|",
		]
		
		nestRules3 = [
			"H:|[text3]-[editText3]|"
		]
		nestRules4 = [
			"H:|[text4]-[threshold4]|"
		]
		metrics = {
			"space" : 15
		}
		
		self.w.addAutoPosSizeRules(rules, metrics)
		self.w.group1.addAutoPosSizeRules(nestRules1)
		self.w.group2.addAutoPosSizeRules(nestRules2)
		self.w.group3.addAutoPosSizeRules(nestRules3)
		self.w.group4.addAutoPosSizeRules(nestRules4)

		self.w.open()
	
	def encodeBase64(self, name):
		name_bytes = name.encode('utf-8')
		base64_bytes = base64.b64encode(name_bytes)
		base64_name = base64_bytes.decode('utf-8')
	
		return base64_name
	
	def convertToDict(self ,alist):
		newDict = {}
		for mid, value, name in alist:
			newDict[value] = name
		
		return newDict

	def replaceChar(self,text):
		replacements = {'-': '9', '.': '8'}
		replaced_chars = [replacements.get(char, char) for char in text]
		newString = ''.join(replaced_chars)

		return newString
		
	def printAll(self, sender):
		anchorConst = self.w.group2.editText2.get()
		anchorConjunct = self.w.group3.editText3.get()
		threshold = self.w.group4.threshold4.get()
		
		thisFont = Glyphs.font
		script = self.w.group1.popUpButton.getItem()
		threshold = self.w.group4.threshold4.get()
		HasDescenders = set()
		
		for glyph in thisFont.glyphs:
			for layer in glyph.layers:
				if glyph.script == script and int(layer.bounds.origin.y) < -20 and glyph.export == 1:
					HasDescenders.add(glyph.name)
		
		features = set()

		
		for master in thisFont.masters:
			letters = []
			pasangans = []
			HasDescenders = set()
			
			for glyph in thisFont.glyphs:
				for layer in glyph.layers:
					if glyph.script == script and int(layer.bounds.origin.y) < -20 and glyph.export == 1:
						HasDescenders.add(glyph.name)
	
			for glyph in thisFont.glyphs:
				layer = glyph.layers[master.id]
				for anchor in layer.anchors:
					if glyph.category == "Letter" and glyph.export == 1 and glyph.script == script and '.post' not in glyph.name:
						if anchor.name == anchorConst:
							letters.append((master.id, int(layer.bounds.size.width), glyph.name))
	
					if glyph.category == "Mark" and glyph.export == 1 and glyph.script == script and '.post' not in glyph.name:
						if anchor.name == anchorConjunct:
							pasangans.append((master.id, int(layer.anchors[anchorConjunct].position.x) - int(layer.bounds.origin.x), glyph.name))

			letter = self.convertToDict(letters)
			pasangan = self.convertToDict(pasangans)
			
			features = set()
			for v, w in letter.items():
				for x, y in pasangan.items():
					if x > v:
						currentName = f"{w}_{y}"
						name = self.replaceChar(currentName)
						value = int((x - v) + int(threshold))
						master.setNumberValueValue_forName_(value, name)
						featureLine = f"pos @LetterWithBelow [{w}]' [{y}] <${{{name}}} 0 ${{{name}}} 0>;"
						features.add(featureLine)
						
		if len(script) == 0:
			Message("Select Script First")
		elif len(features) == 0:
			Message("No Feature Generated")
		else:
			print(pasangans)
			fea = "#Automatic Code End\nlookup contextualKern " + '{\n'+ '\tlookupflag UseMarkFilteringSet [' + " ".join(set(x[2] for x in pasangans)) + '];\n\n' + '\n'.join(features) + '\n} contextualKern;'
			if thisFont.classes["LetterWithBelow"]:
				thisFont.classes["LetterWithBelow"].code = " ".join(HasDescenders)
			else:
				thisFont.classes.append(GSClass('LetterWithBelow', " ".join(HasDescenders)))
			if thisFont.features["kern"]:
				thisFont.features["kern"].code = fea
			else:
				thisFont.features.append(GSFeature('kern', fea))

WindowKern()