package main

import (
	"fmt"
	"github.com/jessevdk/go-flags"
)

type CmdActivate struct {
	Verbose bool `short:"v" long:"verbose" description:"Be verbose"`
}
type CmdDeactivate struct {
	Verbose bool `short:"v" long:"verbose" description:"Be verbose"`
}

var (
	cmdActivate CmdActivate
	cmdDeactivate CmdDeactivate
)

func (cmd *CmdActivate) Execute(args []string) error {
	fmt.Printf("Activate: v=%v\n", cmd.Verbose)
	return nil
}

func (cmd *CmdDeactivate) Execute(args []string) error {
	fmt.Printf("Deactivate: v=%v\n", cmd.Verbose)
	return nil
}

type Options struct {
	Name string `short:"n" long:"name" description:"Give a name"`
}

var options Options

func main() {
	var parser = flags.NewParser(&options, flags.Default)
	parser.AddCommand("activate", "Activate this", 
		"Long description of 'activate'",
		&cmdActivate)
	parser.AddCommand("deactivate", "Deactivate this", 
		"Long description of 'deactivate'",
		&cmdDeactivate)
	parser.Parse()
}
