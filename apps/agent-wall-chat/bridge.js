// Real-session bridge abstraction.
// Current implementation is intentionally safe: it records intended OpenClaw
// session bindings and falls back to local orchestration when direct tool
// routing is unavailable from this web process.

class SessionBridge {
  constructor() {
    this.mode = process.env.AGENT_WALL_BRIDGE_MODE || 'local-fallback';
    this.bindings = new Map();
    this.events = [];
  }

  bindAgent(agentId, meta = {}) {
    const binding = {
      agentId,
      mode: this.mode,
      status: 'bound-local-fallback',
      sessionKey: meta.sessionKey || null,
      label: meta.label || null,
      reason: 'Direct OpenClaw tool bridge is not available inside this Node web process yet.',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };
    this.bindings.set(agentId, binding);
    this.events.push({ ts: binding.createdAt, type: 'bind', agentId, binding });
    return binding;
  }

  getBinding(agentId) {
    return this.bindings.get(agentId) || this.bindAgent(agentId);
  }

  listBindings() {
    return Array.from(this.bindings.values());
  }

  async send(agentId, message) {
    const binding = this.getBinding(agentId);
    const event = {
      ts: new Date().toISOString(),
      type: 'send',
      agentId,
      mode: binding.mode,
      status: 'fallback-local',
      message,
      reason: binding.reason
    };
    this.events.push(event);
    return event;
  }

  getStatus() {
    return {
      mode: this.mode,
      ready: true,
      realSessionEnabled: false,
      reason: 'Web app lacks direct access to OpenClaw tool/session RPC; using bridge abstraction + local fallback.',
      bindings: this.listBindings(),
      events: this.events.slice(-50)
    };
  }
}

module.exports = { SessionBridge };
