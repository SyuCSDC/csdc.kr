document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('networkCanvas');
    const ctx = canvas.getContext('2d');

    // 캔버스 크기 설정
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    
    // 노드(점)을 저장할 배열
    let nodes = [];

    // 노드 생성 함수
    function createNodes(count) {
        for (let i = 0; i < count; i++) {
            let node = {
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                radius: Math.random() * 3 + 1, // 1 ~ 4 사이의 크기
                vx: Math.random() *  1 - 0.5 , // x축 속도 (-1 ~ 1)
                vy: Math.random() * 0.6 - 0.3 , // y축 속도 (-1 ~ 1)
                color: `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`, // RGB 색상 값
            };
            nodes.push(node);
        }
    }

    function updateNodePositions() {
        nodes.forEach(node => {
            node.x += node.vx;
            node.y += node.vy;
    
            // 화면 경계에서 반사
            if (node.x <= 0 || node.x >= canvas.width) node.vx *= -1;
            if (node.y <= 0 || node.y >= canvas.height) node.vy *= -1;
        });
    }

    // 노드 그리기 함수
    function drawNodes() {
        nodes.forEach(node => {
            ctx.beginPath();
            ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
            ctx.fillStyle = node.color; // 노드의 색상 설정
            ctx.fill();
        });
    }
    //연결 선 함수 
    function drawConnections() {
        nodes.forEach((node, index) => {
            for (let i = index + 1; i < nodes.length; i++) {
                let otherNode = nodes[i];
                let distance = Math.sqrt(Math.pow(node.x - otherNode.x, 2) + Math.pow(node.y - otherNode.y, 2));
                // console.log(distance)
                if (distance < 150) { // 거리가 150px 이하일 때만 선을 그림
                    ctx.beginPath();
                    ctx.moveTo(node.x, node.y);
                    ctx.lineTo(otherNode.x, otherNode.y);
                    ctx.lineWidth = 2; // 선의 두께를 2픽셀로 설정
                    ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)'; // 선의 색상과 투명도 설정
                    ctx.stroke();
                }
            }
        });
    }

    // 애니메이션 업데이트 함수
    function update() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // 캔버스 클리어
        updateNodePositions(); // 노드 위치 업데이트
        drawConnections(); // 노드 사이의 선 그리기
        drawNodes(); // 노드 그리기
        requestAnimationFrame(update); // 다음 프레임을 위한 업데이트 함수 호출
    }
    // 초기화
    function init() {
        createNodes(100); // 예: 100개의 노드 생성
        update();
    }
    
    init();
});
