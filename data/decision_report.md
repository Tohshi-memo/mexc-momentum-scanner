# Decision Report

- generated_at: 2026-09-08T10:21:19.757021+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13980**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.09% / filled 20/20。**
- 全期間 MARKET基準: n=13980, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.41% | **+0.35%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.94% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.34% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,022.29** / 初期 $100.00 (+922.29%)
- 確定: 5247件 (Win 1584 / Loss 1704 / Flat 1959) / skip 5294件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.58% 残高後 $1,022.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.10** / 初期 $100.00 (+89.10%)
- 確定: 2584件 (Win 720 / Loss 621 / Flat 1243) / skip 4807件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0670 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $189.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.09** / 初期 $100.00 (+22.09%)
- 確定: 2569件 (Win 755 / Loss 964 / Flat 850) / pending 3件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000255 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $122.09

## 6. Latest Market Context

- 更新: 2026-09-08T10:21:09.746461+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=78949.8
- Funnel: target 1065 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +118.68% | $16,716,105.85 |
| BNCSTOCK/USDT:USDT | +52.18% | $1,628,183.59 |
| FORM/USDT:USDT | +27.99% | $3,829,132.76 |
| USELESS/USDT:USDT | +17.75% | $11,773,538.18 |
| MEMEROBINHOOD/USDT:USDT | +15.56% | $5,921,647.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +4.21% | +3.93% |
| BTR/USDT:USDT | below_1h_threshold | +2.35% | +2.07% |
| XPL/USDT:USDT | below_1h_threshold | +1.81% | +1.53% |
| SOFTBANKSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +0.91% |
| SEI/USDT:USDT | below_1h_threshold | +1.18% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
