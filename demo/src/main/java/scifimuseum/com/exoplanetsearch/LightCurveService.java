package scifimuseum.com.exoplanetsearch;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class LightCurveService {

    private final LightCurveRepository lightCurveRepository;

    @Autowired
    public LightCurveService(LightCurveRepository lightCurveRepository) {
        this.lightCurveRepository = lightCurveRepository;
    }

    public List<LightCurve> getAllLightCurves() {
        return lightCurveRepository.findAll();
    }

    public Optional<LightCurve> getLightCurveById(Long id) {
        return lightCurveRepository.findById(id);
    }

    public LightCurve saveLightCurve(LightCurve lightCurve) {
        return lightCurveRepository.save(lightCurve);
    }

    public void deleteLightCurve(Long id) {
        lightCurveRepository.deleteById(id);
    }

    // Additional methods for updating, and other business logic can be added here
}
