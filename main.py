document.querySelector("body > div.homework-result-page > div:nth-child(1) > div > div > div > div:nth-child(2) > div.col-md-3.col-sm-4.col-xs-5 > div > span").textContent = "12 / 12";
document.querySelector("body > div.homework-result-page > div:nth-child(1) > div > div > div > div:nth-child(3) > div:nth-child(4) > div > span").textContent = "100";

const spanElement = document.querySelector("body > div.homework-result-page > div:nth-child(1) > div > div > div > div:nth-child(3) > div:nth-child(2) > div > span");

let currentText = spanElement.textContent.trim();

const [currentScore, maxScore] = currentText.split('/').map(num => num.trim());

spanElement.textContent = `${maxScore} / ${maxScore}`;

document.querySelector("body > div.homework-result-page > div:nth-child(1) > div > div > div > div:nth-child(4) > div.col-md-9.col-sm-9 > div > div.progress-bar").textContent = "100%";
const progressBar = document.querySelector('.progress-bar');
progressBar.style.width = '100%';
document.querySelector("body > div.homework-result-page > div:nth-child(1) > div > div > div > div:nth-child(5) > div.col-md-4.col-sm-4.hidden-xs > div > span").textContent = "0";
document.querySelector("body > div.homework-result-page > div:nth-child(1) > div > div > div > div:nth-child(5) > div:nth-child(2) > div > span").textContent = "0";

let numberOfQuestionsElement = document.querySelector('.homework-personal-stat-number');
let numberOfQuestions = numberOfQuestionsElement.textContent.split('запитань')[0].split(' ').join('');

document.querySelector("body > div.homework-result-page > div:nth-child(1) > div > div > div > div:nth-child(5) > div:nth-child(1) > div > span").textContent = numberOfQuestions;

let timeElement = document.querySelector("body > div.homework-result-page > div:nth-child(1) > div > div > div > div:nth-child(6) > div:nth-child(2) > div > span");
let cleanNumber = timeElement.textContent.replace(' сек', '').replace(' ', '');
let randomTime = (Math.random() * (12.9 - 11.1) + 11.1).toFixed(1);
timeElement.textContent = randomTime + ' сек';

let totalTimeElement = document.querySelector("body > div.homework-result-page > div:nth-child(1) > div > div > div > div:nth-child(6) > div:nth-child(1) > div > span");
let totalTime = Math.round(randomTime * numberOfQuestions);
totalTimeElement.textContent = totalTime + ' сек';
