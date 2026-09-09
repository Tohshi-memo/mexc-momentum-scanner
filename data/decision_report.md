# Decision Report

- generated_at: 2026-09-09T12:11:20.611635+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14058**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.92% / filled 20/20。**
- 全期間 MARKET基準: n=14058, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.92% | **+2.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.92% | **+2.92%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.33% | **+1.98%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.75% | **+1.23%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.25% | **+1.13%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | +0.33% | **+0.20%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.94% | **-0.14%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | -1.05% | **-0.68%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$991.95** / 初期 $100.00 (+891.95%)
- 確定: 5313件 (Win 1594 / Loss 1715 / Flat 2004) / skip 5306件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IOST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $991.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.39** / 初期 $100.00 (+90.39%)
- 確定: 2657件 (Win 729 / Loss 623 / Flat 1305) / skip 4812件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IOST/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $190.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.95** / 初期 $100.00 (+17.95%)
- 確定: 2619件 (Win 765 / Loss 1000 / Flat 854) / pending 1件 / skip 2911件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CRO/USDT:USDT `MARKET` EXPIRED account +0.11% 残高後 $117.95

## 6. Latest Market Context

- 更新: 2026-09-09T12:11:08.298149+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=79389.2
- Funnel: target 1064 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +59.72% | $1,662,853.23 |
| IOST/USDT:USDT | +33.82% | $6,033,991.60 |
| OL/USDT:USDT | +23.81% | $2,351,339.12 |
| BR/USDT:USDT | +18.55% | $1,473,023.64 |
| NIULAI/USDT:USDT | +17.67% | $2,759,614.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.21% | +3.08% |
| UAI/USDT:USDT | below_1h_threshold | +1.33% | +1.20% |
| HNT/USDT:USDT | below_1h_threshold | +1.29% | +1.15% |
| ATOM/USDT:USDT | below_1h_threshold | +1.26% | +1.13% |
| USOIL/USDT:USDT | below_1h_threshold | +0.73% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
