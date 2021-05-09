import cv2           #to detect the color at a particular pixels
                     #stores values in bgr format instead of rgb

import pandas as pd  

# --------------------------------------------------------------------------

img_path = 'colorpic.jpg'
csv_path = 'colors.csv'

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

# reading csv file
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']  #creating index for the color components
df = pd.read_csv(csv_path, names=index, header=None)   #creating a data frame to read the csv file

num=5
color_loc=1
color_component=1
choose_component='R'


print(RED,BOLD,"\t\t\t\t[1.] first {} colors of the csv file:\n",RESET.format(num),df.head(num))

print(RED,BOLD,"\n \t\t\t\t[2.] Total numbers of colors in the csv file is:",RESET,len(df))
print(RED,BOLD,"\n \t\t\t\t[3.] color components of the given color: \n",RESET,df.loc[color_loc])
print(RED,BOLD,"\n \t\t\t\t[4.] {} component of the given color:",RESET.format(choose_component),df.loc[color_component,'R'])
print(RED,BOLD,RESET)

# reading image
img = cv2.imread(img_path)
img = cv2.resize(img, (700,500)) #resizing the image

#declaring global variables
clicked = False
r = g = b = xpos = ypos = 0

#function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R,G,B):
	minimum = 1000
	for i in range(len(df)):
		
        #differece of RGB components with values stored in csv file
		d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B'])) 
		
		#findig the absolute sum 
		#it is the color name when sum is minimum
		if d <= minimum:
			minimum = d
			cname = df.loc[i, 'color_name']

	return cname

#function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x
		ypos = y
		b,g,r = img[y,x]
		b = int(b)
		g = int(g)
		r = int(r)
		print("co-ordinated of the clicked part: \n x= ",x, " y= ", y)
		print("and the pixels at x and y are :\n",r," ",g," ",b)

#print(clicked,r,g,b,xpos,ypos)

# creating window
cv2.namedWindow('image')     
#
cv2.setMouseCallback('image', draw_function) #binding the function with mouse

while True:
	#display the image
	cv2.imshow('image', img)
	if clicked:
		#cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
		cv2.rectangle(img, (20,20) , (600,60), (b,g,r), -1)

		#Creating text string to display( Color name and RGB values )
		text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
		#cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
		cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)

		#For very light colours we will display text in black colour
		if r+g+b >=600:
			cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == ord('e'):
		break

cv2.destroyAllWindows()
