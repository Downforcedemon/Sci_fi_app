package scifimuseum.com.exoplanetsearch;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/lightcurves")
public class LightCurveController {

    private final LightCurveService lightCurveService;

    @Autowired
    public LightCurveController(LightCurveService lightCurveService) {
        this.lightCurveService = lightCurveService;
    }

    @GetMapping
    public List<LightCurve> getAllLightCurves() {
        return lightCurveService.getAllLightCurves();
    }

    @GetMapping("/{id}")
    public ResponseEntity<LightCurve> getLightCurveById(@PathVariable Long id) {
        return lightCurveService.getLightCurveById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public LightCurve addLightCurve(@RequestBody LightCurve lightCurve) {
        return lightCurveService.saveLightCurve(lightCurve);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> deleteLightCurve(@PathVariable Long id) {
        lightCurveService.deleteLightCurve(id);
        return ResponseEntity.ok().build();
    }

    // Additional endpoints for updating, etc., can be added here
}

