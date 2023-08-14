$(document).ready(function () {

    let SHEET_ID = '1mmFG39YIzlr0ZYn06ziIN6uhy9uu40XQx288KuxrZzM';
    let SHEET_TITLE = 'Products';
    // let SHEET_RANGE = "A1:E106";  + '&range=' + SHEET_RANGE
    let FULL_URL = ('https://docs.google.com/spreadsheets/d/' + SHEET_ID + '/gviz/tq?sheet=' + SHEET_TITLE);

    fetch(FULL_URL)
    .then(res => res.text())
    .then(rep => {
        let data = JSON.parse(rep.substr(47).slice(0,-2));
        let productHtml = '';
        (data.table.rows).forEach(function(item){
            productHtml += `
                <div class="col-sm-6 col-md-4 col-lg-3 p-b-35 isotope-item ${item.c[3].v}">
                    <div class="block2">
                        <div class="block2-pic hov-img0">
                            <img src="${item.c[0].v}" alt="IMG-PRODUCT">
                
                            <a href="${item.c[4].v}" target="_blank" class="block2-btn flex-c-m stext-103 cl10 size-102 bg10 bor2 hov-btn1 p-lr-15 trans-04 js-show-modal1">
                                Purchase
                            </a>
                        </div>
                
                        <div class="block2-txt flex-w flex-t p-t-14">
                            <div class="block2-txt-child1 flex-col-l ">
                                <div class="stext-104 cl4 hov-cl1 trans-04 js-name-b2 p-b-6">
                                    ${item.c[1].v}
                                </div>
                
                                <span class="stext-105 cl3">
                                ₹${item.c[2].v}
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
                `;
        });
        $('.isotope-grid').html(productHtml);

    })
})