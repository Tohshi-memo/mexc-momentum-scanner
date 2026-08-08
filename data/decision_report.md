# Decision Report

- generated_at: 2026-08-08T15:06:24.653847+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10856**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10856, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.06% | **-2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.45% | **+2.33%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +4.40% | **+2.20%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.88% | **+1.59%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.50% | **+1.57%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.74% | **+1.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$634.29** / 初期 $100.00 (+534.29%)
- 確定: 3857件 (Win 1213 / Loss 1253 / Flat 1391) / skip 3560件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $634.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2757件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0806 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.83** / 初期 $100.00 (+18.83%)
- 確定: 1224件 (Win 386 / Loss 469 / Flat 369) / pending 5件 / skip 1099件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000258 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $118.83

## 6. Latest Market Context

- 更新: 2026-08-08T15:06:15.210752+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=65084.2
- Funnel: target 961 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +248.69% | $11,867,268.13 |
| TUT/USDT:USDT | +92.09% | $11,232,887.83 |
| BEAT/USDT:USDT | +39.43% | $31,510,942.14 |
| BLUAI/USDT:USDT | +38.05% | $4,518,920.59 |
| MMT/USDT:USDT | +23.16% | $7,062,656.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.19% | +4.21% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +4.14% | +4.17% |
| ACE/USDT:USDT | below_1h_threshold | +4.02% | +4.04% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.53% | +1.56% |
| RAVE/USDT:USDT | below_1h_threshold | +1.01% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
