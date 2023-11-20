
					SETUP AND COMPILATION 

0. git clone : https://github.com/sugammaheshwari/Flatbuffer-Cross-Platform-Serialisation-Encoder-Decoder-Utility-

1. flatbuffers - subrepository of google flatbuffers library.
	- official doc : https://github.com/google/flatbuffers

2. client.fbs 
	schema for client which contains Msg,Person,Group schema details.

3. fb_encoder.cpp 
	- CPP encoder class
	- Compilation of cpp encoder:
		3.1 cd flatbuffers/
		3.2 cmake -G "Unix Makefiles"
		3.3 make -j 
		3.4 cd ../ && ./flatbuffers/flatc --cpp --python client.fbs
		    3.4.1 Should generate client_generated.h in cpp and Msg.py,Person.py and Group.py in python
		3.5 make
		    3.5.0 default target is compile : g++ -std=c++11 fb_encoder.cpp -I ./flatbuffers/include -o fb_encoder
		    3.5.1 Generates fb_encoder in binary in cpp
		3.6 ./fb_encoder ./
		    3.6.1 Produces fb_bytes.bin file in cwd.
4. fb_decoder.py
	- Python decoder to decode the encoded fb_bytes.bin file by cpp encoder.
	- pip3 install flatbuffers
	- python3 fb_decoder.py ./fb_bytes.bin
		- Produces the decoded output of Person and Group data on the terminal.


					SCHEMAS 

table Msg{
        len:int32;			// to decode the messege according to the messege length
}

table Person{
        id:int16;			// to decode the type of messege 0:Person, 1:Group
        name:string;
        age:short;
        weight:float;
        gender:bool;			// boolean for gender 0:Male 1:Female
}

table Group{
        id:int16;
        name:string;
        avg_age:float;
        avg_weight:float;
        names_cnt:int16;		// To get the count of names in names vector
        names:[string];
}	
