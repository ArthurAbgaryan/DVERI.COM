let colorButton = document.querySelectorAll('.color-a');
let titleDescription = document.querySelectorAll('.title-description');
let bodyDescription = document.querySelectorAll('.body-description');
let picture = document.querySelector('#pictureDetail');
let venderCod = document.getElementById('vender-cod');
let colorTitle = document.querySelector('.title_color');
let price = document.querySelector('.price');
let buttonDescription = document.querySelector('.url_description');
buttonDescription.addEventListener('click', descriptionDoors);
let buttonComplectation = document.querySelector('.url_complectetion');
buttonComplectation.addEventListener('click',complectation);

let mainDescription = document.querySelectorAll('.main-description');
let metalAcsessory = document.querySelector('.metal_acsessory');
let detailBlock = document.querySelector('.detail-block');

let template = document.getElementById('121');

//кнопка корзина товара в детализации
let buttonProductCart = document.getElementById('productDetail');
buttonProductCart.addEventListener('click',cartAjax);


colorButton.forEach(x=>{
    let dataHref = x.getAttribute('href')
    x.addEventListener('click',go)
    })




//ТЕСТИРОВАНИЕ
async function testPostGet(e){
    e.preventDefault();
    let data = await getDataAjax('http://127.0.0.1:8000/doors/test_ajax_post/', method = 'get');
    let dataFinish = await data['arthur'];
    let lic = document.getElementById('mother');
    lic.innerText = dataFinish;
}

async function testPost(e){
    e.preventDefault();
    let data = await getDataAjax('http://127.0.0.1:8000/doors/test_ajax_post_post/', method = 'post',body = JSON.stringify({change:'change'}));
//    let dataFinish = await data['arthur'];
    let lic = document.getElementById('mother');
    lic.innerText = await data['arthur'];
}
//ТЕСТИРОВАНИЕ КОНЕЦ


//fetch для отправки get
async function getDataAjax(x,method,body){
    let header = {'X-Requested-With':'XMLHttpRequest','Content-type':'application/json'}
    if (method == "post"){
            const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
            header['X-CSRFToken'] = csrf;
                         }
    let data = await fetch(x,{
                            method: method,
                            headers:header,
                            body:body})

    let response = await data.json()
    console.log(x)
    return await response
}



function testButton(e){
    e.preventDefault();
    console.log("good job")
}


//Отправка товара и  погонажа в корзину с помощью ajax
async function cartAjax(e){
    e.preventDefault();
    let f = e.target;

    let parentEl = f.parentElement;
    let fotmParent = parentEl.parentElement;
    let hrefCartAjax = fotmParent.getAttribute('action') //ссылка
    let idAttribute = fotmParent.getAttribute('id')

    let fieldValue = fotmParent.quantity.value //значение формы
    let fieldUpdate = fotmParent.update.value //значение update формы
    let newList = hrefCartAjax.split('/'); //массив разделенного href пути
    let numberId = Number(newList[3]) // id обьекта
    let className = newList[4] //название класса обьекта
    let venderCod = document.getElementById('vender-cod').textContent
    console.log('массив разделенного href пути: ',newList);
    console.log('ссылка post: ',hrefCartAjax);
    console.log('numberId: ',numberId);
    console.log('className: ',className);
    console.log('fieldUpdate: ',fieldUpdate);
    console.log('fieldValue: ',fieldValue);
    if (fotmParent.getAttribute('id') == 'formComplectation'){
        venderCod = 'no'
    }
    let data = await getDataAjax('http://127.0.0.1:8000/cart/cart_add_ajax/',
                                  method = "post",
                                  body = JSON.stringify({id:numberId,
                                                         nameClass:className,
                                                         update:fieldUpdate,
                                                         value:fieldValue,
                                                         venderCod:venderCod
                                                         }))


}


async function descriptionDoors(e){
    e.preventDefault();
    let hrefElement1 = e.target.getAttribute('href');
    console.log('ссылка get: ',hrefElement1)
    let data = await getDataAjax(hrefElement1,method = "get");
    let properti = await data['properti'];

    mainDescription.forEach((x)=>{
        x.style.display = "block"
        })

//    Убираем основной Div раздела комплектация, если он есть
    let flex = document.querySelectorAll('.flex_table_main_complectation-table');
    if(flex !== null){
        flex.forEach((x)=>{x.style.display = "none"});
    }


//Получаем список ключей и прописываем их в описании товара
    let arrKeys = Object.keys(properti);
    arrKeys.forEach((element,index)=>{
        titleDescription[index].innerText = arrKeys[index];
        bodyDescription[index].innerText = properti[element] ;
    })
}

//Фу-ия для раздела комплектация
async function complectation(e){
    let hrefElement1 = e.target.getAttribute('href');
    e.preventDefault();
    let data = await getDataAjax(hrefElement1,method = "get");
    let properti = await data['complectation'];
    let getName = await data['get_name'];
    console.log('ссылка get: ',hrefElement1);


    mainDescription.forEach((x)=>{
        x.style.display = "none"
        })

//Удаляем блок если он был создан до этого, чтобы не было наложение повторноко контента в данном разделе
    let flex = document.querySelectorAll('.flex_table_main_complectation-table');
        if(flex !== null){
            flex.forEach((x)=>{x.remove()});
            }

//Код с помощью клона template
    let arrKeys1 = Object.keys(properti)
    console.log(properti);
    properti.forEach((element,index)=>{
        let template = document.getElementById("template121");
        let templateContent = template.content.cloneNode(true);

        detailBlock.appendChild(templateContent);
        let parent = document.querySelectorAll('.table_body_row-complectation')

        let callTitle = document.createElement("div");
        callTitle.classList.add('table-body-cell');
        callTitle.style.width = '200%'
        callTitle.innerText = element['title'];
        parent[index].appendChild(callTitle)

        let callvendor_code = document.createElement("div");
        callvendor_code.classList.add('table-body-cell');
        callvendor_code.innerText = element['vendor_code'];
        parent[index].appendChild(callvendor_code)

        let callIMG = document.createElement("div");
        callIMG.classList.add('table-body-cell');
        let imgCreate = document.createElement('img');
        imgCreate.setAttribute('src', element.pictures.small);
        callIMG.appendChild(imgCreate)
        parent[index].appendChild(callIMG)

        let callPrice = document.createElement("div");
        callPrice.classList.add('table-body-cell');
        callPrice.style.width = '50%'
        callPrice.innerText = element['price'];
        parent[index].appendChild(callPrice)
        console.log('cart/cart_add'+'/'+element.id +'/'+ getName[index])

        //Исправить, добавить класс а не ID
        let formComplectation = document.querySelectorAll('.cartForm');
        formComplectation[index].method = "post";
        formComplectation[index].action = '/cart/cart_add'+'/'+element.id +'/'+getName[0]+'/';
    })
    let cartButton = document.querySelectorAll('.isol');
    cartButton.forEach(x=>{x.addEventListener('click',cartAjax);})


}

async function go(e){
    e.preventDefault();
    let hrefElement = e.target.parentElement.getAttribute('href');
    console.log(hrefElement);
    let data = await getDataAjax(hrefElement,method = 'get');
    let dataPrice = await data['price'];
    let data1 = await data['detailImage'];
    let data2 = await data1[0]['large'];
    let dataVenderCod = await data['vendor-cod'];
    picture.setAttribute('src',data2);
    venderCod.innerText =dataVenderCod;
    price.innerText = dataPrice;
    let PropertyData = await data['proper_dict'];
    let keys = Object.keys(PropertyData);
    titleDescription.forEach((e,index)=>{e.innerText = keys.at(index)});
    bodyDescription.forEach((e,index)=>{e.innerText = PropertyData[keys.at(index)]});
    let colorT = await data['color'];
    colorTitle.innerText = colorT;

    let size = await data['size'];
    let listSizeObject = document.querySelectorAll('.size-buttom');
    let listMainSize = document.querySelector('.list_size');
    let divListSize = document.querySelectorAll('.list-size-obj');
    divListSize.forEach((x)=>x.style.display = 'none');
    for (let i=0; i<size.length; i++){
        let parentElement = document.createElement('div');
        parentElement.classList.add('list-size-obj');
        let sunElement = document.createElement('a');
        sunElement.classList.add("size-buttom");
        sunElement.innerText = size[i]['title'];
        listMainSize.appendChild(parentElement);
        parentElement.appendChild(sunElement);
    }
}