#include <cstdio>
#define SIZE_MEM 3
#ifndef BUFFER_H
#define BUFFER_H

class CBuffer{
	private:
		char* buffer;
	public:
		CBuffer();
		~CBuffer();
		char& operator[](int idx);
};

#endif
