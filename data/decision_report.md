# Decision Report

- generated_at: 2026-08-30T04:46:25.190414+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13014**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13014, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.75% | **-1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.09% | **+0.63%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.50% | **+0.40%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +4.54% | **+2.95%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.70% | **+2.59%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +4.81% | **+2.40%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.32% | **+2.16%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.80% | **+1.53%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.09** / 初期 $100.00 (+692.09%)
- 確定: 4784件 (Win 1460 / Loss 1575 / Flat 1749) / skip 4791件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $792.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.58** / 初期 $100.00 (+72.58%)
- 確定: 2098件 (Win 587 / Loss 512 / Flat 999) / skip 4327件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0666 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $172.58

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.93** / 初期 $100.00 (+16.93%)
- 確定: 2058件 (Win 606 / Loss 800 / Flat 652) / pending 4件 / skip 2424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000370 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $116.93

## 6. Latest Market Context

- 更新: 2026-08-30T04:46:15.251637+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=77975.9
- Funnel: target 1023 → liquid 118 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 88.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +62.70% | $2,417,324.65 |
| FONE/USDT:USDT | +60.47% | $1,338,999.65 |
| HNT/USDT:USDT | +52.57% | $28,953,133.44 |
| PONS/USDT:USDT | +43.32% | $1,508,341.47 |
| PROM/USDT:USDT | +30.15% | $14,361,473.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MOVR/USDT:USDT | below_1h_threshold | +3.45% | +3.62% |
| 4/USDT:USDT | below_1h_threshold | +3.42% | +3.58% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.80% | +1.96% |
| BICO/USDT:USDT | below_1h_threshold | +1.66% | +1.82% |
| VET/USDT:USDT | below_1h_threshold | +1.46% | +1.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
