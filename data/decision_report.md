# Decision Report

- generated_at: 2026-05-21T12:09:12.920241+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4622**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=4622, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.06% | **+1.01%** |
| LIMIT_BB3S | 7/18 | 38.9% | +2.03% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.13% | **+0.06%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.07% | **+0.03%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.05% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 58件 (TP 15 / SL 40 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 637件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T12:09:10.523518+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=77155.1
- Funnel: target 766 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROVE/USDT:USDT | +42.75% | $5,440,530.01 |
| EDEN/USDT:USDT | +39.09% | $30,684,552.91 |
| PEAQ/USDT:USDT | +33.27% | $1,087,540.32 |
| ROAM/USDT:USDT | +32.59% | $2,250,209.89 |
| FIDA/USDT:USDT | +29.72% | $12,688,922.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.55% | +4.56% |
| FIDA/USDT:USDT | below_1h_threshold | +4.52% | +4.52% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.46% | +4.46% |
| EDEN/USDT:USDT | below_1h_threshold | +2.72% | +2.72% |
| USELESS/USDT:USDT | below_1h_threshold | +0.78% | +0.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
