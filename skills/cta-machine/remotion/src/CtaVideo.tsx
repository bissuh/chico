import {AbsoluteFill, Img, useCurrentFrame, useVideoConfig, spring, interpolate, staticFile} from 'remotion';
import {loadFont as loadAnton} from '@remotion/google-fonts/Anton';
import {loadFont as loadPlayfair} from '@remotion/google-fonts/PlayfairDisplay';

const {fontFamily: ANTON} = loadAnton();
const {fontFamily: PLAYFAIR} = loadPlayfair('normal', {weights: ['900'], subsets: ['latin']});

export type CtaProps = {
  headline1: string;       // alarm line, e.g. "STOP SCROLLING."
  headline2: string;       // action line, e.g. "START BUILDING."
  subhead: string;         // social proof + offer, one sentence
  url: string;             // your single destination, e.g. "yourdomain.com"
  brandColor?: string;     // hex accent, multiplied over backgrounds. Default neutral slate.
  bg1?: string;            // scene 1 background (file in public/ or an https URL)
  bg2?: string;            // scene 2 background
  bg3?: string;            // scene 3 background
};

const SANS = '"Helvetica Neue", Helvetica, Arial, sans-serif';
const DEFAULT_BRAND = '#2A4A52';

// Slightly darker shade of the brand color for the fallback gradient.
const darken = (hex: string) => {
  const n = parseInt(hex.replace('#', ''), 16);
  if (Number.isNaN(n)) return hex;
  const r = Math.max(0, ((n >> 16) & 255) - 28);
  const g = Math.max(0, ((n >> 8) & 255) - 28);
  const b = Math.max(0, (n & 255) - 28);
  return `rgb(${r}, ${g}, ${b})`;
};

const SCENE_1_LEN = 36;
const SCENE_2_LEN = 42;
const SCENE_3_LEN = 108;
const FADE = 8;

const SCENE_1_END = SCENE_1_LEN;
const SCENE_2_START = SCENE_1_END - FADE;
const SCENE_2_END = SCENE_2_START + SCENE_2_LEN;
const SCENE_3_START = SCENE_2_END - FADE;
const SCENE_3_END = SCENE_3_START + SCENE_3_LEN;

const KenBurns: React.FC<{
  src?: string;
  brand: string;
  localFrame: number;
  duration: number;
  panX: number;
  panY: number;
}> = ({src, brand, localFrame, duration, panX, panY}) => {
  const t = Math.max(0, Math.min(1, localFrame / duration));
  const scale = 1.02 + 0.05 * t;
  const tx = panX * t;
  const ty = panY * t;

  if (!src) {
    return (
      <AbsoluteFill style={{background: `linear-gradient(180deg, ${brand} 0%, ${darken(brand)} 100%)`}} />
    );
  }

  return (
    <AbsoluteFill style={{overflow: 'hidden'}}>
      <Img
        src={src}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          transform: `scale(${scale}) translate(${tx}px, ${ty}px)`,
          transformOrigin: 'center center',
        }}
      />
      <AbsoluteFill
        style={{backgroundColor: brand, mixBlendMode: 'multiply', opacity: 0.6}}
      />
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(ellipse at center, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.22) 60%, rgba(0,0,0,0) 100%)',
        }}
      />
    </AbsoluteFill>
  );
};

const Vignette: React.FC = () => (
  <AbsoluteFill
    style={{
      background: 'radial-gradient(circle at center, transparent 55%, rgba(0,0,0,0.32) 100%)',
      pointerEvents: 'none',
    }}
  />
);

const Grain: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill
      style={{
        opacity: 0.05,
        mixBlendMode: 'overlay',
        backgroundImage: `radial-gradient(circle at ${20 + (frame % 30)}% ${30 + (frame % 25)}%, white 1px, transparent 2px)`,
        backgroundSize: '6px 6px',
        pointerEvents: 'none',
      }}
    />
  );
};

const headlineStyle = (size: number, struck: number) => ({
  fontFamily: ANTON,
  fontWeight: 400,
  fontSize: size,
  color: 'white',
  textAlign: 'center' as const,
  lineHeight: 0.95,
  letterSpacing: '0.005em',
  textTransform: 'uppercase' as const,
  textShadow: '0 6px 30px rgba(0,0,0,0.6), 0 2px 8px rgba(0,0,0,0.85)',
  position: 'relative' as const,
  display: 'inline-block' as const,
  opacity: 1 - struck * 0.45,
});

const Scene1: React.FC<{text: string; localFrame: number}> = ({text, localFrame}) => {
  const {fps} = useVideoConfig();
  const enterSpring = spring({frame: localFrame, fps, config: {damping: 9, stiffness: 180, mass: 0.5}});
  const scale = interpolate(enterSpring, [0, 1], [0.6, 1]);
  const opacity = interpolate(localFrame, [0, 5], [0, 1], {extrapolateRight: 'clamp'});
  const lift = interpolate(localFrame, [0, 12], [50, 0], {extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', padding: '0 80px'}}>
      <div style={{transform: `scale(${scale}) translateY(${lift}px)`, opacity}}>
        <div style={headlineStyle(180, 0)}>{text}</div>
      </div>
    </AbsoluteFill>
  );
};

const Scene2Checklist: React.FC<{
  text1: string;
  text2: string;
  localFrame: number;
}> = ({text1, text2, localFrame}) => {
  const {fps} = useVideoConfig();

  const stop1Settle = interpolate(localFrame, [0, 14], [1, 0.62], {extrapolateRight: 'clamp'});
  const stop1Lift = interpolate(localFrame, [0, 14], [0, -110], {extrapolateRight: 'clamp'});

  const strikeAlpha = interpolate(localFrame, [6, 22], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const startEnter = spring({
    frame: Math.max(0, localFrame - 8),
    fps,
    config: {damping: 12, stiffness: 130, mass: 0.55},
  });
  const startScale = interpolate(startEnter, [0, 1], [0.5, 1]);
  const startOpacity = interpolate(localFrame, [8, 18], [0, 1], {extrapolateRight: 'clamp'});
  const startLift = interpolate(localFrame, [8, 22], [60, 0], {extrapolateRight: 'clamp'});

  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', padding: '0 80px'}}>
      <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 50}}>
        <div
          style={{
            transform: `scale(${stop1Settle}) translateY(${stop1Lift}px)`,
            transformOrigin: 'center',
          }}
        >
          <div
            style={{
              ...headlineStyle(180, strikeAlpha),
              textDecoration: 'line-through',
              textDecorationColor: `rgba(255, 255, 255, ${strikeAlpha})`,
              textDecorationThickness: '14px',
              textDecorationSkipInk: 'none' as const,
            }}
          >
            {text1}
          </div>
        </div>

        <div
          style={{
            transform: `scale(${startScale}) translateY(${startLift}px)`,
            opacity: startOpacity,
          }}
        >
          <div style={headlineStyle(180, 0)}>{text2}</div>
        </div>
      </div>
    </AbsoluteFill>
  );
};

const Scene3Url: React.FC<{subhead: string; url: string; localFrame: number}> = ({
  subhead,
  url,
  localFrame,
}) => {
  const {fps} = useVideoConfig();

  const subSpring = spring({frame: localFrame, fps, config: {damping: 14, stiffness: 100, mass: 0.6}});
  const subY = interpolate(subSpring, [0, 1], [60, 0]);
  const subOpacity = interpolate(localFrame, [0, 12], [0, 1], {extrapolateRight: 'clamp'});

  const urlSpring = spring({
    frame: Math.max(0, localFrame - 14),
    fps,
    config: {damping: 11, stiffness: 130, mass: 0.6},
  });
  const urlScale = interpolate(urlSpring, [0, 1], [0.65, 1]);
  const urlOpacity = interpolate(localFrame, [14, 26], [0, 1], {extrapolateRight: 'clamp'});

  const pulse = 1 + Math.sin((localFrame - 24) / 8) * 0.018;

  return (
    <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center', padding: '0 80px'}}>
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 600,
          fontSize: 70,
          color: 'rgba(255,255,255,0.95)',
          textAlign: 'center',
          lineHeight: 1.15,
          letterSpacing: '-0.01em',
          marginBottom: 90,
          transform: `translateY(${subY}px)`,
          opacity: subOpacity,
          maxWidth: 920,
          textShadow: '0 4px 20px rgba(0,0,0,0.7)',
        }}
      >
        {subhead}
      </div>
      <div
        style={{
          fontFamily: PLAYFAIR,
          fontWeight: 900,
          fontStyle: 'italic',
          fontSize: 102,
          color: 'white',
          letterSpacing: '-0.02em',
          transform: `scale(${urlScale * pulse})`,
          opacity: urlOpacity,
          textShadow: '0 8px 36px rgba(0,0,0,0.75)',
        }}
      >
        {url}
      </div>
    </AbsoluteFill>
  );
};

const PersistentUrl: React.FC<{url: string}> = ({url}) => {
  const frame = useCurrentFrame();
  const fadeIn = interpolate(frame, [4, 14], [0, 1], {extrapolateRight: 'clamp'});
  const fadeOut = interpolate(
    frame,
    [SCENE_3_START - 4, SCENE_3_START + 6],
    [1, 0],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
  );
  const opacity = fadeIn * fadeOut * 0.95;
  if (opacity <= 0) return null;

  return (
    <AbsoluteFill
      style={{
        justifyContent: 'flex-start',
        alignItems: 'center',
        paddingTop: 110,
        pointerEvents: 'none',
      }}
    >
      <div
        style={{
          opacity,
          fontFamily: SANS,
          fontWeight: 700,
          fontSize: 40,
          color: 'white',
          letterSpacing: '0.02em',
          textShadow: '0 3px 14px rgba(0,0,0,0.7), 0 1px 3px rgba(0,0,0,0.9)',
          textAlign: 'center',
          padding: '10px 28px',
          borderRadius: 999,
          background: 'rgba(0,0,0,0.32)',
        }}
      >
        ↳ {url}
      </div>
    </AbsoluteFill>
  );
};

const resolveSrc = (raw?: string) => {
  if (!raw) return undefined;
  if (raw.startsWith('http://') || raw.startsWith('https://')) return raw;
  return staticFile(raw);
};

const sceneOpacity = (frame: number, start: number, end: number) =>
  interpolate(
    frame,
    [start, start + FADE, end - FADE, end],
    [0, 1, 1, 0],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
  );

export const CtaVideo: React.FC<CtaProps> = ({headline1, headline2, subhead, url, brandColor, bg1, bg2, bg3}) => {
  const frame = useCurrentFrame();
  const brand = brandColor || DEFAULT_BRAND;
  const src1 = resolveSrc(bg1);
  const src2 = resolveSrc(bg2);
  const src3 = resolveSrc(bg3);

  const op1 = interpolate(frame, [0, 4, SCENE_1_END - FADE, SCENE_1_END], [1, 1, 1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const op2 = sceneOpacity(frame, SCENE_2_START, SCENE_2_END);
  const op3 = interpolate(frame, [SCENE_3_START, SCENE_3_START + FADE, SCENE_3_END], [0, 1, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      {op1 > 0 && (
        <AbsoluteFill style={{opacity: op1}}>
          <KenBurns src={src1} brand={brand} localFrame={frame} duration={SCENE_1_LEN} panX={-8} panY={-4} />
          <Scene1 text={headline1} localFrame={frame} />
        </AbsoluteFill>
      )}

      {op2 > 0 && (
        <AbsoluteFill style={{opacity: op2}}>
          <KenBurns
            src={src2}
            brand={brand}
            localFrame={frame - SCENE_2_START}
            duration={SCENE_2_LEN}
            panX={6}
            panY={3}
          />
          <Scene2Checklist
            text1={headline1}
            text2={headline2}
            localFrame={frame - SCENE_2_START}
          />
        </AbsoluteFill>
      )}

      {op3 > 0 && (
        <AbsoluteFill style={{opacity: op3}}>
          <KenBurns
            src={src3}
            brand={brand}
            localFrame={frame - SCENE_3_START}
            duration={SCENE_3_LEN}
            panX={0}
            panY={-6}
          />
          <Scene3Url
            subhead={subhead}
            url={url}
            localFrame={frame - SCENE_3_START}
          />
        </AbsoluteFill>
      )}

      <PersistentUrl url={url} />

      <Grain />
      <Vignette />
    </AbsoluteFill>
  );
};
