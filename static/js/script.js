// script.js
const card = document.querySelector('.img-fluid');
card.addEventListener('mouseover', function () {
card.style.transform = 'scale(1.2)';
});

card.addEventListener('mouseout', function () {
card.style.transform = 'scale(1)';
});
console.log("Hello")
