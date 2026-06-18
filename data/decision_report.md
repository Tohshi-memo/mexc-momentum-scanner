# Decision Report

- generated_at: 2026-06-18T07:06:38.041275+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7016**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.39% / filled 20/20。**
- 全期間 MARKET基準: n=7016, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |
| ASK | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.45% | **+0.23%** |
| LIMIT_6PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.02% | **+0.01%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | -0.04% | **-0.03%** |
| ASK_LONG | 20/20 | 100.0% | -0.10% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$212.94** / 初期 $100.00 (+112.94%)
- 確定: 1862件 (Win 520 / Loss 591 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $212.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.43** / 初期 $100.00 (+5.43%)
- 確定: 289件 (Win 81 / Loss 77 / Flat 131) / skip 138件
- 成長率目線: 平均log +0.000183 / 幾何平均 +0.018% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0586 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.43

## 5. Latest Market Context

- 更新: 2026-06-18T07:06:33.788010+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64030.0
- Funnel: target 793 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +109.98% | $38,917,762.70 |
| O/USDT:USDT | +80.31% | $3,089,503.37 |
| SYN/USDT:USDT | +56.59% | $5,196,304.96 |
| H/USDT:USDT | +35.38% | $31,274,552.99 |
| HOME/USDT:USDT | +28.74% | $2,025,749.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +1.71% | +1.74% |
| H/USDT:USDT | below_1h_threshold | +1.49% | +1.52% |
| PLAY/USDT:USDT | below_1h_threshold | +1.41% | +1.44% |
| HOME/USDT:USDT | below_1h_threshold | +1.11% | +1.14% |
| EVAA/USDT:USDT | below_1h_threshold | +1.01% | +1.05% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
