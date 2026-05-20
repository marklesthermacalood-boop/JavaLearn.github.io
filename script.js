function scrollToLessons() {
  document.getElementById("lessons").scrollIntoView({
    behavior: "smooth"
  });
}

// Add click interaction to lessons
document.querySelectorAll(".card").forEach((card, index) => {
  card.addEventListener("click", () => {
    alert("Opening Lesson " + (index + 1));
  });
});


