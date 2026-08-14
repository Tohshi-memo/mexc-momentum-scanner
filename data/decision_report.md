# Decision Report

- generated_at: 2026-08-14T23:11:25.458206+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11617**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11617, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.48% | **+0.99%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.42% | **+0.40%** |
| LIMIT_BB3S | 2/17 | 11.8% | +2.00% | **+0.24%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.25% | **+0.94%** |
| MARKET_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.75% | **+0.64%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$644.00** / 初期 $100.00 (+544.00%)
- 確定: 4085件 (Win 1281 / Loss 1344 / Flat 1460) / skip 4093件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $644.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$153.59** / 初期 $100.00 (+53.59%)
- 確定: 1680件 (Win 482 / Loss 406 / Flat 792) / skip 3348件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0795 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $153.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.94** / 初期 $100.00 (+17.94%)
- 確定: 1565件 (Win 477 / Loss 599 / Flat 489) / pending 1件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000311 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.94

## 6. Latest Market Context

- 更新: 2026-08-14T23:11:15.568973+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=62866.0
- Funnel: target 985 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +22.06% | $6,720,184.29 |
| HEI/USDT:USDT | +18.07% | $5,280,475.35 |
| ACE/USDT:USDT | +16.99% | $74,730,968.02 |
| DOLO/USDT:USDT | +13.73% | $1,643,189.73 |
| GUN/USDT:USDT | +10.90% | $1,021,092.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +3.21% | +3.19% |
| BTW/USDT:USDT | below_1h_threshold | +1.08% | +1.06% |
| US/USDT:USDT | below_1h_threshold | +0.79% | +0.77% |
| RE/USDT:USDT | below_1h_threshold | +0.73% | +0.72% |
| EDEN/USDT:USDT | below_1h_threshold | +0.44% | +0.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
