# Decision Report

- generated_at: 2026-05-02T16:47:14.095300+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2959**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2959, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.89% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.27% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.98% | **+0.59%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.66% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T16:47:06.770974+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78396.8
- Funnel: target 755 → liquid 164 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.3 >= 65=1, 4h RSI 96.9 >= 65=1, 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +28.50% | $13,062,562.45 |
| LAB/USDT:USDT | +18.00% | $195,555,697.52 |
| TAC/USDT:USDT | +10.30% | $2,495,363.22 |
| XNY/USDT:USDT | +6.81% | $1,232,276.10 |
| BASED/USDT:USDT | +5.53% | $1,298,396.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORDI/USDT:USDT | below_1h_threshold | +4.35% | +4.42% |
| ALCH/USDT:USDT | below_1h_threshold | +3.56% | +3.63% |
| PLAY/USDT:USDT | below_1h_threshold | +3.50% | +3.57% |
| PNUT/USDT:USDT | below_1h_threshold | +3.19% | +3.26% |
| BEAT/USDT:USDT | below_1h_threshold | +2.89% | +2.96% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
