# Decision Report

- generated_at: 2026-05-17T00:43:29.053598+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4373**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.26% / filled 20/20。**
- 全期間 MARKET基準: n=4373, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_1PCT | 14/20 | 70.0% | +0.85% | **+0.59%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.91% | **+0.50%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.87% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.12% | **+0.56%** |
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
- 確定: 392件 (Win 97 / Loss 136 / Flat 159) / skip 542件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-17T00:43:23.331762+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=78139.0
- Funnel: target 760 → liquid 133 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +16.26% | $2,738,434.34 |
| AIA/USDT:USDT | +13.50% | $1,304,170.92 |
| CGPT/USDT:USDT | +13.04% | $1,337,436.70 |
| BSB/USDT:USDT | +11.61% | $3,715,613.56 |
| ASTEROID/USDT:USDT | +11.53% | $4,418,227.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCA/USDT:USDT | below_1h_threshold | +4.81% | +4.76% |
| LYN/USDT:USDT | below_1h_threshold | +3.69% | +3.64% |
| UP/USDT:USDT | below_1h_threshold | +3.28% | +3.23% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.68% | +1.64% |
| MYX/USDT:USDT | below_1h_threshold | +1.54% | +1.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
