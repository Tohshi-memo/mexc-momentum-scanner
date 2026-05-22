# Decision Report

- generated_at: 2026-05-22T15:54:36.590632+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4715**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4715, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.76% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.47% | **+0.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.43% | **+0.28%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.89% | **+0.22%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.66** / 初期 $100.00 (+21.66%)
- 確定: 564件 (Win 144 / Loss 186 / Flat 234) / skip 712件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BUILDONBOB/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $121.66

## 4. Latest Market Context

- 更新: 2026-05-22T15:54:28.498867+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=76744.8
- Funnel: target 768 → liquid 141 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +57.92% | $5,282,749.82 |
| BEAT/USDT:USDT | +42.18% | $29,002,888.00 |
| GENIUS/USDT:USDT | +41.19% | $4,448,604.53 |
| ALT/USDT:USDT | +28.92% | $3,447,229.83 |
| AGT/USDT:USDT | +23.86% | $1,045,828.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.10% | +3.09% |
| PLUME/USDT:USDT | below_1h_threshold | +2.82% | +2.81% |
| FET/USDT:USDT | below_1h_threshold | +1.93% | +1.92% |
| APE/USDT:USDT | below_1h_threshold | +1.72% | +1.70% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.69% | +1.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
