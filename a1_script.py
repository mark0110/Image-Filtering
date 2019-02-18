import MyConv as m
import popupMessage as popup
import compConv as comp
import convSpacialDomain as q1
import Hybrid_Image as hi
import PhaseSwap as ps
import MyCanny as canny


msg = 'Welcome to our Assignment 1!\n\nOur program will display a series of images and textboxs to answer the questions as outlined in the assignment document.\n\nBe advised that the execution time for some of the images is long.\n\nPress Okay to continue...'
popup.popupmsg(msg)

msg = "Instructions:\n\nThe images and textboxs may appear in the back of your current window. If an image is expected, please look around your screen to find the output.\n\nIf the current output is an image, then the next output will not appear until you press any keyboard button (i.e space bar).\n\nIf the current output is a textbox, then it is necessary to to press the okay button to proceed.\n\nPress okay to continue..."
popup.popupmsg(msg)

msg = "2 images will appear next answering the first 2 questions in the first section.\n\nDont forget to press the space bar to display the next images.\n\nPress okay to continue..."
popup.popupmsg(msg)

q1.showImg1()
q1.showImg2()

msg = "The next 3 image's show the outputs for questions 3 4 and 5 from the first section.\n\nThe first image displayed is the convolved image using the code writtent by us (not using the built in command). The second image is the image convolved using the built in command. And finaly the third image will show the difference of the 2 images (or the lack of the difference).\n\nThe execution time is approximately 1:40 minutes.\n\nPress okay to continue..."
popup.popupmsg(msg)

m.myConv()

msg = "Answer for question 4 from section 1:\n\nIs there any difference between the output?\n\nNo difference is observed\n\nPress okay to continue..."
popup.popupmsg(msg)

msg = "Answer for question 5 from section 1:\n\nWhat is observed from the execution time between convolving an image using the 1D or 2D filter?\n\nTo be determined\n\nPress okay to continue..."
popup.popupmsg(msg)

msg = "The next output will be a plot as asked in section 2 that compares the execution time of convolving an image in the spacial and frequency domains\n\nThe execution time is approximetly 00:20 minutes.\n\nPress okay to continue"
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

msg = "Answer for question 2 from section 4:\n\nDescribe the 2 previous images.\n\nTo be determined\n\nPress okay to continue..."
popup.popupmsg(msg)

msg = "The next 2 images are the result of using the code we wrote for the Canny edge detection\n\nThe execution time for the first image is 20 seconds and 3 seconds for the second one.\n\nPress okay to continue..."
popup.popupmsg(msg)

canny.Mycanny("bowl-of-fruit.jpg", 0.04, 5)
canny.Mycanny("3.jpg", 0.04, 5)

msg = "You have reached the end of our Assignment 1\n\nAuthors:\nMark Volfson - 500740834\nMichael Teitelbaum - XXXXXX\n\nThank you for your time!\n\nPress okay to terminate..."
popup.popupmsg(msg)