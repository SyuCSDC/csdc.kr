fetch('/static/js/tags.json')
.then(response => response.json()) // 응답을 JSON으로 변환
.then(data => {
  
  const descriptionDivs = document.querySelectorAll('.tags-description');

  // 선택된 모든 요소에 대해 반복 실행
  descriptionDivs.forEach((div) => {
    
    const randomIndex = Math.floor(Math.random() * data.length);
    const selectedItem = data[randomIndex];

    const displayText = `&lt;${selectedItem.tag}&gt; 태그는 ${selectedItem.description}`;

    div.innerHTML = displayText;
  });
})
.catch(error => console.error('데이터 로드 중 오류 발생:', error));
