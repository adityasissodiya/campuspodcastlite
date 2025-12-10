document.addEventListener("DOMContentLoaded", () => {
  const player = document.getElementById("audio-player");
  if (!player) return;

  player.addEventListener("loadedmetadata", () => {
    const duration = Math.round(player.duration || 0);
    console.log(`Loaded audio (${duration}s)`);
  });
});
