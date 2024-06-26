Deck.GL layers can be added to the map with `Map.add_deck_layers`.

They are defined as a dictionary, where classes  got the `@@type` prefix and getter props
the `@@=` prefix. They are inserted into the layer stack of the maplibre context. Therefore,
you can also pass a `beforeId` prop.

Here is an example corresponding to the [Deck.GL GridLayer API Example](https://deck.gl/docs/api-reference/aggregation-layers/grid-layer):

```python
grid_layer = {
    "@@type": "GridLayer", # JS: new GridLayer
    "id": "my-awsome-grid-layer",
    "data": "https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf-bike-parking.json",
    "extruded": True,
    "getPosition": "@@=COORDINATES", # JS: d => d.COORDINATES
    "getColorWeight": "@@=SPACES", # JS: d => d.SPACES
    "getElevationWeight": "@@=SPACES", # JS: d => d.SPACES
    "elevationScale": 4,
    "cellSize": 200,
    "pickable": True,
    "beforeId": "first-labels-layer" # optional
    }
```

The Code above will generate the following JavaScript code:

```javascript
const gridLayer = new GridLayer({
  id: 'GridLayer',
  data: 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf-bike-parking.json',
  extruded: true,
  getPosition: d => d.COORDINATES,
  getColorWeight: d => d.SPACES,
  getElevationWeight: d => d.SPACES,
  elevationScale: 4,
  cellSize: 200,
  pickable: true
});
```

See also:

- [Deck.GL Layer](../examples/deckgl_layer)
- [Deck.GL Multiple Layers](../examples/deckgl_multiple_layers)
