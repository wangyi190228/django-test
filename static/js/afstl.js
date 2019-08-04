// days of annual leave
function indate(){  
    var totaldays = 0;
    // al starttime gain
    var startdate = document.getElementById('startin').value;
    var start = document.getElementById('alstartin');
    var startindex = start.selectedIndex;
    var starttime=start[startindex].text;

    // al stoptime gain
    var stopdate = document.getElementById('stopin').value;  
    var stop = document.getElementById('alstopin');
    var stopindex = stop.selectedIndex;
    var stoptime=stop[stopindex].text;
    
    // calculate the days
　  var sdate = new Date(startdate); 
  　var now = new Date(stopdate); 
  　var days = now.getTime() - sdate.getTime(); 
  　var totaldays = parseInt(days / (1000 * 60 * 60 * 24)); 
    if(totaldays < 0){
        alert("error!");
        totaldays = 0;
    }else{
        if(starttime == "9:00" && stoptime == "17:30"){
            totaldays++;
        }else if((starttime == "9:00" && stoptime == "13:00") || (starttime == "13:00" && stoptime == "17:30")){
            totaldays += 0.5;
        }
    }
    if(totaldays>=0)
        document.getElementById('numofday').value = totaldays;   
} 

