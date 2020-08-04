# Serial_port_value_save_GUI 
It's a python+pyqt way to catch serial port value.



Sometimes we need to save the messege from the controller by serial port.  
For example, the sensor feedback to arduino,and I send the messege from arduino to computer by serial port: 
  
![img](https://github.com/Ray0124/Serial_port_value_save_GUI/blob/master/serial_port.PNG)    

In this situation.If I want to save 100 data, I dont know which 100 data is best for me.  
If I have a GUI which can show the trend of data in real time , I will exactlly to save the 100 data what I want.  


As for this, my structure is below:  
  
![img](https://github.com/Ray0124/Serial_port_value_save_GUI/blob/master/structure2.PNG)   


My data buffer(default:100, and you can change by UI) and GUI are below:  
  
![img](https://github.com/Ray0124/Serial_port_value_save_GUI/blob/master/data%20buffer.PNG)  
  
![img](https://github.com/Ray0124/Serial_port_value_save_GUI/blob/master/GUI.PNG)  


I seperate my GUI into w.ui(design) and logic.py(function),so it's easy to change design.  
Saving datas will name by count,and they located in the current place.  
Running main.py,and programe will start.  
  
![img](https://github.com/Ray0124/Serial_port_value_save_GUI/blob/master/test.gif)  



PS: In general, the python serial is more slower than the serial of the controller , so I suggest you to set delay function on your controller. 
