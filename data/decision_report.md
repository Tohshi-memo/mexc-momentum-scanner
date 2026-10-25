# Decision Report

- generated_at: 2026-10-25T11:21:20.096505+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17422**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17422, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +1.27% | **+0.70%** |
| LIMIT_BB3S | 3/16 | 18.8% | +3.01% | **+0.56%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.46% | **+0.37%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.11% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.20% | **+1.87%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.36% | **+0.82%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.85% | **+0.77%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.19% | **+0.42%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.97% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,551.00** / 初期 $100.00 (+1451.00%)
- 確定: 6675件 (Win 1942 / Loss 2127 / Flat 2606) / skip 7308件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,551.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$316.02** / 初期 $100.00 (+216.02%)
- 確定: 3965件 (Win 1100 / Loss 931 / Flat 1934) / skip 6868件
- 成長率目線: 平均log +0.000290 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1869 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $316.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5580件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000567 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T11:21:09.819922+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=80386.2
- Funnel: target 1071 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +63.73% | $7,338,329.19 |
| T/USDT:USDT | +35.78% | $7,223,679.14 |
| CAP/USDT:USDT | +30.37% | $1,310,497.95 |
| TAG/USDT:USDT | +18.03% | $1,906,227.06 |
| SKYAI/USDT:USDT | +16.13% | $1,148,402.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +3.79% | +3.61% |
| JCT/USDT:USDT | below_1h_threshold | +3.69% | +3.51% |
| AGT/USDT:USDT | below_1h_threshold | +3.45% | +3.28% |
| CHIP/USDT:USDT | below_1h_threshold | +1.47% | +1.29% |
| PEPE/USDT:USDT | below_1h_threshold | +1.17% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
