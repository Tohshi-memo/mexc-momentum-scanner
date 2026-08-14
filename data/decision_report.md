# Decision Report

- generated_at: 2026-08-14T19:36:32.889131+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11599**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11599, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +2.56% | **+0.90%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.19% | **+0.88%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.95% | **+0.81%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.01% | **+2.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +4.20% | **+1.68%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.40% | **+1.32%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +4.80% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$638.60** / 初期 $100.00 (+538.60%)
- 確定: 4067件 (Win 1276 / Loss 1339 / Flat 1452) / skip 4093件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $638.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$151.92** / 初期 $100.00 (+51.92%)
- 確定: 1665件 (Win 478 / Loss 404 / Flat 783) / skip 3345件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0293 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $151.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.00** / 初期 $100.00 (+17.00%)
- 確定: 1549件 (Win 470 / Loss 594 / Flat 485) / pending 6件 / skip 1519件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000159 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.00

## 6. Latest Market Context

- 更新: 2026-08-14T19:36:19.526294+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=62894.3
- Funnel: target 985 → liquid 175 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +22.99% | $6,899,853.55 |
| DOLO/USDT:USDT | +22.91% | $1,328,119.95 |
| ACE/USDT:USDT | +12.46% | $58,715,172.45 |
| ACU/USDT:USDT | +7.09% | $2,227,105.98 |
| VELVET/USDT:USDT | +6.01% | $41,406,098.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +4.42% | +4.43% |
| CYS/USDT:USDT | below_1h_threshold | +2.87% | +2.88% |
| DOLO/USDT:USDT | below_1h_threshold | +2.31% | +2.32% |
| BANK/USDT:USDT | below_1h_threshold | +1.69% | +1.70% |
| EDEN/USDT:USDT | below_1h_threshold | +1.46% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
