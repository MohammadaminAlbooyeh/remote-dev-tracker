export function formatCET(date) {
  const d = new Date(date);
  return d.toLocaleString("en-GB", { timeZone: "Europe/Rome" });
}

export function nowCET() {
  return new Date(
    new Date().toLocaleString("en-US", { timeZone: "Europe/Rome" })
  );
}
