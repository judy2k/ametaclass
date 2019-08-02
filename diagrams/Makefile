FILES := $(subst .dot,.png, $(shell ls *.dot))

all: $(FILES)

%.png: %.dot
	dot -Gsize=16,9\! -Gdpi=100 -Tpng -o "$@" $<

clean:
	rm -f *.png

.PHONY: clean all