# Machine Monitoring System

A real-time machine monitoring system built using the Observer design pattern. This project demonstrates how to track machine states and notify observers (employees, dashboards) when machines change state.

## Features

- **Observer Pattern Implementation**: Clean implementation of the Observer design pattern in Python
- **Real-time Updates**: WebSocket-based communication for instant state updates
- **Web Dashboard**: Beautiful HTML dashboard displaying machine states in real-time
- **Multiple Observer Types**:
  - `Employee`: Receives console notifications about machine state changes
  - `Dashboard`: Sends state updates to web clients via WebSocket
- **Flexible Architecture**: Easy to extend with new observer types or machine types

## Project Structure

```
Machineobserver/
├── observer.py           # Core Observer pattern implementation with Machine and Observer classes
├── websocket_server.py   # WebSocket server for broadcasting machine state updates
├── dashboard.html        # Web-based dashboard for visualizing machine states
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge, Safari)

### Setup

1. **Clone or download the project**

2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The system consists of three components that work together:

### 1. Start the WebSocket Server

In a terminal, run:
```bash
python websocket_server.py
```

This starts a WebSocket server on `ws://localhost:8765` that broadcasts machine state updates to all connected clients.

**Output:**
```
Starting WebSocket server on ws://localhost:8765
```

### 2. Open the Web Dashboard

Open `dashboard.html` in your web browser. The dashboard will:
- Automatically connect to the WebSocket server
- Display all machines and their current states
- Update in real-time when machines change state
- Show connection status and last update times

### 3. Run the Observer Script

In another terminal, run:
```bash
python observer.py
```

This creates machines, attaches observers, and sends state updates. You'll see:
- Console output from Employee observers
- Dashboard updates sent via WebSocket
- Real-time updates in the web dashboard

## Code Examples

### Creating a Machine and Observer

```python
# Create a machine
machine = Machine("CNC Machine")

# Create an employee observer
employee = Employee("Alice", "Operator")

# Attach the observer to the machine
machine.attach(employee)

# Update machine state (notifies all observers)
machine.setState("Running")
machine.notifyallobservers()
```

### Using the Dashboard Observer

```python
# Create a dashboard observer that sends updates via WebSocket
dashboard = Dashboard("Main Dashboard", "ws://localhost:8765")

# Attach to a machine
machine = Machine("3D Printer")
machine.attach(dashboard)

# State changes will be sent to the web dashboard
machine.setState("Operational")
machine.notifyallobservers()
```

### Extending with Custom Observers

```python


## Architecture

### Observer Pattern

The project implements the classic Observer pattern:

- **Subject (Machine)**: Maintains a list of observers and notifies them of state changes
- **Observer**: Abstract interface for all observers with an `update()` method
- **Concrete Observers**:
  - `Employee`: Logs state changes to console
  - `Dashboard`: Sends state changes to WebSocket server

### Component Communication

```
Machine (Subject)
    ↓
    ├─→ Employee (Observer) → Console Output
    └─→ Dashboard (Observer) → WebSocket Server → Web Browser
```

## Features in Detail

### Employee Observer
- Receives real-time notifications about machine state changes
- Displays employee name, role, machine name, and new state
- Perfect for console-based monitoring

### Dashboard Observer
- Sends JSON-formatted updates to WebSocket server
- Includes error handling for connection failures
- Supports multiple dashboard instances

### Web Dashboard
- Clean, responsive UI
- Color-coded state indicators (Running, Stopped, Idle, etc.)
- Auto-reconnection on disconnect
- Last update timestamps
- Connection status indicator

## Troubleshooting

### WebSocket Connection Errors

If you see `Dashboard: Failed to send update - Connection refused`:
- Ensure the WebSocket server is running (`python websocket_server.py`)
- Check that the port 8765 is not blocked by firewall
- Verify the WebSocket URL matches: `ws://localhost:8765`

### Dashboard Not Updating

- Check browser console for errors (F12 → Console)
- Ensure the WebSocket server is running
- Verify the HTML file is using the correct WebSocket URL
- Try refreshing the browser page

### Port Already in Use

If port 8765 is already in use, you can change it in:
1. `websocket_server.py`: Change the `port` variable
2. `observer.py`: Update the WebSocket URL in Dashboard initialization
3. `dashboard.html`: Update the `wsUrl` variable


## Dependencies

- `websockets==15.0.1`: WebSocket client and server implementation


