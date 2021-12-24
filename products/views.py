from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Wine, WineType, Region, Winery
from .forms import ProductForm


def all_wines(request):
    """ A view to return all wines, including sorting and search queries """

    products = Wine.objects.all()
    query = None
    wine_types = None
    regions = None
    wineries = None
    grapes = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            print(sortkey)
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'wine_type' in request.GET:
            wine_types = request.GET['wine_type']
            products = products.filter(wine_type__name=wine_types)
            wine_types = WineType.objects.filter(name__in=wine_types)

        if 'region' in request.GET:
            regions = request.GET['region']
            products = products.filter(region__name=regions)
            regions = Region.objects.filter(name__in=regions)

        if 'winery' in request.GET:
            wineries = request.GET['winery']
            products = products.filter(winery__name=wineries)
            wineries = Winery.objects.filter(name__in=wineries)

        if 'grape' in request.GET:
            grapes = request.GET['grape']
            products = products.filter(grape__name=grapes)
            grapes = Wine.objects.filter(grape__in=grapes)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_wine_types': wine_types,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Wine, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, admission denied')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.errors(request, 'Failed to add product. Ensure the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, admission denied')
        return redirect(reverse('home'))

    product = get_object_or_404(Wine, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
    messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, admission denied')
        return redirect(reverse('home'))

    product = get_object_or_404(Wine, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))