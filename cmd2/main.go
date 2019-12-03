package main

import (
	"errors"

	"gitlab.com/fliperdev/gocron"
)

func main() {
	gocron.Every(1).Minute().Do(execTeste)
	<-gocron.Start()
}
func execTeste() {
	errors.New("DLKASDKAL")
}
