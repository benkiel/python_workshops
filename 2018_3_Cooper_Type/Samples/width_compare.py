#FLM: Width compare
from robofab.world import AllFonts
from robofab.interface.all.dialogs import Message

fonts = AllFonts()
if len(fonts) == 2:
	for glyph in fonts[0]:
		if glyph.width != fonts[1][glyph.name].width:
			print glyph.name + ' width is different'
else:
	Message('Only two fonts please!')
