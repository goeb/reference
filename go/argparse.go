
// This program demonstrates how to parse command line arguments
// Example:
// go run argparse.go --verbose -path x/y/z aa bb cc -level 3
// level= 1234
// path= x/y/z
// verbose= true
// Positional argument[0]=aa
// Positional argument[1]=bb
// Positional argument[2]=cc
// Positional argument[3]=-level
// Positional argument[4]=3

package main

import (
    "flag"
    "fmt"
    "os"
)

var(
    level int
    path string
    verbose bool
)

func main() {
    flag.IntVar(&level, "level", 1234, "int help message")
    flag.StringVar(&path, "path", "default" , "str help message")
    flag.BoolVar(&verbose, "verbose", false, "bool help message")
    flag.Usage = func() {
        fmt.Fprintln(os.Stderr, "Usage:")
        flag.PrintDefaults()
        fmt.Fprintln(os.Stderr, "More details an examples ...")
    }

    flag.Parse()

    fmt.Println("level=", level)
    fmt.Println("path=", path)
    fmt.Println("verbose=", verbose)
    var other_args = flag.Args()
    for index, value := range other_args {
        fmt.Printf("Positional argument[%d]=%s\n", index, value)
    }
}

