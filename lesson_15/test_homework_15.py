import pytest

class Romb:    
    side = 10    
    angle_a = 90
    angle_b = 90


class TestRomb:

    @pytest.mark.parametrize(
            'side, angle_a, angle_b',
            [
                (5, 110, 70),
                (20, 90, 90),
                
            ],
            ids=[
                'Different angles',
                'Equal angles',
            ],
    )
    def test_pos(self, side, angle_a, angle_b):
        p = Romb()

        setattr(p, 'side', 1 if side==0 else side)
        setattr(p, 'angle_a', angle_a if 0 < angle_a < 180 and 0 < angle_b < 180 and angle_b+angle_a ==180 else 90)
        setattr(p, 'angle_b', angle_b if 0 < angle_a < 180 and 0 < angle_b < 180 and angle_b+angle_a ==180 else 90)
        print(p.side,  p.angle_a, p.angle_b)
        
        assert side==p.side, f"Bad compare sides: expected:{side}, but real: {p.side} "
        assert angle_a==p.angle_a, f"Bad compare angle_a: expected:{angle_a}, but real: {p.angle_a} "
        assert angle_b==p.angle_b, f"Bad compare angle_b: expected:{angle_b}, but real: {p.angle_b} "
    
    @pytest.mark.parametrize(
            'side, angle_a, angle_b',
            [
                (0, 110, 70),
                (0, 90, 90),
                (0, 0, 70),
                (0, 90, 0),
                (0,0,0),
                (1, 180, 0),
                (2, 0, 180),
                (3, 100, 90),
                (2, 181, 182),
                (4, 90, 30)                

            ],
            ids=[
                'Different angles, side=0',
                'Equal angles, side=0',
                'First angle=0, side=0',
                'Second angle=0, side=0',
                'All angles=0, side=0',
                'First angle=180, second angle=0',
                'First angle=0, second angle=180',
                'Sum of angles > 180, side=0',
                'Each of angles > 180',
                'Sum of angles < 180'
            ],
    )
    def test_neg(self, side, angle_a, angle_b):
        p = Romb()
        expected_site = 1 if side==0 else side
        expected_angle_a = angle_a if 0 < angle_a < 180 and 0 < angle_b < 180 and angle_b+angle_a ==180 else 90
        expected_angle_b = angle_b if 0 < angle_a < 180 and 0 < angle_b < 180 and angle_b+angle_a ==180 else 90


        setattr(p, 'side', 1 if side==0 else side)
        setattr(p, 'angle_a', angle_a if 0 < angle_a < 180 and 0 < angle_b < 180 and angle_b+angle_a ==180 else 90)
        setattr(p, 'angle_b', angle_b if 0 < angle_a < 180 and 0 < angle_b < 180 and angle_b+angle_a ==180 else 90)
        print(p.side,  p.angle_a, p.angle_b)
        
        assert expected_site==p.side, f"Bad compare sides: expected:{expected_site}, but real: {p.side} "
        assert expected_angle_a==p.angle_a, f"Bad compare angle_a: expected:{expected_angle_a}, but real: {p.angle_a} "
        assert expected_angle_b==p.angle_b, f"Bad compare angle_b: expected:{expected_angle_b}, but real: {p.angle_b} "