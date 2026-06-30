// run test-command-context.go
// line:line 1
// line:line 2
// signal: killed
// failed
// completed

package main

import (
	"bufio"
	"context"
	"fmt"
	"io"
	"os"
	"os/exec"
	"time"
)

func startProgram(ctx context.Context, command string, args ...string) (<-chan string, error) {

	// Prepare the external command
	cmd := exec.CommandContext(ctx, command, args...)

	// Grab pipes for stdout and stderr before starting the command
	stdoutPipe, err := cmd.StdoutPipe()
	if err != nil {
		return nil, err
	}

	stderrPipe, err := cmd.StderrPipe()
	if err != nil {
		return nil, err
	}

	// Start the process (non-blocking)
	err = cmd.Start()
	if err != nil {
		return nil, err
	}

	outChan := make(chan string)
	go func() {
		// Ensure the channel is closed when the goroutine exits
		defer close(outChan)

		outputDone := make(chan struct{}, 2)

		// Helper function to scan a pipe line by line
		streamLogs := func(pipe io.ReadCloser) {
			scanner := bufio.NewScanner(pipe)
			for scanner.Scan() {
				outChan <- "line:" + scanner.Text()
			}
			// TODO check scanner.Err()
			outputDone <- struct{}{}
		}

		// Read stdout and stderr concurrently
		go streamLogs(stdoutPipe)
		go streamLogs(stderrPipe)

		// Wait for both readers to finish digesting the streams
		<-outputDone
		<-outputDone

		// Wait for the command to clean up and grab the exit status
		err := cmd.Wait()
		if err != nil {
			outChan <- err.Error()
			outChan <- "failed"
		} else {
			outChan <- "ok"
		}
	}()

	return outChan, nil
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)

	script := `
		echo "line 1"
		echo "line 2"
		exec sleep 1234
	`

	events, err := startProgram(ctx, "sh", "-c", script)
	if err != nil {
		fmt.Fprintf(os.Stderr, err.Error())
		os.Exit(1)
	}

	for event := range events {
		fmt.Println(event)
		switch event {
		case "ok":
			break
		case "failed":
			break
		}
	}
	cancel()
	fmt.Println("completed")
}
