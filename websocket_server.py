import asyncio
import websockets

# Store connected clients
connected_clients = set()

async def handler(websocket):
    # Register the client
    connected_clients.add(websocket)
    print(f"Client connected. Total clients: {len(connected_clients)}")
    
    try:
        async for message in websocket:
            print(f"Received: {message}")
            
            # Broadcast to all connected clients (including web dashboards)
            disconnected_clients = set()
            for client in connected_clients:
                try:
                    await client.send(message)
                except Exception as e:
                    print(f"Error sending to client: {e}")
                    disconnected_clients.add(client)
            
            # Remove disconnected clients
            connected_clients.difference_update(disconnected_clients)
            
    except websockets.exceptions.ConnectionClosed:
        print("Client connection closed")
    finally:
        # Unregister the client
        connected_clients.discard(websocket)
        print(f"Client disconnected. Total clients: {len(connected_clients)}")


async def main():
    port = 8765
    print(f"Starting WebSocket server on ws://localhost:{port}")
    async with websockets.serve(handler, "localhost", port):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
