# Decision Report

- generated_at: 2026-05-02T16:17:13.544195+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2949**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2949, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.17% | **+0.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.15% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +2.48% | **+2.11%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +3.02% | **+1.89%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.34% | **+1.75%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.88% | **+1.60%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +3.43% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T16:17:06.545166+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78487.1
- Funnel: target 755 → liquid 162 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.8 >= 65=1, 4h RSI 84.7 >= 65=1, 4h RSI 87.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +15.40% | $180,366,073.09 |
| TAG/USDT:USDT | +11.59% | $11,190,361.91 |
| ORDI/USDT:USDT | +10.41% | $21,530,692.17 |
| PHAROS/USDT:USDT | +7.86% | $1,217,223.48 |
| BASED/USDT:USDT | +5.34% | $1,211,961.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +3.37% | +3.32% |
| TAC/USDT:USDT | below_1h_threshold | +3.28% | +3.23% |
| UB/USDT:USDT | below_1h_threshold | +3.26% | +3.21% |
| XNY/USDT:USDT | below_1h_threshold | +2.89% | +2.84% |
| PNUT/USDT:USDT | below_1h_threshold | +2.11% | +2.06% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
