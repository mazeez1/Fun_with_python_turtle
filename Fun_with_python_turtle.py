
#Lab 8: Graphing With Turtle Graphics

# Moses Azeez            
# mma348                 
from random import *

from turtle import *

class graph:

    def __init__( self):

        self.title = 'blank graph'
        self.xlabel = "X axis"
        self.ylabel = "Y axis"
        self.x_min = 1 
        self.x_max= 10 # default x axis
        self.legend_a = None
        self.legend_b = None
        self.speed = 2
        self.y_min = 1
        self.y_max = 8 # default y axis
        self.plots = None  # this is a python list of about 5 elements
        self.color = 'black'
        self.style = None
        self.x_values = None
        self.y_values = None
        self.xnd_values = None
        self.ynd_values = None
        self.color_nd = 'black'

    def __str__(self):
        s =  "title: " + str(self.title)+"\nxlabel: " + str(self.xlabel)+"\nylabel: " + str(self.ylabel)+"\nx min: "+ str(self.x_min)+"\nx max: "+str(self.x_max)+"\n"
        s2= "\ny min: "+str(self.y_min)+"\ny max: "+str(self.y_max)+ "\nplots: " +str(self.plots) + "\nturtle speed: " + str(self.speed)
        s3 = s+s2
        return s3

    def debugDump( self ):
        print( "\n---------------\nGraph Class\n" )
        print("----------------")
        print( "x points id", id( self.x_values ) )
        print( "y points id", id( self.y_values) )
        print( "xlabel id", id(self.xlabel ))
        print( "ylabel id", id(self.ylabel ))
        print( "title id", id(self.title) )
        print(" x points id", type( self.x_values))

        if self.x_values == None:
            print("\nThis is an empty Graph class\n")

    def draw(self):
        #draw the graph rectangle
        
        speed( self.speed )
        penup()
        goto( -260, 250)
        pendown()

        s = 475         # side length
        for side_count in range(4):
          forward( s )  # four sides, turn 90 deg at corners
          right( 90 )
        
        #The title
        title = str(self.title)
        penup()
        goto( -260, 250)
        pendown()
        title = str(self.title)
        write( "     \t" + str(title), font=("Comic-Sans", 16, "normal") )   # default font and font size
        
        penup()
        goto( -380,220)
        pendown()

        #Y axis
        penup()
        goto( -250, -210)
        pendown()

        yt = int(-290)
        yr = int(-200)

        Y = round(self.y_min,2)
        Dif = self.y_max - self.y_min
        for i in range(8):
            Yst = str(Y)
            part = Dif/7
            penup()
            goto( yt, yr)
            pendown()
            write( str(Y) + " _____", font=("Comic-Sans", 9, "normal") )
            yr = yr + 64
            Y = round(Y + part, 2) #GROWTH OF THE Y AXIS.  IMPORTANT


        penup()
        goto( -380,40)
        pendown()
        #label data, important
        ylabel  = str(self.ylabel)
        write( ylabel , font=("High Tower Text", 12, "bold") )   # default font and font size
            
        penup()
        goto( -250, -270)
        pendown()

        xt = -200
        xr = -250

        X = round(self.x_min,3)
        Dif = self.x_max - self.x_min
        #X axis data points
        for i in range(5):
            Xst = str(X)
            part2 = Dif/4
            penup()
            goto( xt, xr)
            pendown()
            write( str(X) + " ", font=("Comic-Sans", 9, "normal") )
            xt = xt + 96
            X = round(X + part2, 2)  #GROWTH OF THE X AXIS.  IMPORTANT

        xt = -200
        xr = -226
        xy = float(0.00)
        # create lines/indents for graph data points
        for i in range(5):
            penup()
            goto( xt, xr)
            pendown()
            write( " |  ", font=("Comic-Sans", 9, "normal") )
            xt = xt + 99

        penup()
        goto( -90, -275)
        pendown()
        #label of the x axis, important 
        xlabel  = str(self.xlabel)
        write( xlabel , font=("High Tower Text", 12, "bold") )   # default font and font size
            
        #Starting point before graphing 
        penup()
        goto( -261, -228)
        pendown()
        start_point  = str("O")
        write( start_point , font=("Comic-Sans", 5, "bold") )
        penup()
        goto( -280, -245)
        write( "(0,0) ", font=("Comic-Sans", 9, "bold") )
        pendown()
        
        #IF NO DATA IS FOUND
        if self.y_values == None or self.x_values == None:
            penup()
            goto( -240, -205)
            pendown()
            write( "NO DATA FOUND.  PLEASE ENTER PLOT DATA" , font=("Comic-Sans", 6, "normal") )
            hideturtle()
            return

        #plot first graph.  
        ren = len(self.x_values)
        #Dimensions in Pixels of graph
        x_max_pixel = 475
        y_max_pixel = 475

        scale_x = x_max_pixel /  self.x_max
        scale_y = y_max_pixel / self.y_max

        penup()
        goto(-260,-225)
        pendown()
        
        start_x = -260
        start_y =  -225
        #plot first line
        color ('black')
        
        draw_x = self.x_values[0] * scale_x + start_x - 2
        draw_y = self.y_values[0] * scale_y + start_y - 2
        penup()
        goto(draw_x,draw_y)
        color(self.color)
        pendown()
       
        
        for r in range (ren):
                 
                draw_x = self.x_values[r] * scale_x + start_x - 2
                draw_y = self.y_values[r] * scale_y + start_y - 2 
                
                g = float(draw_y * 0.15)
                draw_y = self.y_values[r] * scale_y + start_y - 2 +(g)
                print(draw_x, draw_y)
                penup()
                goto( draw_x, draw_y)
                pendown()
                circle( 3)


        penup()
        goto(-260,-225)
    
        for r in range (ren):
                draw_x = self.x_values[r] * scale_x + start_x - 2
                draw_y = self.y_values[r] * scale_y + start_y - 2
                print(draw_x, draw_y)
                goto( draw_x, draw_y)
                pendown()

        #first legend
        penup()
        goto( -252, 236)
        pendown()
        write( str(self.legend_a) + "---", font=("Comic Sans MS", 7, "normal") )
        penup()
        goto( -252, 224)
        pendown()
        write( "Experimental O", font=("Comic Sans MS", 7, "normal") )
 

        
        #IF THERE IS NO 2ND DATA PLOT FOUND
        if self.ynd_values == None or self.xnd_values == None:
            hideturtle()
            return

        #Swap equations

        self.x_values = self.xnd_values
        self.y_values = self.ynd_values

        #plot second line
        penup()
        goto(-260,-225)
        pendown()
        color('black')
        
        draw_x = self.x_values[0] * scale_x + start_x - 2
        draw_y = self.y_values[0] * scale_y + start_y - 2
        
        penup()
        color (self.color_nd)
        goto( draw_x, draw_y)
        pendown()
  
        for r in range (ren):

            draw_x = self.x_values[r] * scale_x + start_x -2 
            draw_y = self.y_values[r] * scale_y + start_y -2 - (draw_y * 0.08)
            #for debugging.  Prints the pixel corridinates of the x and y labels
            print(draw_x, draw_y)
            penup()
            goto( draw_x, draw_y)
            pendown()
            s =  8            # side length
            setheading( 90 )   # point up or north
            right( 30 )        # three sides, turn 120 degrees at each corner
            forward( s )
            right( 120 )
            forward( s )
            right( 120 )
            forward( s )
            
        penup()
        goto(-260,-225)
        
        for r in range (ren):
                draw_x = self.x_values[r] * scale_x + start_x - 2
                draw_y = self.y_values[r] * scale_y + start_y - 2
                print(draw_x, draw_y)
                goto( draw_x, draw_y)
                pendown()


        # second legend
        
        penup()
        goto(  -253, 210)
        pendown()
        write( str(self.legend_b) + "---", font=("Comic Sans MS", 7, "normal") )
        penup()
        goto( -253, 200)
        pendown()
        write( "Experimental: △", font=("Comic Sans MS", 7, "normal") )

        speed(1)

        
        #Credits
        penup()
        goto( -45, 350)
        pendown()
        color('black')
        write( "Coded By", font=("arial", 11, "bold") )
        penup()
        goto( -410, 330)
        pendown()
    
        color(self.color)
        write( "\t\tMoses Azeez \t\t\t\t", font=("Fixedsys", 11, "bold") )   # default font and font size
        color(self.color_nd)
        penup()
        goto( 150, 330)
        pendown()
        write( "Jin Joo", font=("Tempus Sans ITC", 11, "bold") )

        color('black')

        hideturtle()

    def add_plot(self, plot_data):
        #This Method passes all the data attributes of a plot class to the graph class
        pass_over = plot_data
        self.title = pass_over.title
        self.xlabel = pass_over.xlabel
        self.ylabel = pass_over.ylabel
        self.x_min = pass_over.x_min
        self.y_min = pass_over.y_min
        self.y_max = pass_over.y_max
        self.x_max= pass_over.x_max
    
        self.plots = pass_over.x_values + pass_over.y_values
        self.color = pass_over.color
        self.color_nd = pass_over.color_nd
        self.style = pass_over.stlye
        self.x_values = pass_over.x_values
        self.y_values = pass_over.y_values
        self.color_nd = pass_over.color_nd
        self.xnd_values = pass_over.xnd_values
        self.ynd_values = pass_over.ynd_values
        self.legend_a = pass_over.legend_a
        self.legend_b = pass_over.legend_b

class plot():

    def __init__( self):

        #The x and y values and the one for the second point must be in ascending order(just like in octave/matlab) and 5 values
    
        self.x_values = [1000,2000,3000,4000,5000]
        self.y_values = [0.048,0.05341,0.0595751,  0.06107,0.0641081]

        self.xnd_values = [1000,2000,3000,4000,5000]
        self.ynd_values = [0.094,0.115,0.124099, 0.13013,0.13817]
        

        
        self.legend_a = "Quick Sort Theory"
        self.legend_b = "Merge Sort Theory"
        #You can change the colors as well, but make sure they're in quotes and have correct spelling
        self.color = 'blue'
        self.color_nd = 'red'

        self.y_max = None
        self.x_max = None


        #For max values
        if self.x_values[4] >= self.xnd_values[4]:
            self.x_max = self.x_values[4]
        else:
            self.x_max = self.xnd_values[4]
        
        if self.y_values[4] >= self.ynd_values[4]:
            self.y_max = self.y_values[4]
        else:
            self.y_max = self.ynd_values[4]

        #for min values

        if self.x_values[0] <= self.xnd_values[0]:
            self.x_min = self.x_values[0]
        else:
            self.x_min = self.xnd_values[0]
        
        if self.y_values[0] <= self.ynd_values[0]:
            
            self.y_min = self.y_values[0]
        else:
            self.y_min = self.ynd_values[0]

        self.stlye = 'point'
        self.title = "Comparing Runtimes of Functions "  #works as data name
        self.xlabel = "Random List Length(n)"
        self.ylabel = "Runtime(s)"
        
    def __str__( self ):
        s = "plot class\ntitle: "+str(self.title)+"\nx points: "+str(self.x_values)+"\ny points: "+str(self.y_values)+"\ncolor: "+str(self.color)+"\nstyle: "+str(self.stlye)
        
        return s
    
    def debugDump( self ):
        print( "\n---------------\nPlot Class\n" )
        print("----------------")
        print( "x points id", id( self.x_values ) )
        print( "y points id", id( self.y_values) )
        print( "style id", id(self.stlye) )
        print( "xlabel id", id(self.xlabel ))
        print( "ylabel id", id(self.ylabel ))
        print( "title id", id(self.title) )
        if self.title == "Search algo":
            print("\nThis is the default plot class\n")


print("CREATE EMPTY GRAPH")
d = graph()
print(d)
print("CREATE EMPTY PLOT")
f = plot()
print(f)

#Edit these.  Change the values.


#print("DEBUG DUMP PLOT")
#f.debugDump()

#print("DEBUG DUMP GRAPH")
#d.debugDump()

print("PASS EMPTY PLOT TO EMPTY GRAPH")

#d.add_plot(f)
print(d)

print("MAX AND MIN FOR Y")
print(d.y_min)
print(d.y_max)
print("MAX AND MIN FOR X")
print(d.x_min)
print(d.x_max)
d.add_plot(f)
d.draw()
