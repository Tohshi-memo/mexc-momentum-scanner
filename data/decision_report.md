# Decision Report

- generated_at: 2026-10-23T16:36:34.184702+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17253**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17253, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 8/20 | 40.0% | +6.50% | **+2.60%** |
| LIMIT_9PCT | 7/20 | 35.0% | +6.29% | **+2.20%** |
| LIMIT_7PCT | 10/20 | 50.0% | +3.88% | **+1.94%** |
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_6PCT | 12/20 | 60.0% | +1.47% | **+0.88%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +3.37% | **+3.37%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +5.00% | **+3.00%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +3.43% | **+2.92%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.87% | **+2.32%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +5.54% | **+1.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7261件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$299.52** / 初期 $100.00 (+199.52%)
- 確定: 3917件 (Win 1079 / Loss 912 / Flat 1926) / skip 6747件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2615 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $299.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5414件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000614 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T16:36:18.434635+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=81700.0
- Funnel: target 1088 → liquid 171 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.9 >= 65=1, 4h RSI n/a=1, 4h RSI 86.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +35.27% | $42,092,916.69 |
| KIMCHI/USDT:USDT | +8.67% | $1,824,604.73 |
| BIRB/USDT:USDT | +6.47% | $3,030,499.44 |
| BMT/USDT:USDT | +1.32% | $1,043,926.07 |
| SOXS/USDT:USDT | +1.25% | $37,610,900.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BMT/USDT:USDT | below_1h_threshold | +1.33% | +1.27% |
| PENGU/USDT:USDT | below_1h_threshold | +1.03% | +0.97% |
| SYRUP/USDT:USDT | below_1h_threshold | +1.01% | +0.95% |
| CHIP/USDT:USDT | below_1h_threshold | +0.99% | +0.93% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.97% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
