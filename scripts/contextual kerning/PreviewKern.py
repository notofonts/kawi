#MenuTitle: Preview Kerning List
__doc__="""
Preview Kerning List
"""

import vanilla
import base64
import traceback
import re

font = Glyphs.font

class kernList:
	def __init__(self):
		self.w = vanilla.Window((400,100), "Kerning List", minSize=(400,100))
		self.masterIndex = 0
		columnDescriptions = [
			dict(
                identifier="id",
                title="id",
                sortable=True,
				editable=False
            ),
            dict(
                identifier="affected",
                title="affected",
                sortable=True,
				editable=False
            ),
            dict(
                identifier="affecting",
                title="affecting",
                sortable=True,
				editable=False

            ),
            dict(
                identifier="value",
                title="value",
                sortable=True,
                editable=True
            )
            ]
		self.w.kernList = vanilla.List(
			"auto",
			items = self.kerningList(self.masterIndex),
			columnDescriptions = columnDescriptions,
			selectionCallback = self.clickCallback,
			editCallback = self.editKernValue
		)
		self.w.language = vanilla.PopUpButton('auto', ['javanese', 'kawi', 'balinese'])
		self.w.masterSelect = vanilla.PopUpButton("auto", self.getMaster(), callback=self.getMasterId)
		
		rules = [
		    # Vertical
		    "H:|-[kernList(>=550)]-|",
		    "H:|-[language]-|",
		    "H:|-[masterSelect]-|",
		    "V:|-[kernList(>=150)]-[language]-[masterSelect]-|"
		]
		self.w.addAutoPosSizeRules(rules)
		self.w.open()
	
	def getMaster(self):
		masters = []
		for master in font.masters:
			masters.append(master.name)
		return masters
	
	def clickCallback(self, sender):
		listId = sender.getSelection()
		kernList = sender.get()
		kernDict = kernList[listId[0]]
		affected = [x for x in kernDict['affected'].split("_")]
		affecting = [x for x in kernDict['affecting'].split("_")]
		value = kernDict['value']
		
		text = ""
		for x in affected:
			for y in affecting:
				if self.w.language.getItem() == 'balinese':
					text += f"/ka-bali/suku-bali/{x}{self.belowSplitter(y,'balinese')}/ka-bali/la-bali"
				if self.w.language.getItem() == 'javanese':
					text += f"/ka-java/suku-java/{x}{self.belowSplitter(y,'javanese')}/ka-java/la-java"
				elif self.w.language.getItem() == 'kawi':
					text += f"/ka-kawi/vowelU-kawi/{x}{self.belowSplitter(y,'kawi')}/la-kawi/ka-kawi"

		font = Glyphs.font
		if font.currentTab:
			font.currentTab.text = text
			PreviewTextWindow.open()
			PreviewTextWindow.text = font.currentTab.text
			PreviewTextWindow.fontSize = 150
			self.w.makeKey()
		else:
			font.newTab(text)
			PreviewTextWindow.open()
			font = PreviewTextWindow.font
			PreviewTextWindow.text = font.currentTab.text
			PreviewTextWindow.fontSize = 150
			self.w.makeKey()
			
	def belowSplitter(self, glyphname, lang):
		text = ""
		if lang == 'kawi':
			glyph = f"/{glyphname}"
			listHold = glyph.split('.')
			listHold.pop()
			listHold.insert(0, '/virama-kawi')
			text = "".join(listHold)
		
		if lang == 'balinese':
			glyph = f"/{glyphname}"
			listHold = glyph.split('.')
			listHold.pop()
			listHold.insert(0, '/adegadeg-bali')
			text = "".join(listHold)
			
		if lang == 'javanese':
			listHold = glyphname.split('_')
			newList = []
			for x in listHold:
				replaced = x.replace('Pas', '-java')
				newString = re.sub(r"|\.alt|\.below2|.base|.below|.001|.002?", "", replaced)
				newList.append("/" + newString)
			newList.insert(0, '/pangkon-java')
			text = "".join(newList)
		return text
	
	def editKernValue(self, sender):
		try:
			listId = sender.getSelection()[0]
			kernList = sender.get()
			masterIndex = self.w.masterSelect.get()
			value = int(kernList[listId]['value'])
			kernId = kernList[listId]['id']
			masterId = font.masters[masterIndex].id
			font.masters[masterId].font.masters[self.masterIndex].numbers[kernId] = value
			value1 = font.masters[masterId].numbers[kernId]
			print(font.masters[masterId], kernId, value1)
			print(len(font.masters[masterId].numbers))
		except:
			print(traceback.format_exc())

	def getMasterId(self, sender):
		try:
			self.masterIndex = sender.get()
			items = self.kerningList(self.masterIndex)
			self.w.kernList.set(items)
			font = PreviewTextWindow.font
			instanceNames = [instance.name for instance in font.instances]
			regularIndex = instanceNames.index(sender.getItem())
			PreviewTextWindow.instanceIndex = regularIndex
		except:
			print(traceback.format_exc())

	
	def replaceChar(self, text):
		replacements = {'9': '-', '8': '.'}
		newString = text.replace("9", "-").replace("8", ".")
		return newString
	
	def kerningList(self, masterIndex):
		items = []
		for i, a in enumerate(font.numbers):
			if a:
#				name_decoded = self.decodeBase64(a.name)
				names = a.name.split("_")
				affected = self.replaceChar(names[0])
				affecting = self.replaceChar(names[1])
				newDict = dict(
					id = a.name,
					affected = affected,
					affecting = affecting,
					value = font.masters[self.masterIndex].numbers[a.name]
				)
				items.append(newDict)
		
		return items


if font:
	kernList()
else:
	print('Open Font')