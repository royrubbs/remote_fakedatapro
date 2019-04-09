from django.shortcuts import render

from django.shortcuts import render,redirect
from .models import FakeData
import faker
fake=faker.Faker()
def insertingview(request):
    for i in range(500):
        first_name=fake.first_name()
        last_name=fake.last_name()
        sal=fake.random_element(elements=(1000,2000,3000,1500))
        job=fake.random_element(elements=('HR','SW','SM','PM'))
        loc=fake.random_element(elements=('hyd','bang','pune','mumbai'))
        data=FakeData(
            first_name=first_name,
            last_name=last_name,
            email=email,
            sal=sal,
            loc=loc,
            job=job
        )
        data.save()
        return redirect('/home/')

    def fetchingview(request):
        fdata=FakeData.objects.all()
        return render(request,'fakedata.html',{'fdata':fdata})


