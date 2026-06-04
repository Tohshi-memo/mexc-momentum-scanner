# Decision Report

- generated_at: 2026-06-04T08:30:54.959935+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5614**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=5614, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.75% | **+2.75%** |
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.01% | **+0.75%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.19% | **+0.11%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.73% | **+0.40%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.82% | **+0.16%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.25% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1006件 (Win 239 / Loss 312 / Flat 455) / skip 1169件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T08:30:52.669755+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63583.9
- Funnel: target 771 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +39.70% | $3,686,367.35 |
| OPN/USDT:USDT | +25.22% | $31,559,959.07 |
| SIREN/USDT:USDT | +21.82% | $4,077,401.11 |
| EPIC/USDT:USDT | +18.81% | $5,131,833.04 |
| HNT/USDT:USDT | +15.37% | $1,149,915.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +4.86% | +4.82% |
| OPN/USDT:USDT | below_1h_threshold | +3.56% | +3.53% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.98% | +2.94% |
| ZORA/USDT:USDT | below_1h_threshold | +2.36% | +2.33% |
| HEI/USDT:USDT | below_1h_threshold | +1.74% | +1.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
