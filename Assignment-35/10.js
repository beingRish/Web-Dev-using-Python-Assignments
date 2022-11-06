/*
10. Create a human readable time format using the Date time object
a. YYYY-MM-DD HH:mm
b. DD-MM-YYYY HH:mm
c. DD/MM/YYYY HH:mm
*/

/*function humanRedableTime1(num) {
    return num.toString().padStart(2, '0');
  }
  
  function formatDate(date) {
    return (
      [
        date.getFullYear(),
        humanRedableTime1(date.getMonth() + 1),
        humanRedableTime1(date.getDate()),
      ].join('-') +
      ' ' +
      [
        humanRedableTime1(date.getHours()),
        humanRedableTime1(date.getMinutes()),
        //humanRedableTime1(date.getSeconds()), This step is optional 
      ].join(':')
    );
  }
  
  //  2021-10-24 16:21:23 (yyyy-mm-dd hh:mm:ss)
  console.log(formatDate(new Date()));*/
  

  /*function humanRedableTime2(num) {
    return num.toString().padStart(2, '0');
  }
  function formateDate(date){
    return [
        humanRedableTime2(date.getDate()),
        humanRedableTime2(date.getMonth()+1),
        date.getFullYear(),
    ].join('-') +
    ' '+
    [
        humanRedableTime2(date.getHours()),
        humanRedableTime2(date.getMinutes()),
        //humanRedableTime2(date.getSeconds()), This step is optional 
    ].join(':')
    
  }
  // DD-MM-YYYY HH:mm 
  console.log(formateDate(new Date())); */


  function humanRedableTime3(num) {
    return num.toString().padStart(2, '0');
  }

  function formateDate(date){
    return [
        humanRedableTime3(date.getDate()),
        humanRedableTime3(date.getMonth()+1),
        date.getFullYear(),
    ].join('/') +
    ' '+

    [
        humanRedableTime3(date.getHours()),
        humanRedableTime3(date.getMinutes()),
        //humanRedableTime3(date.getSeconds()), This step is optional 
    ].join(':')
    
  }

  // DD/MM/YYYY HH:mm 
  console.log(formateDate(new Date()));
