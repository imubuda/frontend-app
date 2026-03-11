
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}


type WebResponse struct {
    Success bool        `json:"success"`
    Data    interface{} `json:"data,omitempty"`
    Error   string      `json:"error,omitempty"`
}

