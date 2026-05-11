# Decision Report

- generated_at: 2026-05-11T14:02:55.970744+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4035**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4035, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.79% | **+0.72%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_2PCT | 18/20 | 90.0% | -0.09% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.16% | **+0.75%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.32% | **+0.59%** |
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 378件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T14:02:52.751008+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=81122.4
- Funnel: target 762 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +39.74% | $4,404,745.75 |
| US/USDT:USDT | +36.97% | $14,476,481.84 |
| PENGUIN/USDT:USDT | +28.77% | $1,749,728.25 |
| SAGA/USDT:USDT | +26.00% | $3,688,276.92 |
| B/USDT:USDT | +19.59% | $13,166,500.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STXSTOCK/USDT:USDT | below_1h_threshold | +0.73% | +0.62% |
| ONDO/USDT:USDT | below_1h_threshold | +0.73% | +0.62% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.70% | +0.59% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +0.70% | +0.59% |
| BANANAS31/USDT:USDT | below_1h_threshold | +0.69% | +0.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
