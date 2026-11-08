# Decision Report

- generated_at: 2026-11-08T06:46:27.542807+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18411**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18411, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_7PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_6PCT | 11/20 | 55.0% | -0.19% | **-0.11%** |
| LIMIT_10PCT | 7/20 | 35.0% | -0.57% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +2.75% | **+2.61%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +3.39% | **+2.55%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.82% | **+2.26%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.40% | **+1.44%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,569.77** / 初期 $100.00 (+1469.77%)
- 確定: 7107件 (Win 2044 / Loss 2269 / Flat 2794) / skip 7865件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $1,569.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4755件 (Win 1277 / Loss 1047 / Flat 2431) / skip 7067件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0268 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6572件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000456 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T06:46:11.526606+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=75748.0
- Funnel: target 1089 → liquid 107 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +220.58% | $8,696,679.68 |
| BTW/USDT:USDT | +5.78% | $6,331,841.84 |
| ARIA/USDT:USDT | +5.24% | $1,776,470.56 |
| AIOT/USDT:USDT | +4.77% | $2,308,583.98 |
| ESPORTS/USDT:USDT | +3.95% | $1,270,312.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARIA/USDT:USDT | below_1h_threshold | +3.06% | +3.13% |
| IDOL/USDT:USDT | below_1h_threshold | +1.91% | +1.98% |
| AIOT/USDT:USDT | below_1h_threshold | +1.24% | +1.31% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.89% | +0.96% |
| MUU/USDT:USDT | below_1h_threshold | +0.87% | +0.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
