# Serial_port_value_save_GUI 
It's a python+pyqt way to catch serial port value.
  
The picture below is the sensor feedback from arduino by the serial port: 

![img](https://github.com/Ray0124/Serial_port_value_save_GUI/blob/master/serial_port.PNG)    

As for catching the data, my structure is below:  

![img](https://github.com/Ray0124/Serial_port_value_save_GUI/blob/master/structure2.PNG)   

I made a fifo data buffer so that I can observe the data stream on the GUI.
My data buffer(default:100, and you can change by UI) and GUI are below:  

![img](https://github.com/Ray0124/Serial_port_value_save_GUI/blob/master/data%20buffer.PNG)  
  
![img](https://github.com/Ray0124/Serial_port_value_save_GUI/blob/master/GUI.PNG)  


I seperate my GUI into w.ui(design) and logic.py(function),so it's easy to change design.  
Saving datas will name by count,and they located in the current place.  
Running main.py,and programe will start.  
  
![img](https://github.com/Ray0124/Serial_port_value_save_GUI/blob/master/test.gif)  




