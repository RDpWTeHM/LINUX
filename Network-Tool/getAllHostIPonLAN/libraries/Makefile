###
### Makefile
###

###
### software be used.
###
MAKE = make

## run all need check ./bin/nmap exist???
### check "$ make" permission!!!!
all:
## get nmap tar path (full name)

## Extra nmap.
	tar -jxvf nmap-7.70.tar.bz2


## run configuration
	cd nmap-7.70 &&	./configure

## run Make
	$(MAKE) --directory=nmap-7.70

	cp ./nmap-7.70/nmap ./bin/

## -[o] joseph, update cp ./nmap-7.70/nmap ./bin/
## if cp OK do below:
	rm -fr ./nmap-7.70

### INSTALL ## if permission OK
#	cp ./bin/nmap /usr/local/bin/nmap



.PHONY: all clean

clean:
	rm -fr ./bin/nmap ./nmap-7.70



