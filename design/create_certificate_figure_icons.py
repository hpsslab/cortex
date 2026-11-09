from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR
from pptx.oxml.xmlchemy import OxmlElement

OUT=Path(__file__).parent
r=Presentation();r.slide_width=Inches(16);r.slide_height=Inches(7.4)
s=r.slides.add_slide(r.slide_layouts[6])
C={'navy':'21314D','ink':'253345','muted':'596575','line':'D7DFE6','paper':'F5F7F9','rust':'A64B2A','blue':'235C83','white':'FFFFFF'}
def color(c):return RGBColor.from_string(C.get(c,c))
def shape(kind,x,y,w,h,fill=None,line=None):
 a=s.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
 if fill:a.fill.solid();a.fill.fore_color.rgb=color(fill)
 else:a.fill.background()
 if line:a.line.color.rgb=color(line)
 else:a.line.fill.background()
 return a
def box(x,y,w,h,fill,line=None):return shape(MSO_SHAPE.RECTANGLE,x,y,w,h,fill,line)
def text(x,y,w,h,txt,size=18,fill='ink',bold=False,font='Aptos'):
 a=s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h));tf=a.text_frame;tf.word_wrap=True
 tf.margin_left=tf.margin_right=0;tf.margin_top=tf.margin_bottom=0
 for i,line in enumerate(txt.split('\n')):
  p=tf.paragraphs[0] if i==0 else tf.add_paragraph();p.text=line;p.font.name=font;p.font.size=Pt(size);p.font.bold=bold;p.font.color.rgb=color(fill);p.space_after=Pt(5)
 return a
def line(x1,y1,x2,y2,c='navy',width=2):
 a=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2));a.line.color.rgb=color(c);a.line.width=Pt(width);return a
import sys
iteration=int(sys.argv[1]) if len(sys.argv)>1 else 3
r.slide_height=Inches(7)
box(0,0,16,7,'white')
text(.55,.3,14,.3,'COLORADO SCHOOL OF MINES  /  CERTIFICATE OF EXPERIENCE',12,'rust',True)
text(.55,.88,15,.7,'A path into semiconductor manufacturing',32,'navy',True,'Georgia')
# The first three stages are learning experiences; placement is the intended outcome.
xs=[.55,4.38,8.21,12.04];w=3.41
text(.55,1.85,9,.32,'EXPERIENTIAL LEARNING',12,'rust',True)
line(.55,2.28,11.62,2.28,'line',1.5)
text(12.04,1.85,3.4,.32,'PROGRAM GOAL',12,'rust',True)
for n,x in enumerate(xs):
 final=n==3 and iteration>=2
 bg='navy' if final else 'paper';fg='white' if final else 'navy'
 box(x,2.58,w,3.62,bg)
 if iteration<3:box(x,2.58,w,.04,'rust' if n==3 else 'navy')
 text(x+.2,2.82,.5,.32,f'0{n+1}',14,'white' if final else 'rust',True)
 label=['Coursework','Hands-on learning','Industry capstone','Industry placement'][n]
 text(x+.2,5.25,w-.4,.43,label,19,fg,True)
 text(x+.2,5.79,w-.4,.3,['3 credits','3 credits','6 credits','Semiconductor manufacturing'][n],11,'D3DCE6' if final else 'muted')
 if n<3:shape(MSO_SHAPE.CHEVRON,x+w+.12,4.03,.18,.29,'rust')
# Coursework: open book with a semiconductor die.
x=xs[0];y=3.55
for side in [0,1]:
 bx=x+.58+side*1.13
 box(bx,y,1.12,1.12,'white','line')
 for dy in [.22,.4,.58,.76]:line(bx+.15,y+dy,bx+.92,y+dy,'line',1)
line(x+1.71,y-.06,x+1.71,y+1.24,'navy',2)
box(x+1.37,y+.27,.68,.64,'navy')
if iteration>=2:
 line(x+.58,y+1.12,x+1.71,y+1.3,'navy',2)
 line(x+1.71,y+1.3,x+2.83,y+1.12,'navy',2)
 line(x+1.71,y-.06,x+1.71,y+1.3,'navy',2)
for d in [.12,.33,.54]:
 line(x+1.37+d,y+.15,x+1.37+d,y+.27,'blue',1.5)
 line(x+1.37+d,y+.91,x+1.37+d,y+1.03,'blue',1.5)
# Lab: actual headset view, cropped around the wafer and trainee's hands.
a=s.shapes.add_picture(str(OUT.parent/'assets/images/arca-spin-coating.jpg'),Inches(xs[1]+.2),Inches(3.42),width=Inches(3.01),height=Inches(1.49))
a.crop_top=.06;a.crop_bottom=.06
# Capstone: board and traces (native editable vectors).
x=xs[2]
box(x+.49,3.44,2.43,1.48,'white','line')
box(x+1.28,3.84,.72,.64,'navy')
for yy in [3.97,4.15,4.33]:
 line(x+.72,yy,x+1.28,yy,'blue',1.5);shape(MSO_SHAPE.OVAL,x+.66,yy-.04,.08,.08,'rust')
 line(x+2,yy,x+2.65,yy,'blue',1.5)
for xx in [.76,1.06,2.27,2.56]:box(x+xx,3.61,.15,.13,'rust')
for xx in [.75,1.06,2.27,2.56]:box(x+xx,4.64,.15,.1,'blue')
# Manufacturing: fab building and wafer, distinct from the capstone board.
x=xs[3];fg='white' if iteration>=2 else 'navy';bg='navy' if iteration>=2 else 'white'
box(x+.52,4.01,2.36,.89,None,fg)
box(x+.79,3.58,1.79,.43,None,fg)
for xx in [.7,1.2,1.7,2.2]:box(x+xx,4.24,.29,.3,'D3DCE6' if iteration>=2 else 'blue')
shape(MSO_SHAPE.OVAL,x+1.94,3.16,.97,.97,bg,fg)
for d in [.24,.48,.71]:
 line(x+1.94+d,3.3,x+1.94+d,3.98,fg,.8)
 line(x+2.08,3.16+d,x+2.77,3.16+d,fg,.8)
if iteration<3:
 text(.55,6.48,12,.3,'Coursework → practice → project → placement',14,'muted')
r.core_properties.title='Certificate pathway: learning to industry placement'
r.core_properties.author='Colorado School of Mines'
for item in s.shapes:
 sp=item._element.find('{http://schemas.openxmlformats.org/presentationml/2006/main}spPr')
 if sp is not None:sp.append(OxmlElement('a:effectLst'))
 for ref in item._element.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}effectRef'):ref.set('idx','0')
r.save(OUT/f'certificate-pathway-iteration-{iteration}.pptx')
if iteration==3:r.save(OUT/'certificate-pathway.pptx')
