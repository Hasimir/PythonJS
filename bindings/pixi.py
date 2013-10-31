# Pixi.js wrapper for PythonJS
# by Brett Hartshorn - copyright 2013
# License: "New BSD"

class Texture:
	def __init__(self, baseTexture=None, crop=None, fromImage=None, crossOrigin=False, fromFrame=None, fromCanvas=None):
		with javascript:
			if baseTexture:
				self[...] = new( PIXI.Texture(baseTexture[...], crop) )
			elif fromCanvas:
				self[...] = PIXI.Texture.fromCanvas( fromCanvas )
			elif fromFrame:
				self[...] = PIXI.Texture.fromFrame( fromFrame )
			elif fromImage:
				self[...] = PIXI.Texture.fromImage( fromImage, crossOrigin )

	def setFrame(self, rect):
		with javascript:
			self[...].setFrame( rect[...] )


class _Renderer:
	@property
	def view(self):
		with javascript:
			return self[...].view

	def render(self, stage):
		with javascript:
			self[...].render( stage[...] )


class WebGLRenderer( _Renderer ):
	def __init__(self, width=800, height=600, view=None, transparent=False, antialias=False):
		with javascript:
			self[...] = new( PIXI.WebGLRenderer(width, height, view, transparent, antialias) )

class CanvasRenderer( _Renderer ):
	def __init__(self, width=800, height=600, view=None, transparent=False, antialias=False):
		with javascript:
			self[...] = new( PIXI.CanvasRenderer(width, height, view, transparent, antialias) )


class Point:
	def __init__(self, x=0, y=0, object=None):
		with javascript:
			if object:
				self[...] = object
			else:
				self[...] = new( PIXI.Point() )

	@property
	def x(self):
		with javascript: return self[...].x
	@x.setter
	def x(self, value):
		with javascript: self[...].x = value

	@property
	def y(self):
		with javascript: return self[...].y
	@y.setter
	def y(self, value):
		with javascript: self[...].y = value





class DisplayObject:
	def set_pressed_callback(self, callback, touch=True):
		print 'setting pressed callback', callback
		with javascript:
			self[...].mousedown = callback
			if touch:
				self[...].touchstart = callback

	def set_released_callback(self, callback, touch=True, outside=True):
		with javascript:
			self[...].mouseup = callback
			if touch:
				self[...].touchend = callback
			if outside:
				self[...].mouseupoutside = callback

	def set_drag_callback(self, callback, touch=True):
		with javascript:
			self[...].mousemove = callback
			if touch:
				self[...].touchmove = callback

	@property
	def position(self):
		with javascript: ptr = self[...].position
		return Point( object=ptr )

	@property
	def scale(self):
		with javascript: ptr = self[...].scale
		return Point( object=ptr )

	@property
	def pivot(self):
		with javascript: ptr = self[...].pivot
		return Point( object=ptr )


	@property
	def rotation(self):
		with javascript: return self[...].rotation
	@rotation.setter
	def rotation(self, value):
		with javascript: self[...].rotation = value


	@property
	def alpha(self):
		with javascript: return self[...].alpha
	@alpha.setter
	def alpha(self, value):
		with javascript: self[...].alpha = value


	@property
	def visible(self):
		with javascript: return self[...].visible
	@visible.setter
	def visible(self, value):
		with javascript: self[...].visible = value

	@property
	def hitArea(self):
		with javascript: return self[...].hitArea
	@hitArea.setter
	def hitArea(self, value):
		with javascript: self[...].hitArea = value

	@property
	def buttonMode(self):
		with javascript: return self[...].buttonMode
	@buttonMode.setter
	def buttonMode(self, value):
		with javascript: self[...].buttonMode = value

	@property
	def renderable(self):
		with javascript: return self[...].renderable
	@renderable.setter
	def renderable(self, value):
		with javascript: self[...].renderable = value


	@property
	def parent(self):  ## read only
		with javascript: return self[...].parent

	@property
	def stage(self):  ## read only
		with javascript: return self[...].stage

	@property
	def worldAlpha(self):  ## read only
		with javascript: return self[...].worldAlpha


	def setInteractive(self, value):
		with javascript:
			if value:
				self[...].interactive = True
			else:
				self[...].interactive = False

	@property
	def interactive(self):
		with javascript: return self[...].interactive
	@interactive.setter
	def interactive(self, value):
		with javascript: self[...].interactive = value

	@property
	def mask(self):
		with javascript: return self[...].mask
	@mask.setter
	def mask(self, value):
		with javascript: self[...].mask = value

	def addFilter(self, graphics):
		with javascript: return self[...].addFilter( graphics )

	def removeFilter(self):  ## private
		with javascript: return self[...].removeFilter()

	def updateTransform(self):  ## private
		with javascript: return self[...].updateTransform()

class DisplayObjectContainer( DisplayObject ):


	@property
	def children(self):
		with javascript: ptr = self[...].children
		return list( js_object=ptr )

	def addChild(self, child):
		with javascript:
			self[...].addChild( child[...] )

	def addChildAt(self, child, index=0):
		with javascript:
			self[...].addChildAt( child[...], index )

	def getChildAt(self, index=0):
		with javascript:
			return self[...].getChildAt( index )

	def removeChild(self, child):
		with javascript:
			self[...].removeChild( child[...] )


class Stage( DisplayObjectContainer ):
	def __init__(self, backgroundColor=0, interactive=False ):
		with javascript:
			self[...] = new( PIXI.Stage(backgroundColor, interactive) )

	def setBackgroundColor(self, color):
		with javascript:
			self[...].setBackgroundColor( color )

	def getMousePosition(self):
		with javascript:
			return self[...].getMousePosition()


class Sprite( DisplayObjectContainer ):
	def __init__(self, texture=None, blendMode='NORMAL'):
		with javascript:
			## texture can be low level PIXI.Texture or high level PythonJS Texture
			if isinstance( texture, Texture ):
				texture = texture[...]

			self[...] = new( PIXI.Sprite(texture) )

			if blendMode == 'NORMAL':
				self[...].blendMode = PIXI.blendModes.NORMAL
			elif blendMode == 'SCREEN':
				self[...].blendMode = PIXI.blendModes.SCREEN
			else:
				print 'ERROR: unknown blend mode type for Sprite:' + blendMode

	@property
	def width(self):
		with javascript: return self[...].width
	@width.setter
	def width(self, value):
		with javascript: self[...].width = value

	@property
	def height(self):
		with javascript: return self[...].height
	@height.setter
	def height(self, value):
		with javascript: self[...].height = value

	def setTexture(self, texture):
		with javascript: self[...].setTexture( texture )

	@property
	def anchor(self):
		with javascript: ptr = self[...].anchor
		return Point( object=ptr )


class MovieClip( Sprite ):
	def __init__(self, textures=None, animationSpeed=1.0, loop=True, onComplete=None):
		with javascript: arr = []
		for tex in textures:
			if isinstance(tex, Texture):
				arr.push( tex[...] )
			else:
				arr.push( tex )

		with javascript:
			self[...] = new( PIXI.MovieClip( arr ) )
			self[...].animationSpeed = animationSpeed
			self[...].loop = loop
			self[...].onComplete = onComplete

	@property
	def currentFrame(self):
		with javascript: return self[...].currentFrame

	@property
	def playing(self):
		with javascript: return self[...].playing

	def play(self):
		with javascript: return self[...].play()

	def stop(self):
		with javascript: return self[...].stop()

	def gotoAndPlay(self, frame):
		with javascript: return self[...].gotoAndPlay( frame )

	def gotoAndStop(self, frame):
		with javascript: return self[...].gotoAndStop( frame )


class Text( Sprite ):
	def __init__(self, text, font='bold 20pt Arial', fill='black', align='left', stroke='blue', strokeThickness=0, wordWrap=False, wordWrapWidth=100 ):
		with javascript:
			style = {font:font, fill:fill, align:align, stroke:stroke, strokeThickness:strokeThickness, wordWrap:wordWrap, wordWrapWidth:wordWrapWidth}
			self[...] = new( PIXI.Text( text, style ) )

	def setStyle(self, font='bold 20pt Arial', fill='black', align='left', stroke='blue', strokeThickness=0, wordWrap=False, wordWrapWidth=100):
		with javascript:
			style = {font:font, fill:fill, align:align, stroke:stroke, strokeThickness:strokeThickness, wordWrap:wordWrap, wordWrapWidth:wordWrapWidth}
			self[...].setStyle( style )

	def setText(self, text):
		with javascript:
			self[...].setText( text )

	def updateText(self):  ## private
		with javascript:
			self[...].updateText()

	def updateTexture(self):  ## private
		with javascript:
			self[...].updateTexture()

	def determineFontHeight(self):  ## private
		with javascript:
			return self[...].determineFontHeight()

	def destroy(self, destroyTexture=False):
		with javascript:
			return self[...].destroy( destroyTexture )

