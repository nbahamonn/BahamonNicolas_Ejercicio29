evolve_A.png. : D.py Datos.dat 
	python D.py
    
Datos.dat : D.x
	./D.x

D.x : D.cpp
	c++ D.cpp -o D.x
    