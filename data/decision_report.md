# Decision Report

- generated_at: 2026-05-17T00:23:33.906736+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4372**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=4372, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| ASK | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.74% | **+0.44%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.52% | **+0.39%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.70% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.12% | **+0.56%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.98% | **+0.54%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +1.37% | **+0.41%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.09% | **+0.38%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 392件 (Win 97 / Loss 136 / Flat 159) / skip 541件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-17T00:23:27.705642+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78131.2
- Funnel: target 760 → liquid 132 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +16.66% | $2,441,307.87 |
| BSB/USDT:USDT | +12.12% | $3,673,531.47 |
| AIA/USDT:USDT | +11.46% | $1,254,429.98 |
| ASTEROID/USDT:USDT | +10.49% | $4,358,799.81 |
| CGPT/USDT:USDT | +9.43% | $1,290,255.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LYN/USDT:USDT | below_1h_threshold | +3.94% | +3.90% |
| MYX/USDT:USDT | below_1h_threshold | +1.96% | +1.92% |
| CGPT/USDT:USDT | below_1h_threshold | +1.96% | +1.92% |
| SAGA/USDT:USDT | below_1h_threshold | +1.45% | +1.42% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.02% | +0.99% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
