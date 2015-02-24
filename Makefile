.DEFAULT_GOAL =	all

.PHONY =	all clean wget gen gen-twisted copy copy-twisted

LOC	=	https://raw.githubusercontent.com/iPlantCollaborativeOpenSource/skywalker.thrift/master/skywalker.thrift
IDL_FILE =	./skywalker.thrift
WGET	=	wget
THRIFT	=	thrift
COPY	=	cp
CHOWN	=	chown
USER	=	root
GROUP	=	root

all : wget gen copy

clean :
	rm -rf ./build
	rm -rf ./gen-py.twisted
	rm -rf ./skywalker
	rm -f ./skywalker.thrift

wget :
	$(WGET) -O $(IDL_FILE) $(LOC)

gen : gen-twisted

gen-twisted :
	$(THRIFT) --gen py:twisted ./skywalker.thrift

copy : copy-twisted

copy-twisted :
	$(COPY) -r gen-py.twisted/skywalker ./skywalker

chown :
	$(CHOWN) -R $(USER):$(GROUP) .
