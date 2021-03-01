let moneyUnit = {
    "ONE HUNDRED": 100.0 ,
    "TWENTY": 20.0 ,
    "TEN": 10.0 ,
    "FIVE": 5.0 ,
    "ONE": 1.0 ,
    "QUARTER": 0.25 ,
    "DIME": 0.1 ,
    "NICKEL": 0.05 ,
    "PENNY": 0.01
};
// 从小于现金的最大面额开始，减，如果为0，就往下一层
// 接着减，直到抽屉没钱或者要找钱的为零；
function checkCashRegister(price, cash, cid) {
    // 深度复制
    let backup = cid.map(m => m.slice());
    let payBack = cash - price;
    let changeContent = [];
    // 判断是否有足够的钱找零
    if (cid.filter(m => {
        return  moneyUnit[m[0]] <= payBack;
    }).reduce((acc, m)=> {return acc+ m[1]}, 0) < payBack) {
        return {status: "INSUFFICIENT_FUNDS", change: []};
    }
    // 开始找零
    while (payBack > 0) {
        payBack = Math.round(payBack * 100) / 100;
        if (payBack >= 100 && cid.filter(m => m[0] === "ONE HUNDRED")[0][1] > 0) {
            payBack -= 100;
            cid.map(m => {
                if (m[0] === "ONE HUNDRED") {
                    m[1] -= 100;
                    changeContent.push([m[0], 100]);
                }
            })
        } else if (payBack >= 20 && cid.filter(m => m[0] === "TWENTY")[0][1] > 0) {
            payBack -= 20;
            cid.map(m => {
                if (m[0] === "TWENTY") {
                    m[1] -= 20;
                    changeContent.push([m[0], 20]);
                }
            })
        } else if (payBack >= 10 && cid.filter(m => m[0] === "TEN")[0][1] > 0) {
            payBack -= 10;
            cid.map(m => {
                if (m[0] === "TEN") {
                    m[1] -= 10;
                    changeContent.push([m[0], 10]);
                }
            })
        } else if (payBack >= 5 && cid.filter(m => m[0] === "FIVE")[0][1] > 0) {
            payBack -= 5;
            cid.map(m => {
                if (m[0] === "FIVE") {
                    m[1] -= 5;
                    changeContent.push([m[0],5]);
                }
            })
        } else if (payBack >= 1 && cid.filter(m => m[0] === "ONE")[0][1] > 0) {
            payBack -= 1;
            cid.map(m => {
                if (m[0] === "ONE") {
                    m[1] -= 1;
                    changeContent.push([m[0], 1]);
                }
            })
        } else if (payBack >= 0.25 && cid.filter(m => m[0] === "QUARTER")[0][1] > 0) {
            payBack -= 0.25;
            cid.map(m => {
                if (m[0] === "QUARTER") {
                    m[1] -= 0.25;
                    changeContent.push([m[0], 0.25]);
                }
            })
        } else if (payBack >= 0.1 && cid.filter(m => m[0] === "DIME")[0][1] > 0) {
            payBack -= 0.1;
            cid.map(m => {
                if (m[0] === "DIME") {
                    m[1] -= 0.1;
                    changeContent.push([m[0], 0.1]);
                }
            })
        } else if (payBack >= 0.05 && cid.filter(m => m[0] === "NICKEL")[0][1] > 0) {
            payBack -= 0.05;
            cid.map(m => {
                if (m[0] === "NICKEL") {
                    m[1] -= 0.05;
                    changeContent.push([m[0], 0.05]);
                }
            })
        } else if (payBack >= 0.01 && cid.filter(m => m[0] === "PENNY")[0][1] > 0) {
            payBack -= 0.01;
            cid.map(m => {
                if (m[0] === "PENNY") {
                    m[1] -= 0.01;
                    m[1] = Math.round(m[1] * 100) /100;
                    changeContent.push([m[0], 0.01]);
                }
            })
        }
    }
    // changeContent 去重
    let result = {};
    for (let m of changeContent) {
        if (result.hasOwnProperty(m[0])) {
            result[m[0]] += m[1];
        } else {
            result[m[0]] = m[1];
        }
    }
    let content = [];
    Object.getOwnPropertyNames(result).forEach(function(key){
        content.push([key, result[key]]);
    })
    if (Math.round(cid.reduce((acc, m)=> {return acc+ m[1]}, 0)*100)/100 === 0) {
        return {status: "CLOSED", change: backup};
    } else {
        return {status: "OPEN", change: content};
    }
}

checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);