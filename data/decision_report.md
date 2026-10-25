# Decision Report

- generated_at: 2026-10-25T04:56:15.335899+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17402**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17402, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.81% | **-0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.12% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.56% | **+2.05%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.77% | **+1.25%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.74% | **+1.23%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,480.93** / 初期 $100.00 (+1380.93%)
- 確定: 6655件 (Win 1932 / Loss 2120 / Flat 2603) / skip 7308件
- 成長率目線: 平均log +0.000405 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIGHT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,480.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$306.33** / 初期 $100.00 (+206.33%)
- 確定: 3945件 (Win 1090 / Loss 924 / Flat 1931) / skip 6868件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2030 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LIGHT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $306.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5563件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000631 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T04:56:04.214420+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=80918.3
- Funnel: target 1079 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.7 >= 65=1, 4h RSI 73.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +65.71% | $2,690,654.33 |
| T/USDT:USDT | +36.60% | $2,912,833.71 |
| USELESS/USDT:USDT | +19.90% | $3,998,157.19 |
| AGT/USDT:USDT | +17.39% | $5,777,729.68 |
| LIGHT/USDT:USDT | +15.39% | $1,317,962.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.69% | +3.57% |
| GRASS/USDT:USDT | below_1h_threshold | +2.47% | +2.36% |
| SNXX/USDT:USDT | below_1h_threshold | +1.10% | +0.98% |
| MUU/USDT:USDT | below_1h_threshold | +0.81% | +0.70% |
| SPX/USDT:USDT | below_1h_threshold | +0.78% | +0.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
