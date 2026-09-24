# Decision Report

- generated_at: 2026-09-24T13:36:25.277842+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15479**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15479, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.03% | **-0.01%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.21% | **-0.14%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.26% | **-0.22%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.50% | **-0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.03% | **+0.77%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.61% | **+0.34%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +1.03% | **+0.31%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.54% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5899件 (Win 1739 / Loss 1890 / Flat 2270) / skip 6141件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$253.81** / 初期 $100.00 (+153.81%)
- 確定: 3426件 (Win 946 / Loss 791 / Flat 1689) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0358 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONDO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $253.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.27** / 初期 $100.00 (+21.27%)
- 確定: 3159件 (Win 932 / Loss 1246 / Flat 981) / pending 0件 / skip 3789件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000221 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.27

## 6. Latest Market Context

- 更新: 2026-09-24T13:36:14.461719+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.51% price=83984.1
- Funnel: target 1069 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +46.34% | $5,262,676.68 |
| LSK/USDT:USDT | +35.23% | $13,781,070.14 |
| NIL/USDT:USDT | +18.68% | $25,229,217.67 |
| ONDO/USDT:USDT | +17.10% | $50,661,195.71 |
| LTC/USDT:USDT | +15.60% | $66,236,585.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MORPHO/USDT:USDT | below_1h_threshold | +4.64% | +4.14% |
| AERO/USDT:USDT | below_1h_threshold | +4.16% | +3.65% |
| PYTH/USDT:USDT | below_1h_threshold | +3.62% | +3.11% |
| ZRO/USDT:USDT | below_1h_threshold | +3.30% | +2.80% |
| ENA/USDT:USDT | below_1h_threshold | +3.20% | +2.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
