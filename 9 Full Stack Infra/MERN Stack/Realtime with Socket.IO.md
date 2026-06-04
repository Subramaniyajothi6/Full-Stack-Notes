---
tags: [mern, realtime, advanced]
---

# Realtime with Socket.IO

> Adding bidirectional realtime to a MERN app — chat, presence, live dashboards, collaborative editing.

## Architecture
```
React client ──── Socket.IO ──── Express + Socket.IO server
                                       │
                                       └── Redis adapter ── (other server instances)
                                                              │
                                                              └── ...
```

The Redis adapter lets multiple Node instances share rooms + broadcast.

## Server side
```ts
import { Server } from 'socket.io';
import { createAdapter } from '@socket.io/redis-adapter';
import { createClient } from 'redis';

const io = new Server(httpServer, {
  cors: { origin: 'https://app.example.com', credentials: true },
});

// Multi-instance pub/sub via Redis
const pub = createClient({ url: process.env.REDIS_URL });
const sub = pub.duplicate();
await Promise.all([pub.connect(), sub.connect()]);
io.adapter(createAdapter(pub, sub));

// Auth via existing JWT cookie
io.use(async (socket, next) => {
  const token = parseCookie(socket.handshake.headers.cookie || '').at;
  try { socket.data.user = jwt.verify(token, ACCESS_SECRET); next(); }
  catch { next(new Error('unauthorized')); }
});

io.on('connection', (socket) => {
  const userId = socket.data.user.sub;
  socket.join(`user:${userId}`);

  socket.on('chat:join', (roomId) => socket.join(`room:${roomId}`));
  socket.on('chat:message', async (msg, ack) => {
    const saved = await Message.create({ roomId: msg.roomId, userId, body: msg.body });
    io.to(`room:${msg.roomId}`).emit('chat:message', saved);
    ack({ ok: true, id: saved.id });
  });
});
```

## Client side
```tsx
import { io } from 'socket.io-client';

const socket = io('https://api.example.com', { withCredentials: true });

useEffect(() => {
  socket.emit('chat:join', roomId);
  socket.on('chat:message', (msg) => setMessages(m => [...m, msg]));
  return () => { socket.off('chat:message'); };
}, [roomId]);

socket.emit('chat:message', { roomId, body }, (resp) => {
  if (resp.ok) markAsSent(resp.id);
});
```

## Patterns
- **Rooms** — `socket.join('room:abc')` for chat channels, `socket.join('user:123')` for per-user notifications
- **Presence** — store `userId → socketIds` in Redis; emit on (dis)connect
- **Acknowledgements** — third arg to `emit` is a callback the server calls
- **Backpressure** — if a client falls behind, queue messages or drop intelligently
- **Reconnect logic** — built-in; on reconnect, refetch missed events by sequence id

## Real World Usage
- Chat (Slack, Discord-style)
- Live dashboards (stocks, ops monitoring)
- Collaborative editing (Figma-style cursors with [[WebRTC]] for high-frequency)
- Multiplayer games (turn-based)
- Notifications fanout

## Common Mistakes
- No auth on connections → anyone subscribes to anyone's events
- In-memory `userId → socket` map across multiple instances (breaks horizontal scale; use Redis adapter)
- Sending entire chat history on connect (kills first paint)
- Forgetting to `socket.off` on unmount → handlers stack up
- No rate limiting on emit → DoS surface
- Treating Pub/Sub as durable (it's not — use Streams for replay)
- Sticky sessions misconfigured at LB → reconnect storms

## Prerequisites
- [[WebSockets]] · [[Redis]] · [[Full-Stack Auth Flow]]

## What To Learn Next
- [[Background Jobs]] · [[WebRTC]]

## Best Learning Resources

### Official Documentation
- [Socket.IO docs](https://socket.io/docs/v4/)
- [Redis adapter](https://socket.io/docs/v4/redis-adapter/)
- [ws (lower-level alternative)](https://github.com/websockets/ws)

### Best YouTube Resource
- [Hussein Nasser — WebSocket internals](https://www.youtube.com/@hnasr)
- [Web Dev Simplified — Socket.IO chat](https://www.youtube.com/c/WebDevSimplified)

### Best Free Course
- [Socket.IO chat tutorial (official)](https://socket.io/get-started/chat)
- [LiveKit / mediasoup tutorials (for SFU patterns)](https://livekit.io/)

### Best Advanced Resource
- [Designing Distributed Pub/Sub — Confluent blog](https://www.confluent.io/blog/) — for when you outgrow Pub/Sub
- [PartyKit](https://www.partykit.io/) — Cloudflare Durable Objects for realtime

### Best Practice Project
Build a chat app with rooms, presence, typing indicators, read receipts, and message history pagination. Run two backend instances behind nginx; verify Redis adapter syncs broadcasts. Add rate limiting per socket.

### Recommended Order to Learn
1. Plain WebSocket via `ws`
2. Socket.IO basics (rooms, ack)
3. Auth on the handshake
4. Redis adapter for multi-instance
5. Presence + typing indicators
6. Message persistence + history
7. Production: sticky LB, monitoring, scaling

## Interview Questions
**Q. WebSockets vs Server-Sent Events?**
A. WebSockets are bidirectional. SSE is server-only. Use SSE for notifications, WS for chat.

**Q. Why Redis adapter for Socket.IO?**
A. With multiple Node instances, sockets connected to instance A can't broadcast to sockets on instance B without a shared bus. Redis Pub/Sub bridges them.

**Q. What's a sticky session?**
A. Load balancer routes a client's HTTP requests to the same backend instance, needed for non-Redis-adapter Socket.IO and for hot caches.

## Related
- [[WebSockets]] · [[Server-Sent Events]] · [[Redis]] · [[Background Jobs]] · [[WebRTC]]
