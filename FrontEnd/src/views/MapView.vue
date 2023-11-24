<template>
    <div class="map-view">
        <h1>지도</h1>
        <p>지도에서 가장 가까운 은행을 검색해보세요!</p>
        <!-- 검색창 -->
        <form @submit.prevent="searchMap" class="search">
            <select type="select" v-model="selectedLocation1">
                <option value="">선택하세요</option>
                <option v-for="location1 in locations1" :key="location1">
                    {{ location1 }}
                </option>
            </select>
            <select type="select" v-model="selectedLocation2">
                <option value="">선택하세요</option>
                <option v-for="location2 in locations2[selectedLocation1]" :key="location2">
                    {{ location2 }}
                </option>
            </select>
            <select type="select" v-model="selectedBank">
                <option value="">은행을 선택하세요</option>
                <option v-for="bank in banklist" :key="bank">
                    {{ bank }}
                </option>
            </select>
            <input type="submit" value="검색">
        </form>

        <!-- 지도 -->
        <div style="display: flex; flex-wrap: wrap;">
            <div class="map-container">
                <div id="map" class="map"></div>
                <!-- 현재 위치에서 검색 -->
                <button @click="searchNow()" class="map-btn"><i class="fa-solid fa-arrow-rotate-right"></i> 현 지도에서 검색</button>
                <!-- 지도 레벨 조절 -->
                <div class="zoom">
                    <button @click="zoomIn()" class="zoom-btn"><i class="fa-solid fa-plus"></i></button>
                    <button @click="zoomOut()" class="zoom-btn"><i class="fa-solid fa-minus"></i></button> 
                </div>
            </div>
            <!-- 오버레이창 -->
            <div class="overlay">
                <p style="font-size: 30px;">선택한 지역의 정보</p>
                <div v-if="showOverlay">
                    <div id="overlay" class="overlay-container">
                        <div class="overlay-header">
                            {{ result.place_name }}
                            <div @click="closeOverlay" title="닫기" class="close-button"><i class="fa-solid fa-xmark"></i></div>
                        </div>
                        <div class="overlay-content">
                            <div class="overlay-address">{{ result.road_address_name }}</div>
                            <div class="overlay-address">{{ result.address_name }}</div>
                            <div class="overlay-address">{{ result.phone }}</div>
                            <div class="overlay-link">
                            <a :href="result.place_url" target="_blank">카카오맵 검색</a>
                        </div>
                        </div>
                    </div>
                </div>
            </div>   
        </div>
        
        
        
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'
    let map = null
    const searchAdress = ref('')
    const showOverlay = ref(false)
    const API_KEY = '7e033eb100beade756129b908dbe16a3'
    const result = ref([])

    // 오버레이 띄우고 없애고
    const printOverlay = function(inputResult) {
        result.value = inputResult
        console.log(result.value)
        showOverlay.value = true
    }
    const closeOverlay = function () {
        showOverlay.value = false
    }

    // 지역, 은행 리스트
    const selectedLocation1 = ref('')
    const selectedLocation2 = ref('')
    const selectedBank = ref('')
    const locations1 = [
        '서울특별시', '경기도', '인천광역시', '부산광역시', '대전광역시', '대구광역시', '울산광역시', '세종특별자치시',
        '광주광역시', '강원도', '충청북도', '충청남도', '경상북도', '경상남도', '전라북도', '전라남도', '제주도'
    ]
    const locations2 = {
        '서울특별시': [
            '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구',
            '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구',
            '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'
        ],
        '경기도' : [
            "수원시 장안구", "수원시 권선구", "수원시 팔달구", "수원시 영통구", "성남시 수정구", 
            "성남시 중원구", "성남시 분당구", "의정부시", "안양시 만안구", "안양시 동안구", 
            "부천시", "광명시", "평택시", "동두천시", "안산시 상록구", "안산시 단원구", 
            "고양시 덕양구", "고양시 일산동구", "고양시 일산서구", "과천시", "구리시", 
            "남양주시", "오산시", "시흥시", "군포시", "의왕시", "하남시", "용인시 처인구", 
            "용인시 기흥구", "용인시 수지구", "파주시", "이천시", "안성시", "김포시", "화성시", 
            "광주시", "양주시", "포천시", "여주시", "연천군", "가평군", "양평군"
        ],
        '인천광역시' : [ 
            "계양구", "미추홀구", "남동구", "동구", "부평구", "서구", 
            "연수구", "중구", "강화군", "옹진군" 
        ],
        '부산광역시': [
            "강서구", "금정구", "남구", "동구", "동래구", "부산진구", "북구", "사상구", "사하구", "서구", 
            "수영구", "연제구", "영도구", "중구", "해운대구", "기장군"
        ],
        '대전광역시': [
            "대덕구", "동구", "서구", "유성구", "중구"  
        ],
        '대구광역시': [
            "남구", "달서구", "동구", "북구", "서구", "수성구", "중구", "달성군"
        ],
        '울산광역시': [
            "남구", "동구", "북구", "중구", "울주군"
        ],
        '세종특별자치시': ["세종특별자치시"],
        '광주광역시' :[
            "광산구", "남구", "동구", "북구", "서구"
        ],
        '강원도': [
            "춘천시", "원주시", "강릉시", "동해시", "태백시", "속초시", "삼척시", "홍천군", "횡성군", "영월군", 
            "평창군", "정선군", "철원군", "화천군", "양구군", "인제군", "고성군", "양양군"
        ],
        '충청북도': [
            "청주시 상당구", "청주시 서원구", "청주시 흥덕구", "청주시 청원구", "충주시", "제천시", 
            "보은군", "옥천군", "영동군", "증평군", "진천군", "괴산군", "음성군", "단양군"
        ],
        '충청남도': [
            "천안시 동남구", "천안시 서북구", "공주시", "보령시", "아산시", "서산시", "논산시", "계룡시", 
            "당진시", "금산군", "부여군", "서천군", "청양군", "홍성군", "예산군", "태안군" 
        ],
        '경상북도': [
            "포항시 남구", "포항시 북구", "경주시", "김천시", "안동시", "구미시", "영주시", "영천시", 
            "상주시", "문경시", "경산시", "군위군", "의성군", "청송군", "영양군", "영덕군", "청도군", 
            "고령군", "성주군", "칠곡군", "예천군", "봉화군", "울진군", "울릉군" 
        ],
        '경상남도': [
            "창원시 의창구", "창원시 성산구", "창원시 마산합포구", "창원시 마산회원구", "창원시 진해구", 
            "진주시", "통영시", "사천시", "김해시", "밀양시", "거제시", "양산시", "의령군", "함안군", 
            "창녕군", "고성군", "남해군", "하동군", "산청군", "함양군", "거창군", "합천군"
        ],
        '전라북도': [
            "전주시 완산구", "전주시 덕진구", "군산시", "익산시", "정읍시", "남원시", "김제시", 
            "완주군", "진안군", "무주군", "장수군", "임실군", "순창군", "고창군", "부안군"
        ],
        '전라남도': [
            "목포시", "여수시", "순천시", "나주시", "광양시", "담양군", "곡성군", "구례군", 
            "고흥군", "보성군", "화순군", "장흥군", "강진군", "해남군", "영암군", "무안군", 
            "함평군", "영광군", "장성군", "완도군", "진도군", "신안군"
        ],
        '제주도': [
            "서귀포시", "제주시"
        ]
    }
    const banklist = [
        '', '하나은행', 'SC제일은행', 'KB국민은행', '신한은행', '외한은행', 
        '우리은행', '씨티은행', 'IBK기업은행', 'NH농협은행', 'Sh수협은행', 'KDB산업은행',
        '한국수출입은행', '경남은행', '광주은행', '대구은행', '부산은행', '전북은행', '제주은행'
    ]

    onMounted(() => {
        if (window.kakao && window.kakao.maps) {
            initMap()
        } else {
            const script = document.createElement('script')
            /* global kakao */
            script.onload = () => kakao.maps.load(initMap)
            script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}&libraries=services`
            document.head.appendChild(script)
        }
    })

    // 처음위치 띄우기
    const initMap = () => {
        const container = document.getElementById('map')
        console.log(window.kakao)
        const options = {
            center: new kakao.maps.LatLng(37.5013068, 127.0396597),
            level: 5,
        }
        map = new kakao.maps.Map(container, options)
    }



    // 위치 검색 후 위치 옮기기 + 은행 찾기
    const searchMap = () => {

        var geocoder = new kakao.maps.services.Geocoder()
        searchAdress.value = `${selectedLocation1.value} ${selectedLocation2.value}`
        geocoder.addressSearch(searchAdress.value, function(result, status) {
            // 정상적으로 검색이 완료됐으면 
            if (status === kakao.maps.services.Status.OK) {
                var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
                // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
                map.setCenter(coords)
                findBankMap()
            }
        })
    }

    // 현재 위치에서 검색하기
    const searchNow = () => {
        selectedLocation1.value = ''
        selectedLocation2.value = ''
        findBankMap()
    }
    // 은행 찾아서 마커 찍기
    const findBankMap = () => {
        var infowindow = new kakao.maps.InfoWindow({zIndex:1})
        // 장소 검색 객체를 생성합니다
        var ps = new kakao.maps.services.Places(map)

        // 카테고리로 은행을 검색합니다
        ps.categorySearch('BK9', placesSearchCB, {useMapBounds:true})
        // 키워드 검색 완료 시 호출되는 콜백함수 입니다
        function placesSearchCB (data, status, pagination) {
            if (status === kakao.maps.services.Status.OK) {
                for (var i=0; i<data.length; i++) {
                    // console.log(data[i])
                    const bankName = data[i].category_name
                    if (bankName.includes(selectedBank.value)){
                        displayMarker(data[i])    
                    }
                }       
            }
        }

        // 지도에 마커를 표시하는 함수입니다
        function displayMarker(place) {
            // 마커를 생성하고 지도에 표시합니다
            var marker = new kakao.maps.Marker({
                map: map,
                position: new kakao.maps.LatLng(place.y, place.x) 
            })

            // 마커에 마우스 올리면 장소명
            kakao.maps.event.addListener(marker, 'mouseover', function() {
                infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
                infowindow.open(map, marker)
            });
            // 마커에서 마우스 떼면 없어지게
            kakao.maps.event.addListener(marker, 'mouseout', function() {
                infowindow.close()
            });
            // 마커를 클릭하면 검색(콘솔창 참고)
            kakao.maps.event.addListener(marker, 'click', function() {
                var places = new kakao.maps.services.Places()
                var callback = function(result, status) {
                    if (status === kakao.maps.services.Status.OK) {
                        printOverlay(result[0])
                        // window.location.href=`${result[0]}`
                    }
                }
                places.keywordSearch(place.place_name, callback)
            });

        }
    }


    // 지도 확대 & 축소
    const zoomIn = function() {        
        var level = map.getLevel();
        map.setLevel(level - 1);
    }   
    const zoomOut = function() {    
        var level = map.getLevel(); 
        map.setLevel(level + 1);
    }  
</script>

<style scoped>

/* 전체 페이지 반응형임 */
.map-view {
    padding: 50px 20px;
}
@media screen and (min-width: 1400px) {
    .map-view {
        padding: 50px 200px;
    }
}

/* 맵 사이즈 */
.map-container {
    margin: auto;
    position: relative;
    width: 60%;
    min-width: 200px;
    height: 500px;
    box-shadow: 0px 4px 8px rgba(119, 119, 119, 0 .9);
}
.map {
    width: 100%;
    height: 500px;
}
/* 여기서 검색하기 버튼 */
.map-btn {
    border: 1px solid #86c5c7;
    width: 180px;
    height: 50px;
    background-color: #86c5c7;
    border-radius: 20px;
    position: absolute;
    bottom: 30px;
    left: 50%;
    z-index: 20;
    transform: translateX(-50%);
    box-shadow: 0px 4px 8px rgba(119, 119, 119, 0.9);
}
.zoom {
    position: absolute;
    width: 80px;
    top: 20px;
    right: 0px;
    z-index: 20;
    transform: translateX(-50%);
}
.zoom-btn {
    width: 35px;
    margin: 0 2px;
    border: 1px solid #86c5c7;
    background-color: #86c5c7;
    box-shadow: 0px 4px 8px rgba(119, 119, 119, 0.9);
}
/* 검색창 */
.search {
    display: flex;
    /* justify-content: center; */
    margin: 30px 0px;
}
.search select {
    margin: 0 5px;
}

/* 오버레이용 */
.overlay {
    min-width: 150px;
    padding: 30px;
    width: 35%;
    
}
.overlay-container {
  padding: 15px;
  border: 1px solid #ccc;
  background-color: #fff;
  width: 100%;
  height: 350px;
  box-shadow: 0px 4px 8px rgba(119, 119, 119, 0.9);
}

.overlay-header {
  font-size: 2em;
  margin: 20px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.close-button {
  width: 10%;
  height: 16px;
  cursor: pointer;
}

.overlay-content {
  font-size: 1.3em;
  margin-top: 20px;
  padding-top: 20px;
}

.overlay-address {
    margin: 10px 0;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.overlay-link {
  margin-top: 5px;
}

.overlay-link a {
    font-size: 1.4em;
  color: #86c5c7;
  text-decoration: none;
}

@media screen and (max-width: 1100px) {
    .overlay-header{
        font-size: 1.2em;
    }
    .overlay-link a {
        font-size: 1.2em;
    }
    .overlay-content {
        font-size: 0.8em;
    }
}
@media screen and (max-width: 800px) {
    .overlay {
        display: none;        
    }
}
</style>