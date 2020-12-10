.POSIX:

all: clean ll

ll: ll.o
	${CXX} -o ll ll.o

ll.o:
	${CXX} -c ll.cpp

clean:
	rm -f ll.o ll
