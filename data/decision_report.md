# Decision Report

- generated_at: 2026-08-14T09:36:26.624446+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11523**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11523, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 3/12 | 25.0% | +1.06% | **+0.26%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | -0.06% | **-0.01%** |
| LIMIT_ATR | 14/20 | 70.0% | -0.08% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.51% | **+0.46%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.32% | **-0.16%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -1.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$610.26** / 初期 $100.00 (+510.26%)
- 確定: 3991件 (Win 1245 / Loss 1308 / Flat 1438) / skip 4093件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $610.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3283件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1008 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.82** / 初期 $100.00 (+16.82%)
- 確定: 1484件 (Win 441 / Loss 562 / Flat 481) / pending 5件 / skip 1506件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $116.82

## 6. Latest Market Context

- 更新: 2026-08-14T09:36:16.630568+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=62786.7
- Funnel: target 981 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +52.72% | $10,107,040.32 |
| VELVET/USDT:USDT | +31.90% | $29,987,833.40 |
| EDEN/USDT:USDT | +19.08% | $35,570,695.10 |
| AKE/USDT:USDT | +18.80% | $64,044,196.50 |
| WDAYSTOCK/USDT:USDT | +18.58% | $1,631,971.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 2Z/USDT:USDT | below_1h_threshold | +3.50% | +3.68% |
| SNXX/USDT:USDT | below_1h_threshold | +2.98% | +3.17% |
| CAP/USDT:USDT | below_1h_threshold | +2.16% | +2.35% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.65% | +1.84% |
| NIL/USDT:USDT | below_1h_threshold | +1.15% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
