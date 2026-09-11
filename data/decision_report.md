# Decision Report

- generated_at: 2026-09-11T19:26:32.198823+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14249**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14249, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.11% | **+0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.01% | **+0.35%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.00% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.11% | **+0.11%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.88% | **+3.92%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.35% | **+1.22%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.29% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.77% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,112.33** / 初期 $100.00 (+1012.33%)
- 確定: 5406件 (Win 1631 / Loss 1749 / Flat 2026) / skip 5404件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,112.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.99** / 初期 $100.00 (+109.99%)
- 確定: 2821件 (Win 776 / Loss 655 / Flat 1390) / skip 4839件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0039 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $209.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.12** / 初期 $100.00 (+24.12%)
- 確定: 2741件 (Win 812 / Loss 1050 / Flat 879) / pending 5件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000304 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $124.12

## 6. Latest Market Context

- 更新: 2026-09-11T19:26:19.601922+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=77224.1
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +41.30% | $8,992,945.28 |
| LAB/USDT:USDT | +21.59% | $7,383,054.95 |
| BEAT/USDT:USDT | +12.50% | $9,281,664.35 |
| RIVER/USDT:USDT | +6.27% | $3,530,524.11 |
| MET/USDT:USDT | +3.47% | $1,853,386.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HPQSTOCK/USDT:USDT | below_1h_threshold | +2.08% | +1.81% |
| EGLD/USDT:USDT | below_1h_threshold | +1.95% | +1.69% |
| RUNE/USDT:USDT | below_1h_threshold | +1.14% | +0.88% |
| POL/USDT:USDT | below_1h_threshold | +1.08% | +0.82% |
| GPS/USDT:USDT | below_1h_threshold | +1.07% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
