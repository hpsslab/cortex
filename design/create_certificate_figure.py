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
# Photo-led pathway. Images remain separate, editable PowerPoint picture objects.
r.slide_height=Inches(7.8)
box(0,0,16,7.8,'white')
text(.55,.3,14,.3,'CORTEX  /  COLORADO SCHOOL OF MINES',12,'rust',True)
text(.55,.85,15,.95,'Certificate of Experience on Semiconductor Training Readiness Through Experiential Learning',26,'navy',True,'Georgia')
xs=[.55,4.38,8.21,12.04];w=3.41
text(.55,1.88,9,.32,'EXPERIENTIAL LEARNING',12,'rust',True)
line(.55,2.28,11.62,2.28,'line',1.5)
text(12.04,1.88,3.4,.32,'PROGRAM GOAL',12,'rust',True)
paths=[OUT/'source-images/coursework.jpg',OUT.parent/'assets/images/arca-spin-coating.jpg',OUT/'source-images/capstone.jpg',OUT/'source-images/manufacturing.jpg']
for n,(x,path) in enumerate(zip(xs,paths)):
 final=n==3;fg='white' if final else 'navy'
 box(x,2.59,w,4.58,'navy' if final else 'paper')
 # Fit pictures by cropping rather than stretching. Focus remains on the work and people.
 a=s.shapes.add_picture(str(path),Inches(x),Inches(2.59))
 a.left=Inches(x);a.top=Inches(2.59);a.width=Inches(w);a.height=Inches(2.38)
 iw,ih=a.image.size;ratio=iw/ih;target=w/2.38
 if ratio>target:
  crop=(1-target/ratio)/2;a.crop_left=crop;a.crop_right=crop
 else:
  crop=(1-ratio/target)/2;a.crop_top=crop;a.crop_bottom=crop
 if n==3:
  # Zoom into the fab technicians while preserving the picture aspect ratio.
  a.crop_left=.13;a.crop_right=.13
  vertical=(1-(iw/ih)*.74/target)/2
  a.crop_top=vertical;a.crop_bottom=vertical
 box(x+.15,2.74,.43,.35,'navy')
 text(x+.22,2.79,.32,.25,str(n+1).zfill(2),11,'white',True)
 text(x+.17,5.23,w-.34,.43,['Coursework','Hands-on learning','Industry capstone','Industry placement'][n],19,fg,True)
 text(x+.17,5.88,w-.34,.88,[
  'Build a foundation in devices, materials, physics, and computing.',
  'Practice microelectronics processing with laboratory work and SMILE tools.',
  'Design, build, and test a project with a semiconductor industry partner.',
  'Bring course, lab, and project experience into an engineering role.'
 ][n],14,'D3DCE6' if final else 'ink')
 text(x+.17,6.77,w-.34,.27,['3 credits','3 credits','6 credits','Semiconductor manufacturing'][n],11,'D3DCE6' if final else 'muted')
 if n<3:shape(MSO_SHAPE.CHEVRON,x+w+.12,4.4,.18,.3,'rust')
# Notes carry attribution without adding labels to the graphic itself.
s.notes_slide.notes_text_frame.text = """Photo sources and intended use:
1. Coursework: ThisIsEngineering, Engineers Working in Office. https://www.pexels.com/photo/engineers-working-in-office-3912378/ — Pexels License https://www.pexels.com/license/ . Representative engineering collaboration, not a photo of Mines students.
2. Hands-on: ARCA spin-coating demonstration from supplied SMILE material. Retained project image.
3. Industry capstone: ThisIsEngineering, Woman Working on Computer Hardware. https://www.pexels.com/photo/woman-working-on-computer-hardware-19895718/ — Pexels License. Representative electronics project work, not a photo of a Mines capstone team.
4. Industry placement: Carol M. Highsmith, Kenneth Rudolph and John Hojnacki at Intel's wafer fabrication facility, Chandler, Arizona, 14 November 2018. Library of Congress, https://www.loc.gov/item/2018703083/ . Rights advisory: No known restrictions on publication. Cropped for layout. This image illustrates semiconductor employment; it does not identify a program partner or placed graduate.
The final stage is the program goal. Course credits remain 3 + 3 + 6.
"""
r.core_properties.title='CORTEX: Certificate of Experience on Semiconductor Training Readiness Through Experiential Learning'
r.core_properties.author='Colorado School of Mines'
for item in s.shapes:
 sp=item._element.find('{http://schemas.openxmlformats.org/presentationml/2006/main}spPr')
 if sp is not None:sp.append(OxmlElement('a:effectLst'))
 for ref in item._element.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}effectRef'):ref.set('idx','0')
r.save(OUT/'certificate-pathway.pptx')
