# Decision Report

- generated_at: 2026-08-15T13:11:32.376644+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11666**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.20% / filled 20/20。**
- 全期間 MARKET基準: n=11666, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |
| LIMIT_2PCT | 12/20 | 60.0% | +2.02% | **+1.21%** |
| LIMIT_1PCT | 13/20 | 65.0% | +1.01% | **+0.66%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.52% | **+0.26%** |
| LIMIT_4PCT | 8/20 | 40.0% | +0.50% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +3.11% | **+0.93%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.55% | **+0.62%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.56% | **-0.14%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | -0.80% | **-0.52%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | -0.76% | **-0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4134件 (Win 1290 / Loss 1355 / Flat 1489) / skip 4093件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.13** / 初期 $100.00 (+55.13%)
- 確定: 1729件 (Win 491 / Loss 413 / Flat 825) / skip 3348件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1078 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.16** / 初期 $100.00 (+19.16%)
- 確定: 1608件 (Win 490 / Loss 608 / Flat 510) / pending 5件 / skip 1525件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000622 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $119.16

## 6. Latest Market Context

- 更新: 2026-08-15T13:11:18.154522+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63019.1
- Funnel: target 985 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COW/USDT:USDT | +56.00% | $7,237,437.29 |
| MOVR/USDT:USDT | +36.19% | $1,198,976.58 |
| WAL/USDT:USDT | +31.54% | $1,372,192.70 |
| VELVET/USDT:USDT | +24.39% | $30,952,760.71 |
| ANSEM/USDT:USDT | +23.94% | $1,657,538.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +4.46% | +4.47% |
| TUT/USDT:USDT | below_1h_threshold | +2.99% | +3.01% |
| H/USDT:USDT | below_1h_threshold | +2.68% | +2.70% |
| AIO/USDT:USDT | below_1h_threshold | +1.69% | +1.70% |
| BMT/USDT:USDT | below_1h_threshold | +1.68% | +1.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
