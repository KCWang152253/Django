$(document).ready(function () {
    var accunt =document.getElementById("accunt")
    var pass = document.getElementById("pass")
    var  passwd = document.getElementById("passwd")

    var  accunterr = document.getElementById("accunterr")
    var  checkerr =document.getElementById("checkerr")
    var  passerr = document.getElementById('passerr')
    var  passwderr =document.getElementById('passwderr')
    //添加聚焦事件
    accunt.addEventListener("focus",function () {
            accunterr.style.display="none"
            checkerr.style.display = "none"

        },false)
    //添加离焦事件
    accunt.addEventListener("blur",function () {
        instr = this.value
        if(instr.length <6 ||instr.length>12) {
            accunterr.style.display = "block"
            return
        }
        $.post("/checkuserid/",{"userid":instr},function (data) {
            if (data.status=="error"){
                checkerr.style.display="block"
            }

        })
    },false)




    //添加聚焦事件
    pass.addEventListener("focus",function () {
            passerr.style.display="none"

        },false)
    //添加离焦事件
    pass.addEventListener("blur",function () {
        instr = this.value
        if(instr.length <6 ||instr.length>16) {
            passerr.style.display = "block"
            return
        }

    },false)




        //添加聚焦事件
    passwd.addEventListener("focus",function () {
            passwderr.style.display="none"

        },false)
    //添加离焦事件
    passwd.addEventListener("blur",function () {
        instr = this.value
        if(instr != pass.value) {
            passwderr.style.display = "block"
            return
        }

    },false)




    //     }else {
    //     //    验证邮箱是否被注册
    //         console.log("******************1")
    //         $.ajax({
    //             url:"/chenkuserid/",
    //             type:"post",
    //             typedata:"json",
    //             data:{"checkid":accunt.value},
    //             success:function (data) {
    //                 console.log(data)
    //                 if (data.status=="error"){
    //                     checkerr.style.display="block"
    //                 }
    //             }
    //         })
    //     }
    //
    //
    // },false)
    //
    // pass.addEventListener("focus",function () {
    //     passerr.style.display="none"
    //
    // },false)
    // pass.addEventListener("blur",function () {
    //    var inputStr = this.value
    //     if (inputStr.length<6||inputStr.length>16){
    //         passerr.style.display="block"
    //     }
    //
    // },false)
    //
    //
    // passwd.addEventListener("focus",function () {
    //     passwderr.style.display="none"
    //
    // },false)
    // passwd.addEventListener("blur",function () {
    //     var inputStr = this.value
    //     if (inputStr !=pass.value){
    //         passwderr.style.display="block"
    //     }
    //

})