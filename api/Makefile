.EXPORT_ALL_VARIABLES:
GO111MODULE := on

# go config
ifndef $(GOPATH)
  GOPATH=$(shell go env GOPATH)
endif
GOBIN = $(GOPATH)/bin

INCLUDE_FLAGS = -I. -I$(GOPATH)/pkg/mod/github.com/googleapis/api-common-protos@v0.1.0 -I/usr/local/include -I$(GOPATH)/pkg/mod/github.com/grpc-ecosystem/grpc-gateway@v1.12.2/third_party/googleapis -I$(GOPATH)/src
PROTO = proto/hello.proto

all:
	make godeps
	make gate-way
	make reverse-proxy
	make swagger-UI
	make goserver


pyserver: ## create gPRC python server
	python -m grpc_tools.protoc $(INCLUDE_FLAGS) --python_out=. --grpc_python_out=. $(PROTO)


godeps: ## Install the Go dependencies
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
	go get -u github.com/golang/protobuf/protoc-gen-go


gate-way: ## generate gPRC gateway
	protoc -I/usr/local/include -I. \
  	-I$(GOPATH)/src \
  	-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
  	--go_out=plugins=grpc:. \
  	$(PROTO)
	mv proto/hello.pb.go http/proto/hello.pb.go


reverse-proxy: ## generate gPRC reverse proxy
	protoc -I/usr/local/include -I. \
	  -I$(GOPATH)/src \
	  -I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
	  --plugin=protoc-gen-grpc-gateway=$(GOPATH)/bin/protoc-gen-grpc-gateway \
	  --grpc-gateway_out=logtostderr=true:. \
	  $(PROTO)
	mv proto/hello.pb.gw.go http/proto/hello.pb.gw.go


swagger-UI: ## generate swagger UI
	protoc -I/usr/local/include -I. \
	  -I$(GOPATH)/src \
	  -I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
	  --plugin=protoc-gen-swagger=$(GOPATH)/bin/protoc-gen-swagger \
	  --swagger_out=logtostderr=true:. \
	  $(PROTO)
	mv proto/hello.swagger.json www/swagger.json


kill-pyserve: ## Stop the Python server
	lsof -ti TCP:9090 | xargs -n1 kill -9

kill-goserve: ## Stop the Python server
	lsof -ti TCP:8080 | xargs -n1 kill -9


pyserver: kill-pyserve ## start gPRC server
	PYTHONPATH=. python server.py


goserver:kill-goserve ## start HTTP server
	go run http/http_server.go --grpc-server-endpoint localhost:9090

