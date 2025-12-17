const container = document.querySelector(".hearts-container");

function createHeart() {
    const heart = document.createElement("div");
    heart.classList.add("heart");
    heart.innerHTML = "💗";

    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = 8 + Math.random() * 5 + "s";
    heart.style.fontSize = 14 + Math.random() * 20 + "px";

    // POP ON CLICK
    heart.addEventListener("click", () => {
        heart.classList.add("pop");
        setTimeout(() => heart.remove(), 400);
    });

    container.appendChild(heart);

    // auto remove if not clicked
    setTimeout(() => {
        if (heart.parentElement) heart.remove();
    }, 8000);
}

setInterval(createHeart, 400);
// ================= Cursor Heart =================
document.addEventListener("mousemove", (e) => {
    const heart = document.createElement("div");
    heart.classList.add("heart");
    heart.innerHTML = "💖";

    heart.style.left = e.pageX + "px";
    heart.style.top = e.pageY + "px";

    // softer color & smaller size
    heart.style.color = "rgba(255, 182, 193, 0.7)"; // light pink
    heart.style.fontSize = 12 + Math.random() * 15 + "px";

    // slower animation
    heart.style.animation = "cursorFloat 2s forwards";

    container.appendChild(heart);

    setTimeout(() => heart.remove(), 2000);
});

async function predictCrush() {
  const data = {
    texts_first: Number(document.getElementById("texts_first").value),
    reply_speed: Number(document.getElementById("reply_speed").value),
    emoji_usage: Number(document.getElementById("emoji_usage").value),
    eye_contact: Number(document.getElementById("eye_contact").value),
    shares_personal: Number(document.getElementById("shares_personal").value)
  };

  const response = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  document.getElementById("result").innerText = result.message;
  showAnimatedResult(result.message);

}
// ================= Animated Result =================
async function showAnimatedResult(message) {
  const box = document.getElementById("resultBox");
  const heart = document.getElementById("heartIcon");
  const percentText = document.getElementById("percentText");

  box.classList.remove("hidden");

  const percent = parseFloat(message.match(/\d+(\.\d+)?/)[0]);
  percentText.innerText = percent + "%";

  if (percent > 70) {
    heart.innerText = "💖";
    heart.className = "love";
    launchConfetti();
  } else if (percent > 40) {
    heart.innerText = "💗";
    heart.className = "maybe";
  } else {
    heart.innerText = "💔";
    heart.className = "nope";
  }
}
// ================= Confetti Effect (ADD ONLY) =================
function launchConfetti() {
  const colors = ["#ff4d88", "#ff99cc", "#ffccdd", "#ff6699"];

  for (let i = 0; i < 120; i++) {
    const confetti = document.createElement("div");
    confetti.classList.add("confetti");

    confetti.style.left = Math.random() * 100 + "vw";
    confetti.style.backgroundColor =
      colors[Math.floor(Math.random() * colors.length)];
    confetti.style.animationDuration = 2 + Math.random() * 3 + "s";

    document.body.appendChild(confetti);

    setTimeout(() => confetti.remove(), 5000);
  }
}

