#include "client_generated.h"
#include <iostream>
#include <fstream>

void save_builder_state_to_file(flatbuffers::FlatBufferBuilder& builder, std::ofstream& ofile)
{
   uint8_t *buf = builder.GetBufferPointer();
   int32_t size = builder.GetSize();
  
   flatbuffers::FlatBufferBuilder t_builder;
   auto msg_len = CreateMsg(t_builder,size);
   t_builder.Finish(msg_len);
   ofile.write((char *)(t_builder.GetBufferPointer()),t_builder.GetSize());
   
   ofile.write((char *)(buf), size);
}

int main(int argc, const char * argv[]) {

  if(argc<2){
	std::cout<<"Please enter the path to dump binary file!!"<<std::endl;
	return 0;
  }
 
  flatbuffers::FlatBufferBuilder builder;
  auto msg_id = 0;
  auto p1 = builder.CreateString("person 1");
  auto a1 = 25;
  auto w1 = 90;
  auto gen = 0;						// M:0 F:1
  auto person1 = CreatePerson(builder,msg_id,p1,a1,w1,gen);
  builder.Finish(person1);

  flatbuffers::FlatBufferBuilder builder2;
  auto msg2_id = 1;
  auto g1 = builder2.CreateString("group 1");
  auto aa1 = 30.25;
  auto aw1 = 80.568; 
  auto nc = 3;
  std::vector<flatbuffers::Offset<::flatbuffers::String>> name = {builder2.CreateString("sugam"),builder2.CreateString("payas"),builder2.CreateString("ankit")};
  auto name_vec = builder2.CreateVector(name);
  auto group1 = CreateGroup(builder2,msg2_id,g1,aa1,aw1,nc,name_vec);
  builder2.Finish(group1);

  std::string dumpPath = argv[1];
  dumpPath += "fb_bytes.bin";
  std::ofstream ofile(dumpPath.c_str(), std::ios::binary);
  save_builder_state_to_file(builder,ofile);
  save_builder_state_to_file(builder2,ofile);  
  ofile.close();

  printf("The FlatBuffer was successfully created and objects were written to fb_bytes.bin file!!! \n");
}
