import PyPDF2
a=['PurchaseOrder_83332.pdf', 'PurchaseOrder_83646.pdf', 'PurchaseOrder_83505.pdf', 'PurchaseOrder_83480.pdf', 'PurchaseOrder_83468.pdf', 'PurchaseOrder_83125.pdf', 'PurchaseOrder_82772.pdf', 'PurchaseOrder_82592.pdf', 'PurchaseOrder_81974.pdf', 'PurchaseOrder_77780.pdf', 'PurchaseOrder_80950.pdf', 'PurchaseOrder_80848.pdf', 'PurchaseOrder_80753.pdf', 'PurchaseOrder_78929.pdf']
po_no=[]
date=[]
sku=[]
p_name=[]
qty=[]
price=[]   
pdfFileObj=open('d:/github/personal/python/innovations/google api/order files/PurchaseOrder_83707.pdf','rb') 
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
pageObj=pdfReader.getPage(0)
a=pageObj.extractText()
b=a.split('\n')
print(b)
for x in b:
    if x[:5]=='PO No':
        po_no.append(x[-5:])
        break
del x
for x in b:
    if x[:7]=='PO Date':
        date.append(x[-10:])
        break
del x
for x in b:
    if x[:4]=='ASSC':
        sku.append(x)
        break
del x
for x in range(len(b)):
    if b[x][:4]=='ASSC':
        cnt=x+2
        if b[cnt+2]!='Size' and b[cnt+3]!="X":
            p_name.append(b[cnt]+' '+b[cnt+1])
            qty.append(b[cnt+4])
            break
        elif b[cnt+2]=='Size':
            p_name.append(b[cnt])
            qty.append(b[cnt+3])
            break
        elif b[cnt+4][0].isnumeric():
            qty.append(b[cnt+5])
del x
for x in range(len(b)):
    if b[x]=='Total Amount (Inc of Taxes)':
        price.append(b[x+1])
        break
pdfFileObj.close()
