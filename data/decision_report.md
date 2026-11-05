# Decision Report

- generated_at: 2026-11-05T05:46:23.864717+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18160**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18160, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.67% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.33% | **+0.80%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.26% | **+0.70%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.68% | **+0.41%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.49% | **+0.22%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.33% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,508.30** / 初期 $100.00 (+1408.30%)
- 確定: 6979件 (Win 2018 / Loss 2241 / Flat 2720) / skip 7742件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $1,508.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$372.01** / 初期 $100.00 (+272.01%)
- 確定: 4557件 (Win 1223 / Loss 1030 / Flat 2304) / skip 7014件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MVLL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $372.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6321件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000188 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-05T05:46:14.740293+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80425.0
- Funnel: target 1078 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.7 >= 65=1, 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELSA/USDT:USDT | +32.63% | $3,434,380.78 |
| LYN/USDT:USDT | +31.54% | $1,009,458.04 |
| JCT/USDT:USDT | +28.01% | $7,852,595.11 |
| APPSTOCK/USDT:USDT | +20.62% | $1,428,215.46 |
| FLUID/USDT:USDT | +18.80% | $4,638,870.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +2.67% | +2.75% |
| SOXS/USDT:USDT | below_1h_threshold | +0.97% | +1.05% |
| APPSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.83% |
| CC/USDT:USDT | below_1h_threshold | +0.74% | +0.82% |
| AIN/USDT:USDT | below_1h_threshold | +0.73% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
