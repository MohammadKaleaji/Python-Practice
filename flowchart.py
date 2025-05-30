from graphviz import Digraph

# Create a new Digraph
flow = Digraph(comment="Order Distribution Flow (New Method - Based on Delivery Time)")

# Main entry
flow.node("A", "طلب جديد")

# Step 1: Check external provider eligibility
flow.node("B", "هل يطابق شروط الشركات الخارجية؟")
flow.edge("A", "B")

# External provider eligible
flow.node("C", "أرسل للشركات الخارجية")
flow.edge("B", "C", label="نعم")

# Start aggregation timer
flow.node("D", "ابدأ مؤقت التجميع (مثلاً 10 دقائق)")
flow.edge("B", "D", label="لا")

# Step 2: External company response
flow.node("E", "هل تم قبول الطلب؟")
flow.edge("C", "E")

# Accepted by external company
flow.node("F", "تابع عملية التوصيل")
flow.edge("E", "F", label="نعم")

# Not accepted or failed all external options
flow.node("G", "هل هناك سلسلة؟")
flow.edge("E", "G", label="لا")

flow.node("H", "هل فشلت كل الشركات؟")
flow.edge("G", "H", label="نعم")

flow.node("I", "ابحث عن سلة مناسبة")
flow.edge("H", "I", label="نعم")

flow.node("J", "هل توجد سلة مناسبة؟")
flow.edge("I", "J")

flow.node("K", "أضف الطلب للسلة المناسبة وأرسله مباشرة")
flow.edge("J", "K", label="نعم")

flow.node("L", "أنشئ سلة جديدة وأضف الطلب")
flow.edge("J", "L", label="لا")

# Aggregation expires
flow.node("M", "انتهى وقت التجميع؟")
flow.edge("D", "M")

flow.node("N", "ابدأ تجميع الطلبات")
flow.edge("M", "N", label="نعم")

flow.node("O", "رتب الطلبات حسب أسرع مسار")
flow.edge("N", "O")

flow.node("P", "احذف الطلبات غير المؤهلة")
flow.edge("O", "P")

flow.node("Q", "اسند الطلبات المناسبة للسلال")
flow.edge("P", "Q")

flow.render('/home/kaleaji/Desktop/python-clone/Python-Practice/order_distribution_flowchart.png')
