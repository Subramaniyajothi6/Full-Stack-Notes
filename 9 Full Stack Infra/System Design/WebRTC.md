---
tags: [infra, backend, advanced]
---

# WebRTC

> Real-time peer-to-peer audio, video, and data channels in the browser.

## Why it matters
Powers Google Meet, Discord voice, FaceTime web, multiplayer games. Lets browsers stream media and arbitrary data to each other with low latency.

## Core ideas
- **Signaling** — out-of-band channel (WebSocket usually) to exchange offer/answer + ICE candidates
- **STUN** — discover public IP for NAT traversal
- **TURN** — relay when direct P2P is impossible (~10–20% of users behind strict NATs)
- **SDP** — text format describing media capabilities
- **MediaStream / RTCPeerConnection / RTCDataChannel** — three core APIs
- **SFU** — Selective Forwarding Unit; for >2 participants, relay through a server

## Flow (simplified)
```
A creates offer → signaling → B
B creates answer → signaling → A
Both gather ICE candidates → exchanged → P2P connection
```

## Real World Usage
- Video calling apps
- Real-time collaboration (cursors, drawing) over `RTCDataChannel`
- Cloud gaming (browser → server)
- Live streaming with low-latency (LL-HLS alternative)

## Common Mistakes
- Building 1:1 mental model and trying to scale → must move to SFU
- Skipping TURN — works in dev, fails in corp networks
- Not handling ICE failures + reconnect
- Putting business data in unencrypted-by-default DataChannels (WebRTC encrypts but verify config)

## Prerequisites
- [[WebSockets|WebSockets]] · [[Client-Server Model|Client/Server]]

## What To Learn Next
- [[Server-Sent Events|SSE]] · [[Edge Computing]]

## Best Learning Resources

### Official Documentation
- [WebRTC.org](https://webrtc.org/) — concepts + samples
- [MDN — WebRTC API](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API) — API reference

### Best YouTube Resource
- [Hussein Nasser — WebRTC explained](https://www.youtube.com/@hnasr) — protocol-level depth
- [Fireship — WebRTC in 100 seconds](https://www.youtube.com/c/Fireship) — quick mental model

### Best Free Course
- [WebRTC Codelab — Google](https://webrtc.org/getting-started/overview)
- [getstream.io blog — WebRTC tutorials](https://getstream.io/resources/projects/webrtc/) — practical

### Best Advanced Resource
- [High Performance Browser Networking — WebRTC chapter](https://hpbn.co/webrtc/) — Ilya Grigorik
- [WebRTC for the Curious](https://webrtcforthecurious.com/) — free book on internals

### Best Practice Project
Build a 2-person video call with vanilla WebRTC + a tiny Node WebSocket signaling server. Then add a 3rd participant by integrating mediasoup or LiveKit (open-source SFU).

### Recommended Order to Learn
1. ICE/STUN/TURN concepts
2. Signaling flow
3. `RTCPeerConnection` basics + offer/answer
4. MediaStream API + getUserMedia
5. DataChannel
6. SFU architecture for many participants

## Interview Questions
**Q. Why do you need a signaling server if WebRTC is P2P?**
A. To exchange the initial offer/answer and ICE candidates. Once connected, media is P2P.

**Q. STUN vs TURN?**
A. STUN finds public IP through NAT. TURN relays media when symmetric NAT prevents direct connection.

**Q. Why move from mesh to SFU at >3 participants?**
A. Mesh sends each peer's stream to every other peer (N²); SFU routes through one server (N).

**Q. Is WebRTC encrypted?**
A. Yes — DTLS for keys, SRTP for media. Mandatory.

## Related
- [[WebSockets|WebSockets]] · [[Server-Sent Events|SSE]]
