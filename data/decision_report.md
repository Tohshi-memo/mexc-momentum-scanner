# Decision Report

- generated_at: 2026-08-14T23:01:19.125185+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11615**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11615, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.65% | **-0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.65% | **+0.93%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.29% | **+0.71%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.56% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.25% | **+0.94%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.73% | **+0.78%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.21% | **+0.60%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.99% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.83** / 初期 $100.00 (+540.83%)
- 確定: 4083件 (Win 1280 / Loss 1343 / Flat 1460) / skip 4093件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $640.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$153.08** / 初期 $100.00 (+53.08%)
- 確定: 1678件 (Win 481 / Loss 405 / Flat 792) / skip 3348件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0851 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $153.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.74** / 初期 $100.00 (+17.74%)
- 確定: 1563件 (Win 476 / Loss 598 / Flat 489) / pending 2件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000335 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.74

## 6. Latest Market Context

- 更新: 2026-08-14T23:01:10.888708+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=62860.4
- Funnel: target 985 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +26.52% | $73,546,490.31 |
| US/USDT:USDT | +22.19% | $6,714,914.31 |
| HEI/USDT:USDT | +15.16% | $4,835,563.79 |
| DOLO/USDT:USDT | +14.14% | $1,631,444.62 |
| GUN/USDT:USDT | +12.22% | $1,007,444.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +0.84% | +0.84% |
| CYS/USDT:USDT | below_1h_threshold | +0.73% | +0.72% |
| HEI/USDT:USDT | below_1h_threshold | +0.54% | +0.54% |
| DOLO/USDT:USDT | below_1h_threshold | +0.36% | +0.36% |
| BTW/USDT:USDT | below_1h_threshold | +0.31% | +0.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
