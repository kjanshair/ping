package main

import (
  "net/http"
  "fmt"
)

func main() {
	http.HandleFunc("/api", func(w http.ResponseWriter, r *http.Request) {
        message := "World!"
  		w.Write([]byte(message))
	})	
	
	fmt.Println("Started at: 8080")
	
	if err := http.ListenAndServe(":8080", nil); err != nil {
	  panic(err)
    }
}