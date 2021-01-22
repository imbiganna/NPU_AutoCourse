src='http://code.jquery.com/jquery-1.9.1.min.js'>
function myFunct (){
    //nothing just test
};

var uid;
var pwd;
var courseListName = new Array();;
var needCourseList = new Array();;

function getdata () {
    uid = document.getElementById("uid").value;
    pwd = document.getElementById("pwd").value;
    if(uid == '' || pwd == '') {
        alert("請輸入帳號密碼");
    }
    else
    {
        document.getElementById("loginBtnLoad").hidden=false;
        document.getElementById("loginBtn").disabled=true;
        $.ajax({
            url: "http://127.0.0.1:5000/?uid="+uid+"&pwd="+pwd,   //存取Json的網址
            type: "GET",
            cache:false,
            dataType: 'json',
            contentType: "application/json",
            crossDomain: true,
            success: function (data) {

                if (data[0]["stdid"] == "fail"){
                    alert("登入失敗，請檢查帳號密碼。")
                    uid=undefined;
                    pwd=undefined;
                }else{
                    document.getElementById("loginbar").hidden=true;
                    document.getElementById('status').innerHTML = data[0]["stdid"]+"已登入 祝你搶課順利🥰";
                    alert(data[0]["stdid"]+"已登入 祝你搶課順利🥰");
                }
                document.getElementById("loginBtnLoad").hidden=true;
                document.getElementById("loginBtn").disabled=false;
            },

        });
    }
};
let tabName = ['cou_name','cou_date','canselect']
var myData = new Array();
function getCourse(){
    cname = document.getElementById("couName").value;
    document.getElementById("loadingBtn").hidden=false;
    document.getElementById("searchBtn").disabled=true;
    document.getElementById('courseList').innerHTML = '';
    $.ajax({
        url: "http://127.0.0.1:5000/?name="+cname,
        type: "GET",
        cache:false,
        dataType: 'json',
        contentType: "application/json",
        crossDomain: true,
        success: function (data) {
            myData=data;
            var ul = document.getElementById("courseList");
            for (i=0 ; i<data.length ;i++) {

                var li = document.createElement("tr");
                li.setAttribute("id", "course"+i);
                ul.appendChild(li)
                var nTable = document.getElementById("course"+i);

                for (var j = 0 ; j<3 ; j++){
                    var nTableid = document.createElement("td");
                    nTableid.setAttribute("CouID","course0"+i);
                    nTableid.innerHTML = data[i][tabName[j]];
                    nTable.appendChild(nTableid);
                }

                var nButton = document.createElement("td");
                nButton.innerHTML = "<button class=\"btn btn-primary\" type=\"button\" onclick=\"addCourse("+i+");\" id=\"addBtn"+data[i]["cou_id"]+"\" style=\" \">新增</button>";
                nTable.appendChild(nButton);

                nButton = document.createElement("td");
                nButton.innerHTML = "<button class=\"btn btn-primary\" type=\"button\" onclick=\"viewDetial('"+i+"');\" data-toggle=\"modal\" data-target=\"#coudetial\" id=\"detial"+data[i]["cou_id"]+"\" style=\"background: rgb(89,90,94)\"> 詳細 </button>";
                nTable.appendChild(nButton);
                myData[i]['indID']=i;

            }
            document.getElementById("loadingBtn").hidden=true;
            document.getElementById("searchBtn").disabled=false;
            //alert(data[0]["cou_name"]);
        },

    });

};
let nameList = ["cou_name","cou_id","cou_score","cou_class","cou_dept","cou_times","cou_requ","cou_teach","cou_room","cou_info","canselect"];
let need_print = ["課程名稱：","課程代號：","學分數：","開課班級：","開課系所：","時數：","必選修：","授課教師：","授課教室：","備註：","可選人數："];

function viewDetial(ind){
    document.getElementById('coudtlList').innerHTML = '';
    let nTable = document.getElementById("coudtlList");
    for (j=0;j<11;j++){
        var nTableid = document.createElement("p");
        nTableid.innerHTML = need_print[j]+myData[ind][nameList[j]];
        nTable.appendChild(nTableid);
    }
}

function addCourse(id){
    let courseID = myData[id]['cou_id']
    needCourseList[courseID]=(myData[id]);
    let chgbtn = document.getElementById("addBtn"+courseID);
    chgbtn.setAttribute("onclick","delCourse('"+courseID+"','"+needCourseList[courseID]['indID']+"');");
    chgbtn.setAttribute("style","background: rgb(238,45,88)");
    chgbtn.innerHTML="移除";
    updateNeedList();
}

function delCourse(cId,indID){
    let chgbtn = document.getElementById("addBtn"+cId);
    delete needCourseList[cId];
    chgbtn.setAttribute("onclick","addCourse('"+indID+"');");
    chgbtn.setAttribute("style"," ");
    chgbtn.innerHTML="新增";
    updateNeedList();

}

let updList = ['cou_name','cou_id','canselect'];

function updateNeedList(){
    document.getElementById('selCourseList').innerHTML = '';
    let updateList = document.getElementById("selCourseList");
    for (let key in needCourseList){
        console.log(key);
        let li = document.createElement("tr");
        li.setAttribute("id", "needCourse"+key);
        updateList.appendChild(li)
        let nTable = document.getElementById("needCourse"+key);

        for (let j = 0 ; j<3 ; j++){
            let nTabloid = document.createElement("td");
            nTabloid.setAttribute("CouID","needCourse0"+key);
            nTabloid.innerHTML = needCourseList[key][updList[j]];
            nTable.appendChild(nTabloid);
        }

        let nButton = document.createElement("button");
        nButton.setAttribute("class","btn btn-primary");
        nButton.setAttribute("type","button");
        nButton.setAttribute("onclick","delCourse('"+needCourseList[key]["cou_id"]+"','"+needCourseList[key]['indID']+"');");
        nButton.setAttribute("id","addBtn"+needCourseList[key]["cou_id"]);
        nButton.setAttribute("style","background: rgb(238,45,88)");
        nButton.innerHTML = "移除";
        nTable.appendChild(nButton);
    }
}
s
function goCourse(){
    if (uid == undefined || pwd == undefined) {
        alert("請先登入！");
    }else {

        alert("還不能偷跑啦！！");
    }
}