package main

import (
  "net/http"
	"fmt"
	"os"
)

func main() {
	http.HandleFunc("/api", func(w http.ResponseWriter, r *http.Request) {
        message := "World!"
  		w.Write([]byte(message))
	})	
	
	fmt.Println("Started at: " + os.Getenv("WORLD_PORT"))
	
	if err := http.ListenAndServe(":" + os.Getenv("WORLD_PORT"), nil); err != nil {
	  panic(err)
    }
}