# Decision Report

- generated_at: 2026-05-11T17:28:10.274230+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4055**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4055, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.21% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.77% | **+0.83%** |
| ASK_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| MARKET_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.94% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 398件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T17:28:07.372027+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=81554.9
- Funnel: target 762 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +12.33% | $2,260,202.81 |
| USELESS/USDT:USDT | +6.84% | $1,276,894.31 |
| B/USDT:USDT | +5.99% | $27,663,509.02 |
| PENGUIN/USDT:USDT | +4.57% | $2,137,534.56 |
| AKT/USDT:USDT | +4.39% | $3,363,605.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.17% | +3.14% |
| AKT/USDT:USDT | below_1h_threshold | +2.87% | +2.84% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.49% | +2.46% |
| SAGA/USDT:USDT | below_1h_threshold | +2.22% | +2.19% |
| B/USDT:USDT | below_1h_threshold | +2.08% | +2.05% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
