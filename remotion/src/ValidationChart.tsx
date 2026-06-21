import {AbsoluteFill, Img, staticFile} from 'remotion';
import {loadFont as loadInter} from '@remotion/google-fonts/Inter';

const {fontFamily: INTER} = loadInter();

const C = {
  bg: '#2A7A6D',
  ink: '#FFFFFF',
  sub: 'rgba(255,255,255,0.85)',
  accent: '#CFEFE7',
  line: 'rgba(255,255,255,0.24)',
  card: 'rgba(255,255,255,0.10)',
};

const Texture: React.FC = () => (
  <AbsoluteFill
    style={{
      opacity: 0.06,
      mixBlendMode: 'soft-light',
      backgroundImage: `radial-gradient(circle at 15% 25%, #fff 0.5px, transparent 1.5px)`,
      backgroundSize: '6px 6px',
      pointerEvents: 'none',
    }}
  />
);

const Step: React.FC<{n: string; title: string; detail: string}> = ({n, title, detail}) => (
  <div
    style={{
      flex: 1,
      background: C.card,
      border: `2px solid ${C.line}`,
      borderRadius: 24,
      padding: '40px 24px',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      textAlign: 'center',
      gap: 12,
    }}
  >
    <div
      style={{
        width: 66,
        height: 66,
        borderRadius: 33,
        background: C.accent,
        color: C.bg,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: INTER,
        fontWeight: 800,
        fontSize: 34,
      }}
    >
      {n}
    </div>
    <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 33, color: C.ink, lineHeight: 1.05, marginTop: 6}}>{title}</div>
    <div style={{fontFamily: INTER, fontWeight: 600, fontSize: 25, color: C.accent}}>{detail}</div>
  </div>
);

const Chevron: React.FC = () => (
  <div style={{display: 'flex', alignItems: 'center', color: C.accent, fontFamily: INTER, fontWeight: 800, fontSize: 52, flexShrink: 0}}>›</div>
);

export const ValidationChart: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: C.bg, fontFamily: INTER}}>
    <Texture />
    <AbsoluteFill style={{padding: 96, display: 'flex', flexDirection: 'column'}}>
      <div>
        <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 26, letterSpacing: '0.18em', textTransform: 'uppercase', color: C.accent}}>The order that saves you 6 months</div>
        <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 86, color: C.ink, lineHeight: 1.0, letterSpacing: '-0.02em', marginTop: 12}}>
          Validate before you build
        </div>
      </div>

      <div style={{flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: 40}}>
        <div style={{display: 'flex', alignItems: 'stretch', gap: 16}}>
          <Step n="1" title="Name who hurts" detail="your exact ICP" />
          <Chevron />
          <Step n="2" title="One-page site" detail="Carrd, under 2h" />
          <Chevron />
          <Step n="3" title="Drive traffic" detail="200-300 visitors" />
          <Chevron />
          <Step n="4" title="5 customer calls" detail="in one week" />
          <Chevron />
          <Step n="5" title="First dollar" detail="now build it" />
        </div>

        <div
          style={{
            background: 'rgba(255,255,255,0.06)',
            border: `2px solid ${C.line}`,
            borderRadius: 20,
            padding: '24px 34px',
            fontFamily: INTER,
            fontWeight: 500,
            fontSize: 30,
            color: C.sub,
          }}
        >
          <span style={{color: C.accent, fontWeight: 700}}>On the calls, ask only three things: </span>
          What are they replacing? · What would make them cancel? · What would they pay more for?
        </div>
      </div>

      <div style={{paddingTop: 28, borderTop: `2px solid ${C.line}`, display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
        <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 32, color: C.ink}}>
          A stranger paying before the product exists is the only validation that never lies.
        </div>
        <div style={{display: 'flex', alignItems: 'center', gap: 14, opacity: 0.9}}>
          <Img src={staticFile('logo-b.png')} style={{height: 42, width: 'auto'}} />
          <div style={{fontFamily: INTER, fontWeight: 600, fontSize: 26, color: C.sub}}>@thebillionperson</div>
        </div>
      </div>
    </AbsoluteFill>
  </AbsoluteFill>
);
