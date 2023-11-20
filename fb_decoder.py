import flatbuffers
import sys
from Person import Person
from Group import Group
from Msg import Msg

if len(sys.argv)<2:
	print("please enter the path to read the binary dump file")
	exit(1)

file_path = sys.argv[1]

buf = open(file_path, 'rb').read()
buf = bytearray(buf)

ptr = 0

while ptr < len(buf):
	
	msg = Msg.GetRootAsMsg(buf,ptr);
	person = Person.GetRootAsPerson(buf,ptr+20);

	if person.Id()==0:
		print("msg_id:0")
		print(person.Name())
		print(person.Age())
		print(person.Weight())
		print(person.Gender())
	else:
		print("msg_id:1")
		group = Group.GetRootAsGroup(buf,ptr+20);
		print(group.Name())
		print(group.AvgAge())
		print(group.AvgWeight())
		siz = group.NamesCnt()
		for i in range(siz):
			print(group.Names(i),end =" ")

	ptr = ptr + 20 + msg.Len()
