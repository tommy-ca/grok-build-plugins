#!/bin/sh
# Run from a host shell or `grok --sandbox off` / `grok --sandbox herdr-install`.
# Nested grok under homelab bind-mounts ~/.grok/hooks read-only (EROFS).
set -eu
if [ "${__GROK_INSIDE_BWRAP:-}" = 1 ]; then
  echo "herdr grok hooks: this process is inside agent bwrap. hooks/ is read-only." >&2
  echo "Use a host shell, grok --sandbox off, grok --sandbox devbox, or grok --sandbox herdr-install." >&2
  exit 1
fi
command -v herdr >/dev/null 2>&1 || {
  echo "herdr not on PATH" >&2
  exit 1
}
herdr integration install grok
echo "herdr grok hooks: $(ls -1 "${HOME}/.grok/hooks/herdr.json" "${HOME}/.grok/hooks/herdr-agent-state.sh")"
