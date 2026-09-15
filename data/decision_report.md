# Decision Report

- generated_at: 2026-09-15T06:41:18.678114+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14573**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14573, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.16% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.29% | **+1.98%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.25% | **+1.49%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.88% | **+1.22%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,078.22** / 初期 $100.00 (+978.22%)
- 確定: 5475件 (Win 1642 / Loss 1773 / Flat 2060) / skip 5659件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,078.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.20** / 初期 $100.00 (+130.20%)
- 確定: 3014件 (Win 835 / Loss 718 / Flat 1461) / skip 4970件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0694 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.98** / 初期 $100.00 (+23.98%)
- 確定: 2908件 (Win 862 / Loss 1133 / Flat 913) / pending 1件 / skip 3137件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.98

## 6. Latest Market Context

- 更新: 2026-09-15T06:41:06.669728+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=77373.9
- Funnel: target 1075 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +52.00% | $9,426,811.92 |
| SHROOM/USDT:USDT | +49.43% | $1,574,080.21 |
| POWER/USDT:USDT | +44.49% | $9,705,946.64 |
| FF/USDT:USDT | +26.42% | $1,242,447.50 |
| STORJ/USDT:USDT | +18.19% | $1,075,881.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +3.59% | +3.87% |
| AIN/USDT:USDT | below_1h_threshold | +1.93% | +2.21% |
| RIVER/USDT:USDT | below_1h_threshold | +0.82% | +1.10% |
| MUU/USDT:USDT | below_1h_threshold | +0.60% | +0.88% |
| CRV/USDT:USDT | below_1h_threshold | +0.37% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
