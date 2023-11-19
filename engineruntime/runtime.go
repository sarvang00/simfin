package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

// Message struct for JSON encoding/decoding
type SendMessage struct {
	User   string `json:"user"`
	Day    int    `json:"day"`
	Task   string `json:"task"`
	Amount int    `json:"amount"`
}

type RecdMessage struct {
	User   string `json:"user"`
	Day    int    `json:"day"`
	Status string `json:"task"`
}

func handler(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println(err)
		return
	}
	defer conn.Close()

	for {
		// Read message from browser
		messageType, p, err := conn.ReadMessage()
		if err != nil {
			log.Println(err)
			return
		}

		// Unmarshal JSON
		var receivedMessage RecdMessage
		err = json.Unmarshal(p, &receivedMessage)
		if err != nil {
			log.Println("Error decoding JSON:", err)
			return
		}

		// Print the received message
		fmt.Printf("Received message: %s\n", receivedMessage)

		// Create a response message
		responseMessage := SendMessage{User: "abc@abc.com", Day: 2, Task: "debit", Amount: 200}

		// Marshal response message to JSON
		responseJSON, err := json.Marshal(responseMessage)
		if err != nil {
			log.Println("Error encoding JSON:", err)
			return
		}

		// Write JSON response back to the browser
		err = conn.WriteMessage(messageType, responseJSON)
		if err != nil {
			log.Println(err)
			return
		}
	}
}

func main() {
	serverURL := "ws://localhost:8000/"
	// Establish WebSocket connection
	conn, _, err := websocket.DefaultDialer.Dial(serverURL, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()
	fmt.Println("started")
	// Send a JSON message
	message := map[string]string{"text": "Hello, WebSocket from Go!"}
	err = conn.WriteJSON(message)
	if err != nil {
		log.Fatal(err)
	}

	// Receive and print the response
	var responseMessage map[string]string
	err = conn.ReadJSON(&responseMessage)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Received message: %s\n", responseMessage["text"])
}
