# Decision Report

- generated_at: 2026-07-03T01:40:54.354892+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8123**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=8123, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +2.21% | **+1.66%** |
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| ASK | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.56% | **+0.45%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.97% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.39% | **+0.48%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.69% | **+0.38%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.25% | **+0.15%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.11% | **+0.04%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.11% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$286.85** / 初期 $100.00 (+186.85%)
- 確定: 2446件 (Win 755 / Loss 816 / Flat 875) / skip 2238件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $286.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.46** / 初期 $100.00 (+5.46%)
- 確定: 578件 (Win 140 / Loss 137 / Flat 301) / skip 956件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.55%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0518 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: O/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.46

## 5. Latest Market Context

- 更新: 2026-07-03T01:40:42.997417+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.65% price=61682.5
- Funnel: target 834 → liquid 170 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| THE/USDT:USDT | +23.70% | $1,968,782.84 |
| GUA/USDT:USDT | +23.41% | $9,894,388.18 |
| PIPPIN/USDT:USDT | +21.31% | $6,848,559.78 |
| MAGMA/USDT:USDT | +13.56% | $5,252,440.44 |
| WLD/USDT:USDT | +13.03% | $61,847,848.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAMSUNGSTOCK/USDT:USDT | below_relative_strength | +5.22% | +4.57% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +4.60% | +3.95% |
| PIPPIN/USDT:USDT | below_1h_threshold | +4.33% | +3.68% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.15% | +2.50% |
| US/USDT:USDT | below_1h_threshold | +2.85% | +2.20% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
