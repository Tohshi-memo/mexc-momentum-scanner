# Decision Report

- generated_at: 2026-05-08T16:12:31.873399+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3801**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.97% / filled 20/20。**
- 全期間 MARKET基準: n=3801, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |
| ASK | 20/20 | 100.0% | +1.95% | **+1.95%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.36% | **+0.88%** |
| LIMIT_3PCT | 9/20 | 45.0% | +0.28% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.15% | **+0.46%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.49% | **+0.22%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | -0.04% | **-0.02%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.95% | **-0.19%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.45% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 170件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T16:12:28.846180+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=79955.5
- Funnel: target 772 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +4.06% | $17,431,158.02 |
| M/USDT:USDT | +2.43% | $1,951,634.38 |
| SPORTFUN/USDT:USDT | +2.32% | $1,171,773.35 |
| COLLECT/USDT:USDT | +2.10% | $1,345,761.05 |
| NIL/USDT:USDT | +1.81% | $33,606,987.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.12% | +4.31% |
| M/USDT:USDT | below_1h_threshold | +2.44% | +2.63% |
| COLLECT/USDT:USDT | below_1h_threshold | +2.16% | +2.35% |
| SPORTFUN/USDT:USDT | below_1h_threshold | +2.13% | +2.33% |
| NIL/USDT:USDT | below_1h_threshold | +1.80% | +2.00% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
