THE README THUS FAR:
The goal of this project is to calculate the inverse kinematics movement of a robot with 2 joins as simply as possible with only high school trig.

IMPORTANT: THIS ROBOT HAS 2 JOINS AND BOTH ARMS LEGNTHS ARE THE SAME OR IT WON'T WORK.

Welcome to my project! Here I make a robotic arm that uses inverse kinematics to move around and possibly do a job/function that is to be decided later

How it started: As everyone probably has, I was binge watching MIT maker portfolio videos and realizing how cooked I am compared to these super sweats when I suddenly realized something. I kept on hearing the term "**INVERSE KINEMATICS**", I was suepr intreseted in this as I had absulutely no idea what it was and it was related to hardware, two thing that I like. That's when I hopped on my laptop and I started watching videos and researching inverse kinematics, well it didn't end up to well, cause after trying to understand what co ordinate transoformations are, what end affectors are and how angles are derived from matrixes I realized this was wayyy to complicated for me. 

HOWEVER

I didn't give up there, I decided I would want to make my own way finding the angle in inverse kinematics that I could understand with my high school knowledge. Basically I was limited to using Tan, sine, cosine, and the cosine rule, as those were the only things I knew.

I tried to watch more youtube videos but none of them has videos about arms with 2 joins, one base and one elbox joint. I wanted to start with 2 joints as it would be easy. That's why I had to make up my own method to calculate how to get the angles. This was a very big procces and a read me can't really do it justice but here are some challenges I faced during this

1. It started off with CHAT GPT (didn't work well but gave me a starting idea)
2. It was fairly easy to get the middle angle (elbow joint) with the cosine rule but I was mainly stuggling with finding the base angle as since the middle angle would be there, I would need to calculate projection angle which would require complicated math going against my goal.
3. Thats why I made my triangle isocoleses so I could use trianlge properties to calculate the projection agnle (trust me It will make sense when I explain it below)


THE PROCESS:

**Before I explain this a picutre would be usefull so its easy to understand, hence I will draw a diagram of how the robot looks.*

1. First we need to take an co ordinate input and calculate the distance between it. This is pretty straightforward and can be done with the distance formula. Suppose you pick the point (3,4), to calculate the distance between the origin (the base) and this point it's simply $D^2=x^2+y^2$, where D is distance, and x and y are the side legnths, but since we are starting from the origin, the x and y are zero. For our example the equation would result to $3^2+4^2$ which would be 25. Now that we know d^2, we need to square root that, so the distance in the end is $\sqrt{25}$ which is 5. Now that we know the distance we can move on to the next step.

1. You see the middle angle named middle angle? Now, we need to calculate that. We can calculate this by using the cosine rule which is $a^2=b^2+c^2-2bc·cos(A)$ (see image below)
![Screenshot 2026-06-26 at 13.14.26.png](../../../../var/folders/k4/99cxv25d3rsg_nmstybx4pl40000gn/T/TemporaryItems/NSIRD_screencaptureui_d8UIEE/Screenshot%202026-06-26%20at%2013.14.26.png)
since we want to angle, we can rearange the formula to $cos(A)$ = $(b^2+c^2-a^2)\over2bc$. (See picutre to get what I'm talking about), now we can use our distance a, and our x and y co ordinate to get b and c and we can solve for the angle
2. Now some tricky parts come in, you might have learned that when using sine or cosine etc they are sysmterical so there are 2 anwsers. If you don't know this search it up, but basically cos(10)=x and cos (170) can also be X. This just means there are two possible anwsers to the problem, which is why with the anwser we get we store it in one variable, and we do cos(180-A) to get our second possible anwser and store it in our second variable. 
3.  Finally we need the base angle, instead of calcualting projection angle I use properties of trianngle to find out the base angle. First lets find the normal base angle assuming the robot was a straight line, we can do this with $Angle=$ $tan^-1$ $x\over y$, where x and y and the side lenghts, but in this case the co ordinates. Now obv this angle ignores the bend in the middle arm and to counter act the bend we can do some simple math. Since this robot has both arm legnths the same we can make an isocleles triangle. With basic math we can find the other two legnths, now if we take our tan anlge and substract teh side angle with it we have our base angle that includes the projection. YIPEE I KNOW THAT WAS CONFUSING BUT WE GOT THROUGH IT
4. Finally (last one), we need to calculate the most efficent angle. Remever how we stored two angles for cosine, we now test both of them, by adding the absolute value of solution one to our base angle, and the same with solution 2. the solution that provides the smallest number is used.


Well now that we got that out of the way it's time to talk about the actual process, the instresting bit!

Well... It started of with coding. Obv I had to code the math I explained execpt this was like the first time I was touching python and pycharm and coding in general, so I was kinda lost. I learned you needed to import math, to math. The rest was js writing the operations in python language which took a longggggggggg time. I think the hardest part was getting the absulute value. I had to look that up becuase I didn't know there was a function to get absulute value. After that was done, I started to design which is more of my strong point.
I designieed in onshape and the first thign I did was model the servos I was going to use which were the servo mg 90s, luckily this guy on Reddit had a usefull picture with the dimenstions of the servo so I first made that. Now that that was moddeled I starting making a case around the servo model, Then I made arms which were fairly basic, just connecters and I made it so that the total legnth was 10 cm long. Something I ran into the way of making this was I completely forgot the legnths of the servos itself, I was asuming they were 0. I had to incooperate this and then rethink and remodel my design accordingly.