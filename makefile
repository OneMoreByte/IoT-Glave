
BINARY = iotgl

BUILDDIR = build
SOURCEDIR = src
HEADERDIR = include

CXX = g++

CXXFLAGS = -Wall -g -std=c++17

SOURCES := $(shell find $(SOURCEDIR) -name '*.cpp')

OBJECTS := $(addprefix $(BUILDDIR)/,$(SOURCES:%.cpp=%.o))

all: $(BINARY)


$(BINARY): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(BINARY)

$(BUILDDIR)/%.o: %.cpp
	$(CXX) $(CXXFLAGS) -I$(HEADERDIR) -I$(dir $<) -c $< -o $@
