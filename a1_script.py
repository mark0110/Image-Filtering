import MyConv as m
import popupMessage as popup
import compConv as comp
import convSpacialDomain as q1
import Hybrid_Image as hi
import PhaseSwap as ps
import MyCanny as canny
import Q1_5 as q15

msg = "CPS843 Assignment 1\n\nAuthors:\nMark Volfson - 500740834\nMichael Teitelbaum - 500747561\n\nThank you for your time!\n\nPress okay to continue..."
popup.popupmsg(msg)

msg = 'Welcome to our Assignment 1!\n\nOur program will display a series of images and textboxes to answer the questions as outlined in the assignment document. Be advised that the execution time for some of the images is long. \n\nPress Okay to continue...'
popup.popupmsg(msg)

msg = "Instructions:\n\nThe images and textboxes may appear in the back of your current window. If an image is expected, please look around your screen to find the output.If the current output is an image, then the next output will not appear until you press any keyboard button (i.e space bar).If the current output is a textbox, then it is necessary to to press the okay button to proceed.\n\nPress okay to continue..."
popup.popupmsg(msg)

msg = "2 images will appear next answering the first 2 questions in the first section. Dont forget to press the space bar to display the next images.\n\nPress okay to continue..."
popup.popupmsg(msg)

q1.show_img1()
q1.show_img2()

msg = "The next 3 image's show the outputs for questions 3 4 and 5 from the first section. The first image displayed is the convoluted image using the code written by us (not using the built in command). The second image is the image convoluted using the built in command. And finally the third image will show the difference of the 2 images (or the lack of the difference).\n\nThe execution time is approximately 30 seconds.\n\nPress okay to continue..."
popup.popupmsg(msg)

m.my_conv()

msg = "Answer for question 4 from section 1:\n\nIs there any difference between the output?\nNo difference is observed\nPress okay to continue..."
popup.popupmsg(msg)

time = q15.timeCalc()

msg = "Answer for question 5 from section 1:\n\nWhat is observed from the execution time between convoluting an image using the 1D or 2D filter?\nExecution time using 2 1D Gaussian kernels:\n" + \
    str(time[0])[:5]+" ms\nExecution time using a 2D Gaussian kernel:\n"+str(time[1])[:5] + \
    " ms\n\nObservation:\nIt takes approximately twice as long to add a Gaussian kernel using 2 1D kernels then using a 2D kernel.\n\nPress okay to continue..."
popup.popupmsg(msg)

msg = "The next output will be a plot as asked in section 2 that compares the execution time of convoluting an image in the spacial and frequency domains\n\nThe execution time is approximately 00:20 minutes.\n\nPress okay to continue"
popup.popupmsg(msg)

comp.comp()

msg = "Answer for question 3 from section 2:\n\nWhat can be observed from the graph?\n\nAs seen in the graph, the convolution of an image is faster in the spacial domain when its size is small. For bigger images, its better to perform the convolution in the frequency domain\n\nPress okay to continue..."
popup.popupmsg(msg)

msg = "The next image is the output from section 3 of the assignment\n\nPress okay to continue..."
popup.popupmsg(msg)

hi.hi()

msg = "The next 2 images is the output for section 4 of the assignment\n\nPress okay to continue..."
popup.popupmsg(msg)

ps.fSwap()

msg = "The next 2 images are the result of using the code we wrote for the Canny edge detection\n\nThe execution time for the first image is 20 seconds and 3 seconds for the second one.\n\nPress okay to continue..."
popup.popupmsg(msg)

canny.my_canny("bowl-of-fruit.jpg", 0.04, 5)
canny.my_canny("3.jpg", 0.04, 5)

msg = "You have reached the end of our Assignment 1\n\nAuthors:\nMark Volfson - 500740834\nMichael Teitelbaum - 500747561\n\nThank you for your time!\n\nPress okay to terminate..."
popup.popupmsg(msg)
