# Recognito
## Description
The **Recognito** web application acts as an **emotion detector**, 
allowing people to identify their emotions by looking at their faces.
               By keeping suspects on this project's radar, the web app will serve 
               as a **truth-finder** and **distinguisher between an object and a face** for the cops. 
               <br>
                Through its monitoring, this project
                will be able to see every emotion the suspect exhibits. Every 
                emotion will be tracked. After 24 hours, the **most noted emotion** 
                will be displayed after this app has been keeping a watchful eye 
                on culprits. <br>
                As an example-if, the most observed emotion is 
                **happiness**, which means the culprit is not hiding anything and 
                is confident that he is not wrong. When most observed emotion 
                turns into **fear**, it likely means he has a secret and is not 
                telling anyone. There is no doubt that these predictions are 
                accurate because a person who is guilty will definitely become 
                nervous, and this nervousness,fear will definitely be evident on 
                his face. 
                <br>It is almost impossible for a detective to constantly watch a 
                criminal and his emotions, but this web app can do as much as it 
                can. In addition, it eliminates the need to hire additional employees
                 for observation. 
## Features
1. It acts as a **distinguisher** between various objects and faces
2. Whenever **object other than a face** is detected in line of sight of a camera, camera screen **automatically gets freezed** and unblocks only after face comes again in line of sight of camera.
3. Whenever there is a face it **detects emotions** and displays it.
4. Most observed emotion is displayed.
5. Other than the emotion of a person, **race** is also displayed in result section.

## Installation steps
**Note:** All the steps mentioned below are for **Windows** Operating System and uses latest version of **Python: 3.10.4**
1. Clone this Repo using git clone <a href="https://github.com/shubhi-arora/face-recognition.git">https://github.com/shubhi-arora/face-recognition.git<a>
2. Go to the directory where the project is cloned and then to face-recognition folder.
3. Open the project folder using **Visual Studio Code**.
4. Make sure latest version of Python setup is already installed in your computer. If not, then download and install it from <a href="https://www.python.org/downloads/">here</a> for Windows.
5. Open the terminal and run following commands to import libraries and install various packages.
  <ul>
<li>pip install opencv-python</li>
<li>pip install cv</li>
<li>pip install Flask</li>
<li>pip install matplotlib</li>
<li>pip install numpy</li>
<li>pip install DeepFace</li>
<li>pip install Counter</li>
  </ul>
  
  
6. Open the **app.py** file as initiation of project will be done through it.<br>
7. Open the **terminal** and run: <br>py -u path_of_app.py_file<br> If this command doesn't works then try writing:<br> python -u path_of_app.py_file 
<br>
OR
<br>
Run the app.py file in terminal directly.
  <br>
  
  
8. Click on the local host link of port 5001 received in the terminal.

## Steps To Use
1. Click on the Detect button as shown on the homepage.
2. Keep your face in line of sight of camera.
3. As soon as the face gets away from camera and other object appears, camera screen gets blocked automatically.
4. It gets unblock only when face comes again in front of a camera.
5. As per the face emotions, emotions will be displayed of a person.
6. After pressing 'q' twice on the keyboard continuously camera stops and result of most observed emotion and race is displayed.





## Demo
**Homepage**
  <br>
![](images/homepage.png)
  <br>
**About**
  <br>
![](images/about1.png)
  <br>
**Features and Calculations/Algorithm**
  <br>
 ![](images/about2.png)
  <br>
**Contact Info**
  ![](images/contact.png)
  
## Calculations/Algorithm
  1. Store each and every occurrence of emotion value into a **map or dictionary**.
  2. **Count** the occurrence of each emotion. 
  3. **Traverse** through the map and find the maximum occurence count emotion.
  4. **Display** the result and proceed the same for race.
## Tech-Stack Used
<ul>
<li>Python</li>
<li>OpenCV Library</li>
<li>Flask</li>
<li>HTML</li>
<li>CSS</li>
<li>Jupyter Notebook</li>
</ul>
  
  
## Future Scope
  1. Recognito can be taken to the **METAVERSE** in a way such that culprits in a cell will feel that Cops are there in front of them in the jail and so culprits will be forced to sit in front of the camera of this Recognito software, and this will ensure that culprits do not act over-smarter and not play any bad tactics . But in reality, no cops will be there around the culprits. Therefore, it is possible through **metaverse** to make policemen available in front of culprits without actually having them in reality.
  2. More advancements can be made in this project in the near future such as it can detect face color, hair color, face shape etc.
  3. Other than this, it can have the capability to detect any unwanted dangerous equipment hided inside the culprits body.
  
## Connect with me:
<a href="mailto:arora.shubhi0565@gmail.com"><img align="left" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZjPRN5UbMCaEN9Y8SuOMd6z70AZsW8wCpXw&usqp=CAU" width=40 height=40/></a>  
  <br>
 <a href="https://www.linkedin.com/in/shubhi-arora-15a549205/"><img align="left" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAllBMVEUMZMX///8AYcQAWcFDf8nL3PIAWrzQ3vMAYcI0eclZjtAucslAgsz6/v3x9/sgbclOhM8AX8QAYsAAX70AV70AWMLm7vgAXb4sdsw5fsoRbsVmltK6z+iUt+AMZcGDrN3c6fNvnddiltWqwuPA0+r0+vyOrt+lweR9pduuyueUst9Lh81pldd1mtYdbcunxOXO4u7Z4fGRyVlRAAAEKUlEQVR4nO3ce1faMBzG8SblEpSCiUUuQrkMhsCc+v7f3Ko4KjW/yLY0WXOez9mf4Ml3vSW1NYoAAAAAAAAAAAAAAAAAAAAAAAAAAADgYiriIsqU72FURcapGnXHk5aMue+xVCCT6n56x960Z2OpMt8jsozz+Xve0Xqc+h6SXbKzYOeSfex7UBap+J591lThHI3awPxw5KGcVFUj0RayaRrI6UaUj8GTpfA9NivknApkvTC2YdwjC9lc+h6dBWpFB7JFCIXx1FDIRr6HZ0Fq2EkZewjgXNMnLhVH34a+x/fPeMdYOK3/gchvTIFsXf/ZKR+bC+u/DcW1cS/d1f84jFobU+H3ANYXadNU2PU9PAvkd0Ngz/forMgMhU/1P5Xm4h0ZmHQCOAzz68WEPNdsg9iE+ZH4QATeBTApPYqf9PvoKIh99E2qOxQ3jVvf47JHDT5fMl5GAQW+3tNvnF/4N3shwrhJc8Ljw/Q0Q13MJ4GcRc8IORjP99vZfpWlQe2gH3EZx7Gs/4IJAADqQ3DJX/+FM38vqHyKlA5Hhx+Pj49X43468P34CheEiz9Z+pTMlrvFaQ6YbNrblRpKf6vNbHRNKX2yT/kwSVd5XluzGGs//Ew9NfIGS/RYs3X2yUGzp7dpnMYu+zPql1mbp46f+XxeSCkVxrpt8+bmWJgJOTPeYP7m5QkWi4Wye0d94t3m3sNmtFao5OyLvle7zPnRaKlQCb6+IDBfXvddJ1oq5BH5WE7JXd/xwWilUKnJpYGM9a7dPk5mpfCWP18cmO+okdOtaKVwYHxm5ZP1wOWNPBuFneUfBTK2dHkzyEbhwfirco3NxOF+aqPw8rPMbzuHV34bhX+h4e6q6KnQ4ZM6ngrZyNlG9FXo7hfMvgp7zt7o8FXIDq52U2+FznbTKgovmgAsalq4mB0mQqjJYfvler98o6sWhevuYPh2C5jz4WD1ReMPR4soi4W91dmtXy7MK469o7mpvcLn8nRaSWPi9PzH/++FCXvW3LuXpoXxi6MllK1tqHtGLBMd0zccLYNtFR60W8T0wkqv7yTQVuGTfpfLuvRXkms3sxo7hQlx/yy7NayOO3Uq3MXExY148PFY6OZyYafwihqsXNJfGteoMCGXQoYfzxo1KmxSO2kkJvTLcXUq3BreraFnp3UqNLwT3aJPpnUqPNBjTV+CKDScFVv0t+pUaLiytegXq1BoCQoLKNRDYfVQWEChHgqrh8ICCvVQWD0UFlCoh8LqobCAQj0UVg+FBRTqobB6KCygUA+F1UNhAYV6KKweCgso1ENh9VBYQKEeCquHwkKAhe1SIf2UoaFwSP+/dB29FtTvUsbnH+Q3VxTDmxOq+zffskqJiOtFpZda+OV/M6uQKepLof0NWAAAAAAAAAAAAAAAAAAAAAAAAAAAgAr8Aj5RWY0PDbn2AAAAAElFTkSuQmCC" width=40 height=40/></a>  



