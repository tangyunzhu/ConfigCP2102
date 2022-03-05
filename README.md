#URL for configure chip   
https://community.silabs.com/s/article/how-to-control-gpios-of-cp210x-at-runtime?language=en_US   

#Set GPIO output value configure   
https://www.silabs.com/documents/public/application-notes/AN571.pdf   #Page18   

#have creat 3 config file for the following status   
IO0  |  IO1   | IO2   | IO3    | config_file_name
------------------------------------------------------------------
TXLED	  RXLED	  GPIO	  GPIO		cp2102n_a02_gqfn24.configuration   
GPIO	  RX LED	GPIO	  GPIO		cp2102n_a02_gqfn24_mt7628.configuration   
GPIO	  GPIO	  GPIO	  GPIO		cp2102n_a02_gqfn24_1.configuration   	
