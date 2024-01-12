package scifimuseum.com.exoplanetsearch;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface LightCurveRepository extends JpaRepository<LightCurve, Long> {
     // custom queries here
}
