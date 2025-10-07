def update():
    chai="eilaichi"
    def kitchen():
        nonlocal chai
        chai="kesar"
    kitchen()
    print("after",chai)
update()