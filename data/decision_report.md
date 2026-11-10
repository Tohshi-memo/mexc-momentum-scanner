# Decision Report

- generated_at: 2026-11-10T02:51:29.811733+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18572**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18572, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.38% | **+0.27%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.63% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.76% | **+1.50%** |
| MARKET_LONG | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.55% | **+0.64%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +1.92% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,665.33** / 初期 $100.00 (+1565.33%)
- 確定: 7170件 (Win 2061 / Loss 2286 / Flat 2823) / skip 7963件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $1,665.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$387.85** / 初期 $100.00 (+287.85%)
- 確定: 4758件 (Win 1277 / Loss 1048 / Flat 2433) / skip 7225件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1567 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INIT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $387.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6733件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000383 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T02:51:14.118774+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=74856.4
- Funnel: target 1094 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIUBI/USDT:USDT | +47.05% | $1,859,304.93 |
| INIT/USDT:USDT | +27.55% | $4,231,720.24 |
| CLAUDIA/USDT:USDT | +16.14% | $1,096,794.04 |
| BR/USDT:USDT | +12.59% | $1,996,689.76 |
| ZHIPUSTOCK/USDT:USDT | +12.00% | $1,517,662.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRAM/USDT:USDT | below_1h_threshold | +4.87% | +5.12% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +4.46% | +4.71% |
| DELTAELECSTOCK/USDT:USDT | below_1h_threshold | +3.59% | +3.85% |
| PI/USDT:USDT | below_1h_threshold | +1.46% | +1.72% |
| LEAD/USDT:USDT | below_1h_threshold | +0.82% | +1.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
