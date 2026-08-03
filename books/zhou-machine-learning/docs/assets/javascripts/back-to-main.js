(() => {
  const addBackButton = () => {
    const content = document.querySelector(".md-content__inner");
    if (!content || content.querySelector(".back-to-main")) return;
    const link = document.createElement("a");
    link.className = "back-to-main";
    link.href = "/";
    link.target = "_top";
    link.setAttribute("aria-label", "回到主站首页");
    link.textContent = "← 回到主站";
    content.prepend(link);
  };
  if (typeof document$ !== "undefined") document$.subscribe(addBackButton);
  else document.addEventListener("DOMContentLoaded", addBackButton);
})();
