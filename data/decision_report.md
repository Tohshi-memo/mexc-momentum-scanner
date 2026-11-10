# Decision Report

- generated_at: 2026-11-10T15:37:13.345381+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18609**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18609, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.27% | **+0.91%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +3.33% | **+1.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.24% | **+0.87%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.96% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,682.80** / 初期 $100.00 (+1582.80%)
- 確定: 7206件 (Win 2073 / Loss 2302 / Flat 2831) / skip 7964件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CBRSSTOCK/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,682.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$394.41** / 初期 $100.00 (+294.41%)
- 確定: 4775件 (Win 1283 / Loss 1054 / Flat 2438) / skip 7245件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0540 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CBRSSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $394.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6782件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000243 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T15:36:44.783429+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.11% price=73550.8
- Funnel: target 1099 → liquid 149 → pre 50 → checked 50 → surge 10 → strict 8
- Surge前reject: below_1h_threshold=40, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.4 >= 65=1, 4h RSI 69.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +91.29% | $28,211,406.95 |
| ARIA/USDT:USDT | +19.07% | $2,734,014.01 |
| ONE/USDT:USDT | +16.07% | $9,873,904.25 |
| BR/USDT:USDT | +11.35% | $3,823,276.77 |
| ZHIPUSTOCK/USDT:USDT | +11.09% | $1,638,548.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.92% | +6.02% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +4.68% | +5.78% |
| TQQQ/USDT:USDT | below_1h_threshold | +3.95% | +5.05% |
| SNOWSTOCK/USDT:USDT | below_1h_threshold | +3.76% | +4.87% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +3.36% | +4.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
