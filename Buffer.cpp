#include "Buffer.h"

CBuffer::CBuffer():buffer(new char[SIZE_MEM]){}
CBuffer::~CBuffer(){
	delete[] buffer;
}
char& CBuffer::operator[](int idx){
	return buffer[idx];
}
